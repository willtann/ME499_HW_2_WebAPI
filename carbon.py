#! Users/tannerwilliams/Desktop/ME499/ME499_HW_2_WebAPI
import time
from datetime import datetime
# requests if for getting data from the API
import requests
import os.path
import os
import json


""" References
    [1] https://stackoverflow.com/questions/30921399/datetime-fromtimestamp-vs-datetime-utcfromtimestamp-which-one-is-safer-to-use
    [2] https://www.geeksforgeeks.org/python-os-path-isdir-method/
    [3] https://www.geeksforgeeks.org/python-os-mkdir-method/
    [4] https://www.geeksforgeeks.org/read-json-file-using-python/
    [5]
    [6]
    [7]
    [8]
    [9]
    """


def get_current_day(epoch=time.time()):
    """
    :param epoch: number of seconds since 1 January 1970 'Unix epoch timestamp'
    :return: UTC date (string) in form 'YYYY-MM-DD...'
    """
    # return the current time since epoch to print the current UTC time
    date = datetime.utcfromtimestamp(epoch).isoformat()  # [1]
    return date[:10]


def query_carbon(iso=get_current_day(), use_cache=True):
    """
    :param iso: example: if not provided in form '2022-02-07 09:31:26.596621 (str)' then retrieve current date
    :param use_cache: data is in file (boolean)
        1. Data in file?
            - TRUE, good
            - FALSE, retrieve it and store it
    :return:
    """

    # If use_cache is true
    if use_cache:
        try:
            print('Using cached file to get data')
            carbon_data = open('data/carbon_%s.json' % iso,'r')
            iso_data = json.load(carbon_data)  # [4]
        except FileNotFoundError:
            print('Psych that file doesnt exist... lets get it from the www')
            headers = {'Accept': 'application/json'}
            r = requests.get('https://api.carbonintensity.org.uk/intensity/%s' %iso,
                         params={}, headers=headers)
            print(r.status_code)
            print(r.json())




    # # If use_cache is false we need to retrieve it from the URL and ignore any cache files
    # elif:
    #     # Sending request
    #
    #     # Check if status code from URL is 200
    #
    #     # If it is not 200 raise exception
    #     raise Exception
    #     # Otherwise, get data from dictionary retrieved from URL


if __name__ == '__main__':
    print(get_current_day())
    # print(query_carbon('2019-10-31'))
    print(query_carbon())


