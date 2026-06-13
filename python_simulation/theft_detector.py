def detect_theft(in_geofence):

    if not in_geofence:
        return "THEFT ALERT"

    return "SAFE"