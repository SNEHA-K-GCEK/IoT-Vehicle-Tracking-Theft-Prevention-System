import pandas as pd
import folium

data = pd.read_csv(
    "../data/location_history.csv"
)

m = folium.Map(
    location=[
        data.iloc[-1]["Latitude"],
        data.iloc[-1]["Longitude"]
    ],
    zoom_start=15
)

for _, row in data.iterrows():

    folium.Marker(
        [row["Latitude"],
         row["Longitude"]]
    ).add_to(m)

m.save("../outputs/vehicle_map.html")

print("Map Generated")