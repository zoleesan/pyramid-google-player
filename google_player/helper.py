""" Helper utilities
"""

from datetime import datetime


def resort_by_added(lib):
    """ Resort songs by added
    """
    return sorted(lib, key=lambda x: x['creationTimestamp'])


def get_datetime(ts):
    """ Convert string timestamp to datetime object
    """
    d = datetime.fromtimestamp(float(ts[:10]))
    return d
