from datetime import datetime, timedelta


def get_current_date():  # returns current date in format YYYY-MM-DD HH:MM:SS (string)
    return str(datetime.now())[:-7]


def write_time(file, time):
    with open(file, 'a') as f:
        if f.tell() == 0:
            f.write(time)
        else:
            f.write("\n" + time)
    f.close()


def str_to_date(str_list):
    return [datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in str_list]


def select_date(date_list, date):
    return [dt for dt in date_list if dt.date() == date]


def read_time(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    return lines


def sum_time(date_list):
    result = timedelta()

    # loop over the datetime objects in the list and update the result
    for i in range(0, len(date_list), 2):
        pair = (date_list[i], None)  # initialize pair with second element as None
        if i + 1 < len(date_list):  # check if index i + 1 is within bounds of datetimes
            pair = (date_list[i], date_list[i + 1])  # create pair of datetime objects
        try:
            result += pair[1] - pair[0]  # add difference of pair to result
        except Exception as e:
            print(e)

    return result


def sum_all(date_list):
    """Not in use"""
    time_differences = [date_list[i + 1] - date_list[i] for i in range(len(date_list) - 1)]
    entries = len(time_differences)
    if entries == 1:
        seconds = time_differences[0].seconds
    elif entries > 1:
        seconds = sum(time_differences, timedelta())
        seconds = seconds.seconds
    else:
        seconds = 0
    return seconds


def time_delta(time2, time1):
    """Return minutes between time from file and current time
    time_from is the time read from the file, %Y-%m-%d %H:%M:%S
    Return the difference in minutes
    """
    t1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")

    return (t2 - t1).total_seconds() / 60


def shutdown_handler(time_file):
    now_shutdown = get_current_date()
    write_time(time_file, now_shutdown)


class ConfigureTime:

    def __init__(self, time_per_day, max_time):
        seconds = max_time - time_per_day
        dt = timedelta(seconds=seconds)
        self.time = dt

    def add_more_sec(self, sec):
        self.time += timedelta(seconds=sec)

    def hms(self):
        time_str = self.time.__str__()
        return time_str.split(":")
