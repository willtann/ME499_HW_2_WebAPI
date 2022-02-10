#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_2_WebAPI
import requests
from datetime import datetime
import time
import os.path
import os
""" Don't put a request in a loop or website will kick your IP """
""" Assume all days start at midnight """


def get_current_day(timestamp=time.time()):
    """ Problem 1: Setup """

    """
    :param timestamp: number of seconds since 1 January 1970
    :return: UTC date (string)
    """
    return datetime.fromtimestamp(timestamp)


def query_carbon(iso_date=datetime.today().isoformat(), use_cache=True):
    """ Problem 2: Data querying """
    """
    :param iso_date: example: 2022-02-07 09:31:26.596621 (str)
    :param use_cache: Check if data is in json file (boolean)
        1. File exist?
            - TRUE, good
            - FALSE, get it and store it
    :return:
    """

    if not os.path.isdir('data'):  # Check that directory exists
        os.mkdir('data')
        print('Not a directory')
    carbon_date_known = datetime.strptime('carbon_2019-10-31.json')  # Make string
    filename = os.path.join('data', 'data/carbon_2019-10-31.json')
    file_exists = True

    if use_cache and file_exists:
        curr_day = datetime.fromtimestamp().isoformat()
        print('Using cashed file to get data')
        return {}
    else:
        # If file doesn't exist
        headers = {'Accept':'application/json'}
        known_date = 'https://api.carbonintensity.org.uk/intensity/2019-10-31T0941:15?:584382'
        response = requests.get(known_date, params = {}, headers = headers)  # DONT RUN EXCESSIVELY
        print(response.status_code)
        print(response.json())



def plot_carbon():
    """ Problem 3: Plotting """

    """
    :param iso_date: example: 2022-02-07 09:31:26.596621 (str)
    :return: dictionary 
    """


if __name__ == '__main__':
    get_current_day()
    query_carbon()
    """ Testing query carbon """
    assert isinstance(query_carbon()) == type({}), 'Type is not dictionary'