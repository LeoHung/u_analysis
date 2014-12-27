import numpy as np
import matplotlib.dates as mdates
import csv 

def load_stations(filename):
    sid2data = {}

    reader = csv.reader(open(filename), delimiter=';' )
    for row in reader:
        sid = int(row[0])
        name = row[1]
        e_name = row[3]
        lat = float(row[5])
        lng = float(row[6])
        sid2data[sid] = {
            'sid': sid,
            'name': name,
            'e_name': e_name,
            'lat': lat,
            'lng': lng 
        }
    return sid2data

def load_data(filename):
    times, station_ids, empty_slots, available_bike = np.loadtxt(
        filename, 
        skiprows= 1,
        unpack=True,
        delimiter=";",
        usecols= (5, 1, 2, 3),
        converters={ 
            5: mdates.strpdate2num('"%Y-%m-%d %H:%M:%S"'),
            1: lambda x: int(x[1:-1]),
            2: lambda x: int(x[1:-1]),
            3: lambda x: int(x[1:-1])
        }
    )
    return times, station_ids, empty_slots, available_bike
