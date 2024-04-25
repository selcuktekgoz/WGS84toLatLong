from os import path
from datetime import datetime
import pandas as pd
from pyproj import Transformer

# enlem: 37.9698 ve boylam: 34.6766

states = pd.read_csv("epsg.csv")


def open_file(file_name):
    file = []
    with open(file_name, "r") as f:
        file_name = path.basename(f.name)
        file.append(file_name)
        for row in f:
            x, y = map(float, row.strip().split(','))
            file.append((x, y))
    return file


def convert_wgs84_to_lat_long(region, state, dest_epsg=4326):

    state_code = states[states["IL"] == state]["EPSG"].values[0]

    transformer = Transformer.from_crs(f"EPSG:{state_code}", "EPSG:4326")

    dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    file_name = region[0]

    new_file_name = f"{file_name.split('.')[0]}_{dt}.csv"

    lats, longs = [], []

    for x,y in region[1:]:
        lat, long = transformer.transform(y, x)
        lats.append(lat)
        longs.append(long)

    df = pd.DataFrame({"LATITUDE":lats, "LONGITUDE":longs})

    df.to_csv(new_file_name, sep=";", index=False)

    return df

file = open_file("ahipasa_mah.txt")
df = convert_wgs84_to_lat_long(file,"Niğde")

