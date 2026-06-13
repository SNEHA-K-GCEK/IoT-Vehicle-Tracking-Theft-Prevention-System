import csv
import os

FILE = "data/location_history.csv"


def create_file():

    if not os.path.exists(FILE):

        with open(FILE, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Latitude",
                "Longitude",
                "Status"
            ])


def log_data(lat, lon, status):

    with open(FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            lat,
            lon,
            status
        ])