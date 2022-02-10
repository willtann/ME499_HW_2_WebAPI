#! Users/tannerwilliams/Desktop/ME499/ME499_HW_2_WebAPI
import time
from datetime import datetime
# requests if for getting data from the API
import requests
import os.path


""" References
    [1] https://stackoverflow.com/questions/30921399/datetime-fromtimestamp-vs-datetime-utcfromtimestamp-which-one-is-safer-to-use
    [2] https://www.geeksforgeeks.org/python-os-path-isdir-method/
    [3] https://www.geeksforgeeks.org/python-os-mkdir-method/
    [4]
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
    current = datetime.utcfromtimestamp(epoch)  # [1]
    # return current.isoformat()
    return current.date()


def query_carbon(iso=get_current_day(), use_cache=True):
    """
    :param iso: example: if not provided in form '2022-02-07 09:31:26.596621 (str)' then retrieve current date
    :param use_cache: data is in file (boolean)
        1. Data in file?
            - TRUE, good
            - FALSE, retrieve it and store it
    :return:
    """
    # See if directory with data exists
    if not os.path.isdir('data'):  # [2]
        # If directory doesn't exist; make one.
        os.mkdir('data')  # [3]
        data_folder = True
    # If we have the data folder and use_cache is True
    if use_cache and data_folder:

    # If use_cache is false we need to retrieve it from the URL and ignore any cache files
    elif:
        # Sending request

        # Check if status code from URL is 200

        # If it is not 200 raise exception
            raise ValueError('Status Code Error: Not 200')
        # Otherwise, get data from dictionary retrieved from URL


if __name__ == '__main__':
    print(get_current_day())
    print(query_carbon())
