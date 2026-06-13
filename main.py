from python_simulation.gps_simulator import generate_gps
from python_simulation.geofence import check_geofence
from python_simulation.theft_detector import detect_theft
from python_simulation.logger import create_file
from python_simulation.logger import log_data

create_file()

gps = generate_gps()

for _ in range(30):

    lat, lon = next(gps)

    safe = check_geofence(lat, lon)

    status = detect_theft(safe)

    print("--------------------------------")
    print("Latitude :", lat)
    print("Longitude:", lon)
    print("Status   :", status)

    maps_url = (
        f"https://www.google.com/maps?q={lat},{lon}"
    )

    print("Map Link :", maps_url)

    log_data(lat, lon, status)