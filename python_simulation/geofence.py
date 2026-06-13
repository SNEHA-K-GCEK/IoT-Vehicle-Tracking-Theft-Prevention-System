import math

SAFE_LAT = 8.5241
SAFE_LON = 76.9366

RADIUS = 0.003


def check_geofence(lat, lon):

    distance = math.sqrt(
        (lat - SAFE_LAT) ** 2 +
        (lon - SAFE_LON) ** 2
    )

    if distance > RADIUS:
        return False

    return True