from datetime import datetime


def resort_by_added(lib):
    return sorted(lib, key=lambda x: x['creationTimestamp'])


def get_datetime(ts):
    d = datetime.fromtimestamp(float(ts[:10]))
    return d
