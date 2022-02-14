#! Users/tannerwilliams/Desktop/ME499/ME499_HW_2_WebAPI
import time
from datetime import datetime
# requests if for getting data from the API
import requests
import os.path
import os
import json
import matplotlib.pyplot as plt
import numpy


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
    :param iso: example: if not provided in form '2022-02-07 (str)' then retrieve current date
    :param use_cache: data is in file (boolean)
        1. Data in file?
            - TRUE, good
            - FALSE, retrieve it and store it
    :return:
    """
    if use_cache:
        # If use_cache is true
        data_path = "data/carbon_%s.json" % iso
        if os.path.exists(data_path):
            print('File exists in sub-directory')
            with open(data_path, 'r') as json_iso:
                # load data for specified date 'iso'
                # Convert json file to dictionary to use
                return json.load(json_iso)  # [4]

        else:  # File does not exist in data folder
            print('Fetch data from URL')
            headers = {'Accept': 'application/json'}
            # Sending request
            url = 'https://api.carbonintensity.org.uk/intensity/date/%s' % iso
            data_from_url = requests.get(url, params={}, headers=headers)
            print(type(data_from_url))
            # Check if status code from URL is 200
            if not data_from_url.status_code == 200:
                raise Exception('Bad Request or Internal Server Error')
            else:
                with open(data_path, 'w') as json_iso:
                    # Save dictionary to json file
                    json.dump(data_from_url.json(), json_iso)
            # Return usable dictionary right away
            return data_from_url.json()


def plot_carbon(iso=get_current_day()):
    """
    :param iso:example: if not provided in form '2022-02-07 (str)' then retrieve current date
    :return: Plot of actual and predicted carbon intensity for the specified day.
    """
    # Dictionary of data from date
    iso_data = query_carbon(iso)
    # float from 0 (inclusive) to 24 (noninclusive) representing the time from start of day
    t = list(numpy.arange(0, 24, 0.5))

    # Empty lists for storing values from file
    forecast = []
    actual = []

    # Create a blank plot for plotting
    plt.savefig("plots/carbon_%s.png" % iso)
    plt.xlabel('Time (hr)')
    plt.xlim(0, 23.5)
    plt.locator_params(axis='x', nbins=24)
    plt.ylabel('Carbon Intensity')
    plt.title('Predicted and Realized Carbon Intensities for %s' % iso)
    plt.grid()

    # Go through each time frame (30 min) and extract the data from the intensity dict
    for timeframe in iso_data['data']:
        forecast.append(timeframe['intensity']['forecast'])  # Retrieving forecasted value
        actual.append(timeframe['intensity']['actual'])  # Retrieving actual intensity value

    plt.plot(t, forecast, label='Predicted Intensity')  # Plot and label for legend
    plt.plot(t, actual, label='Realized Intensity')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # print(get_current_day())
    # plot_carbon('2019-10-31')
    plot_carbon()
    # plot_carbon('2022-04-15')


