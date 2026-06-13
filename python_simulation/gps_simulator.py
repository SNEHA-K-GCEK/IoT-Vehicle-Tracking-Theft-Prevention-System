import random
import time

def generate_gps():

    lat = 8.5241
    lon = 76.9366

    while True:

        lat += random.uniform(-0.0005, 0.0005)
        lon += random.uniform(-0.0005, 0.0005)

        yield lat, lon

        time.sleep(1)