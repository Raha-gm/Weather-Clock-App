# Weather Clock App 🌤️

A simple desktop application that displays a digital clock and provides real-time weather information for selected cities.

## Features

- Digital clock with automatic updates every second
- Weather information for nine Iranian cities
- Current temperature display
- Weather condition descriptions
- City selection through a dropdown menu
- Simple graphical user interface

## Supported Cities

- Tehran
- Tabriz
- Gilan
- Isfahan
- Shiraz
- Mashhad
- Ahvaz
- Sari
- Urmia

## Technologies Used

- Python
- CustomTkinter
- Requests
- Open-Meteo API
- Datetime

## Project Structure

```text
Weather-Clock-App/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python main.py
```

## Requirements

- Python 3
- Internet connection for weather information
- Morabba font installed on your system for the intended interface appearance

## Weather Data

Weather information is provided by the [Open-Meteo API](https://open-meteo.com/).

The application retrieves the current temperature and weather conditions based on the selected city's coordinates.

---

Created as a beginner Python project.
