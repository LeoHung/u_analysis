
from load import load_data
import numpy as np
import matplotlib.dates as mdates

def extract(times, station_ids, empty_slots, start_time, end_time):
    
    filt = (start_time <= times)
    station_ids = station_ids[filt]
    empty_slots = empty_slots[filt]
    times = times[filt]

    filt = (times <= end_time)
    station_ids = station_ids[filt]
    empty_slots = empty_slots[filt]
    times = times[filt]

    return times, station_ids, empty_slots

def extract_2(filename, output_filename, start_time, end_time):
    
    outf = open(output_filename, 'w')

    f = open(filename)
    f.readline()

    fmtp = mdates.strpdate2num('"%Y-%m-%d %H:%M:%S"')

    for l in f:
        tmp = l.strip().split(";")
        t = fmtp(tmp[5])
        # print start_time , t, tmp[5], end_time
        if start_time <= t and t <= end_time:
            # print "in"
            print >>outf, l.strip()

    f.close()
    outf.close()

if __name__ == "__main__":

    start_time = mdates.strpdate2num("%Y-%m-%d %H:%M:%S")("2013-09-13 00:00:00")
    end_time = mdates.strpdate2num("%Y-%m-%d %H:%M:%S")("2013-09-27 00:00:00")

    extract_2("../../ubike_record.csv", "../ubike_record.09_13_09_26.csv", start_time, end_time)

    # times, station_ids, empty_slots = load_data("../../ubike_record.csv")
    # times, station_ids, empty_slots = load_data("../ubike_record.1000.csv")
    # times, station_ids, empty_slots = extract(times, station_ids, empty_slots, start_time, end_time)

    # np.savetxt("../ubike_record.9_13_9_26.txt", [times, station_ids, empty_slots])