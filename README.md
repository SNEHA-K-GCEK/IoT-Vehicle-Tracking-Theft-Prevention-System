# IoT Vehicle Tracking & Theft Prevention System

## Overview

This project is an IoT-based Vehicle Tracking and Theft Prevention System that monitors vehicle location in real time using GPS coordinates. The system tracks vehicle movement, checks whether it remains within a safe zone (Geofence), generates theft alerts when unauthorized movement is detected, and stores location history for future analysis.

The project is designed for students and beginners while following industry concepts used in fleet management and vehicle security systems.

---

## Problem Statement

Vehicle theft and unauthorized vehicle usage are common problems. Traditional vehicle security systems often lack real-time monitoring capabilities.

This project aims to:

- Track vehicle location continuously
- Detect vehicle movement outside a safe area
- Generate theft alerts
- Store historical route information
- Visualize vehicle movement on a dashboard

---

## Features

### Vehicle Tracking
- Real-time GPS coordinate monitoring
- Live location updates

### Theft Prevention
- Geofence-based monitoring
- Theft alert generation

### Dashboard Visualization
- Route visualization
- Interactive map generation

### Data Logging
- CSV-based location history
- Status monitoring

### Google Maps Integration
- Automatic Google Maps links

---

## Project Architecture

```
GPS Coordinates
       ↓
GPS Simulator
       ↓
Vehicle Tracking Engine
       ↓
Geofence Detection
       ↓
Theft Detection
       ↓
CSV Logger
       ↓
Dashboard Visualization
       ↓
Map Output
```

---

## Folder Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System/

│
├── arduino_code/
├── python_simulation/
│   ├── gps_simulator.py
│   ├── geofence.py
│   ├── theft_detector.py
│   └── logger.py
│
├── dashboard/
│   └── map_dashboard.py
│
├── data/
│   └── location_history.csv
│
├── outputs/
│   └── vehicle_map.html
│
├── images/
├── reports/
├── docs/
│
├── requirements.txt
├── main.py
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- Folium
- Git
- GitHub

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/IoT-Vehicle-Tracking-Theft-Prevention-System.git
```

### Enter Project Directory

```bash
cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run Vehicle Tracking Simulation

```bash
python main.py
```

### Generate Dashboard Map

```bash
python dashboard/map_dashboard.py
```

---

## Sample Output

```text
Latitude : 8.5242
Longitude: 76.9368
Status   : SAFE

Google Maps:
https://www.google.com/maps?q=8.5242,76.9368
```

---

## Theft Detection Logic

The project uses a Geofence mechanism.

If:

Distance from Safe Zone > Allowed Radius

Then:

THEFT ALERT

Otherwise:

SAFE

---

## Output Files

### CSV Log

```
data/location_history.csv
```

Contains:

- Latitude
- Longitude
- Status

### Dashboard Map

```
outputs/vehicle_map.html
```

Displays tracked vehicle locations on an interactive map.

---

## Future Improvements

- ESP32 Integration
- Real GPS Module
- MQTT Communication
- ThingSpeak Dashboard
- Blynk Mobile Application
- SMS Notifications
- Email Alerts
- Remote Engine Lock
- AI-based Theft Prediction

---

## Industry Applications

- Logistics Fleet Tracking
- Delivery Vehicles
- School Bus Monitoring
- Personal Vehicle Security
- Asset Tracking
- Rental Vehicle Monitoring

---

## Learning Outcomes

After completing this project, students will understand:

- GPS Tracking
- IoT Fundamentals
- Geofencing
- Vehicle Security Systems
- Cloud Dashboards
- Data Logging
- GitHub Project Management

---

## Author

Student IoT Project

IoT Vehicle Tracking & Theft Prevention System