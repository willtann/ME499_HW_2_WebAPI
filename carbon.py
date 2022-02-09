#! Users/tannerwilliams/Desktop/ME499/ME499_HW_2_WebAPI
import time
from datetime import datetime
# requests if for getting data from the API
import requests


""" Problem 1: Setup """
""" References:
    https://stackoverflow.com/questions/30921399/datetime-fromtimestamp-vs-datetime-utcfromtimestamp-which-one-is-safer-to-use
    
    """


def get_current_day(epoch=time.time()):
    """
    :param epoch: number of seconds since 1 January 1970 'Unix epoch timestamp'
    :return: UTC date (string) in form 'YYYY-MM-DD...'
    """
    # return the current time since epoch to print the current UTC time
    # current_time = datetime.datetime.utcfromtimestamp(epoch)
    # return datetime.datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
    current = datetime.utcfromtimestamp(epoch)
    return current.isoformat()


def query_carbon(iso=get_current_day(), use_cache=True):
    """
    :param iso: example: 2022-02-07 09:31:26.596621 (str)
    :param use_cache: Check if data is in json file (boolean)
        1. File exist?
            - TRUE, good
            - FALSE, get it and store it
    :return:
    """
    headers = {'Accept': 'application/json'}
    r = requests.get('https://api.carbonintensity.org.uk/intensity/date/{date}', params={}, headers=headers)
    return r.json()


if __name__ == '__main__':
    print(get_current_day())
    print(query_carbon())
