from load import load_data, load_stations
import numpy as np
import matplotlib.dates as mdates
import json

def get_hour(times):
    return np.array([mdates.num2date(t).hour for t in times ])

def get_minute(times, delta):
    return np.array([(mdates.num2date(t).minute/ delta) * delta for t in times])

def main(filename, station_filename, output_filename):
    times, station_ids, empty_slots, available_bikes = load_data(filename)
    sid2data = load_stations(station_filename)

    total_slots = np.add(empty_slots, available_bikes)
    # gen empty_ratio 
    empty_ratios = np.divide(empty_slots, total_slots)
    # gen available ratio
    available_bike_ratios = np.divide(available_bikes, total_slots)

    # gen hours 
    hours = get_hour(times)
    # gen minutes
    minutes = get_minute(times, delta=15)

    # for each 15 minutes generate a snap shot
    data = []
    for h in range(24):
        for m in range(0, 60, 15):
            slot_station_ids = station_ids[ hours == h & minutes == m]
            slot_available_bike_ratios = available_bike_ratios[ hours == h & minutes == m]

            slot_data = {}
            slot_data['hour'] = h 
            slot_data['minute'] = m
            slot_data['station'] = []
            for station_id in range(1, 119+1):
                mean_available_bike_ratio = np.mean(slot_available_bike_ratios[slot_station_ids == station_id])
                slot_data['station'].append({
                    'bike_ratio': mean_available_bike_ratio, 
                    'name': sid2data[station_id]['name'],
                    'e_name': sid2data[station_id]['e_name'],
                    'lat': sid2data[station_id]['lat'],
                    'lng': sid2data[station_id]['lng'],
                    'sid': station_id
                })

            data.append(slot_data)
    
    # print out 
    outf = open(output_filename, 'w')
    print >> outf, json.dumps(data)
    outf.close()

if __name__ == "__main__":
    main()