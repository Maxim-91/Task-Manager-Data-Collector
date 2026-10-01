import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import time
import threading
import psutil


# noinspection PyInterpreter
class DataCollectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Data Collector")
        self.root.geometry("900x500")

        self.collecting = False
        self.start_time = None
        self.data = []

        # Start / Stop button
        self.start_button = tk.Button(
            root,
            text="Start",
            width=20,
            command=self.toggle_collection
        )
        self.start_button.pack(pady=10)

        # Export button
        self.export_button = tk.Button(
            root,
            text="Export CSV",
            width=20,
            state=tk.DISABLED,
            command=self.export_csv
        )
        self.export_button.pack(pady=5)

        # Table
        columns = (
            "seconds",
            "running_processes",
            "cpu_percent",
            "ram_mb",
            "ram_percent",
            "disk_mbps"
        )

        self.table = ttk.Treeview(
            root,
            columns=columns,
            show="headings"
        )

        self.table.heading("seconds", text="Seconds")
        self.table.heading("running_processes", text="Running Processes")
        self.table.heading("cpu_percent", text="CPU %")
        self.table.heading("ram_mb", text="RAM MB")
        self.table.heading("ram_percent", text="RAM %")
        self.table.heading("disk_mbps", text="Disk MB/s")

        self.table.column("seconds", width=80)
        self.table.column("running_processes", width=150)
        self.table.column("cpu_percent", width=100)
        self.table.column("ram_mb", width=120)
        self.table.column("ram_percent", width=100)
        self.table.column("disk_mbps", width=120)

        self.table.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

    def toggle_collection(self):
        if not self.collecting:
            self.start_collection()
        else:
            self.stop_collection()

    def start_collection(self):
        # Clear previous data
        self.data.clear()

        for item in self.table.get_children():
            self.table.delete(item)

        self.collecting = True
        self.start_time = time.time()

        self.start_button.config(text="Stop")
        self.export_button.config(state=tk.DISABLED)

        # Start data collection in a separate thread
        self.collection_thread = threading.Thread(
            target=self.collect_data,
            daemon=True
        )
        self.collection_thread.start()

    def stop_collection(self):
        self.collecting = False

        self.start_button.config(text="Start")
        self.export_button.config(state=tk.NORMAL)

    def collect_data(self):
        seconds = 0

        # Initialize CPU measurement
        psutil.cpu_percent(interval=None)

        previous_disk = psutil.disk_io_counters()

        while self.collecting:
            time.sleep(1)

            seconds += 1

            # CPU
            cpu_percent = psutil.cpu_percent(interval=None)

            # RAM
            memory = psutil.virtual_memory()
            ram_mb = memory.used / (1024 * 1024)
            ram_percent = memory.percent

            # Number of running processes
            running_processes = len(psutil.pids())

            # Disk activity
            current_disk = psutil.disk_io_counters()

            read_bytes = (
                current_disk.read_bytes -
                previous_disk.read_bytes
            )

            write_bytes = (
                current_disk.write_bytes -
                previous_disk.write_bytes
            )

            disk_bytes = read_bytes + write_bytes

            # Bytes -> MB per second
            disk_mbps = disk_bytes / (1024 * 1024)

            previous_disk = current_disk

            row = (
                seconds,
                running_processes,
                round(cpu_percent, 2),
                round(ram_mb, 2),
                round(ram_percent, 2),
                round(disk_mbps, 2)
            )

            self.data.append(row)

            # Update GUI from main thread
            self.root.after(
                0,
                self.add_row_to_table,
                row
            )

    def add_row_to_table(self, row):
        if self.collecting:
            self.table.insert("", tk.END, values=row)

    def export_csv(self):
        if not self.data:
            messagebox.showwarning(
                "No data",
                "There is no data to export."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        headers = [
            "seconds",
            "running_processes",
            "cpu_percent",
            "ram_mb",
            "ram_percent",
            "disk_mbps"
        ]

        try:
            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow(headers)
                writer.writerows(self.data)

            messagebox.showinfo(
                "Success",
                "Data successfully saved to CSV."
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not save file:\n{error}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = DataCollectorApp(root)
    root.mainloop()
