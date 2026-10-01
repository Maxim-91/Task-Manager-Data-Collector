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

[Video demonstration](https://youtu.be/LHjtmtJ_Qcg)

## Data collection and possible machine learning

Ohjelma kerää tietoa tietokoneen suorituskyvystä kerran sekunnissa.

Kerättävät sarakkeet ovat:

* `seconds` – kuinka monta sekuntia tiedonkeruu on kestänyt
* `running_processes` – käynnissä olevien prosessien määrä
* `cpu_percent` – prosessorin käyttö prosentteina
* `ram_mb` – käytetyn RAM-muistin määrä megatavuina
* `ram_percent` – RAM-muistin käyttö prosentteina
* `disk_mbps` – levyn käyttö megatavuina sekunnissa

Näiden tietojen avulla voidaan tarkastella tietokoneen kuormitusta ja eri resurssien käyttöä. Dataa voidaan myöhemmin käyttää koneoppimismallin opettamiseen.

Mahdollinen malli voisi esimerkiksi ennustaa tulevaa CPU:n käyttöä tai luokitella tietokoneen kuormituksen matalaksi, keskitasoiseksi tai korkeaksi.

---

## AI Tool Usage

The AI tool ChatGPT was used to support the writing and development of the code, as well as to translate texts into English and Finnish.
