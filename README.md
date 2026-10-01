# Task Manager Data Collector

A simple Python application for collecting computer performance data every second and saving the results as a CSV file.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in a terminal.
3. Install the required library:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python main.py
```

## How the Program Works

When the program starts, click **Start** to begin collecting data.

The program collects the following information every second:

* Number of running processes
* CPU usage (%)
* Used RAM (MB)
* RAM usage (%)
* Disk activity (MB/s)

The collected data is displayed in the table.

Click **Stop** to stop data collection. The **Export CSV** button will then become available.

Click **Export CSV** to save the collected data as a `.csv` file.

When **Start** is pressed again, the previous data is cleared and a new data collection session begins.

## Video Demonstration

[Video demonstration](PASTE_VIDEO_LINK_HERE)
