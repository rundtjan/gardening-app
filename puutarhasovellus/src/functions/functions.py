import time

def timestamp_from_date(date):
    if not date:
        return -1
    return int(time.mktime(date.timetuple()))