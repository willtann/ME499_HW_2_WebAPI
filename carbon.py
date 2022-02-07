
import requests
from datetime import datetime
import time
""" Don't put a request in a loop or website will kick your IP """
""" Assume all days start at midnight """


def get_current_day(timestamp=time.time()):
    """ Problem 1: Setup """

    """
    :param timestamp: Current day in UTC
    :return: UTC date (string)
    """
    date = datetime.fromtimestamp(timestamp)
    print(date)


def query_carbon(iso_date, use_cache):
    """ Problem 2: Data querying """
    """
    :param iso_date:
    :param use_cache: Check if data is in json file (boolean)
        1. File exist?
            - TRUE, good
            - FALSE, get it and store it
    :return:
    """


def plot_carbon(iso_date):
    """ Problem 3: Plotting """

    """
    :param iso_date: 
    :return: 
    """


if __name__ == '__main__':
    get_current_day()
