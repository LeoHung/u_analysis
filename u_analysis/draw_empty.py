import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from load import load_data

def plot(times ,values):

    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(times, values)

    start, end = ax.get_xlim()

    ticks = np.arange(start, end, (end-start) / 50.0 )
    ax.xaxis.set_ticks(ticks)

    formator = mdates.DateFormatter('%d %H:%M')
    ax.xaxis.set_major_formatter(formator)

    ax.grid(True)
    fig.autofmt_xdate()

    plt.show()

def main():
    filename = "../ubike_record.09_13_09_26.csv"
    # filename = "../../ubike_record.csv"

    times, station_ids, empty_slots, available_bike = load_data(filename)
    # fetch Taipei city goverment data
    start_t = mdates.strpdate2num("%Y-%m-%d %H:%M:%S")("2013-09-15 00:00:00")
    end_t = mdates.strpdate2num("%Y-%m-%d %H:%M:%S")("2013-09-16 00:00:00")

    station_ids = station_ids[times < end_t]
    empty_slots = empty_slots[times < end_t]
    times = times[times < end_t]

    station_ids = station_ids[start_t < times]
    empty_slots = empty_slots[start_t < times]
    times = times[start_t < times]

    station_id = 4 
    times = times[station_ids == station_id] 
    empty_slots = empty_slots[station_ids == station_id]
    available_bike = available_bike[station_ids == station_id]
    # plot 
    plot(times, available_bike)

if __name__ == "__main__":
    main()
