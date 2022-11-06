import datetime


def map_value(value, min_value, max_value, min_result, max_result):
    """maps value (or array of values) from one range to another"""
    result = min_result + (value - min_value) / (max_value - min_value) * (max_result - min_result)
    return result


def convert_in_seconds(time):
    date_time = datetime.strptime(time, "%H:%M:%S")
    print(date_time)
    a_timedelta = date_time - datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return seconds


def split(x, n):
    # If we cannot split the
    # number into exactly 'N' parts
    if x < n:
        return -1

    # If x % n == 0 then the minimum
    # difference is 0 and all
    # numbers are x / n
    elif x % n == 0:
        for i in range(n):
            return x // n
    else:
        # upto n-(x % n) the values
        # will be x / n
        # after that the values
        # will be x / n + 1
        zp = n - (x % n)
        pp = x // n
        res = []
        for i in range(n):
            if i >= zp:
                res.append(pp + 1)
            else:
                res.append(pp)
        return res
