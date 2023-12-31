# -*- coding: utf-8 -*-
"""IOWC-rainfall-selection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kqAs60vHHqoVnbWpsKnRi1gK6C1xxhDr
"""

import pandas as pd

avg_rainfall_threshold = 100

df = pd.read_csv('/content/all_stations_data.csv')

# Define season
# winter: Dec - Feb
# spring: Mar - May
# summer: Jun - Aug
# autumn: Sept - Nov

# In the new csv file, the date column is the date of the first month of the season

# The data for the new dataframe
data = []
data_less_threshold = []
data_more_threshold = []

# row ID
ID = 1
ID_more_threshold = 1
ID_less_threshold = 1

# first station
station = df.loc[0, "Location Name"]
lat = df.loc[0, "Latitude"]
lon = df.loc[0, "Longitude"]

months = []

j = 0 # df row index

len_df = len(df)

while j < len_df:

    # a new station, recount months
    if df.loc[j, "Location Name"] != station or j == len_df-1:

        # process the previous station

        # start with the first month available
        k = 0

        while k < len(months)-2:

            if months[k][1] in [12, 3, 6, 9]:

                count_consec_months = 1

                # check the next two months
                for i in range(1,3):
                    if (months[k+i][0] == months[k+i-1][0] and \
                        months[k+i][1] - months[k+i-1][1] == 1) or \
                         (months[k+i][0] - months[k+i-1][0] == 1 and \
                          months[k+i-1][1] - months[k+i][1] == 11):
                        count_consec_months += 1

                if count_consec_months == 3:

                    """
                    If you want to change the date displayed in the new csv file, change here
                    """
                    date = str(months[k][0]) + "-" + str(months[k][1]) + "-" + "01"

                    rainfall_total = months[k][2] + months[k+1][2] + months[k+2][2]

                    avg_total = months[k][3] + months[k+1][3] + months[k+2][3]

                    anomaly = round(rainfall_total / avg_total * 100, 2)

                    data.append([ID, station, lat, lon, date, rainfall_total, avg_total, anomaly])

                    if avg_total >= avg_rainfall_threshold:
                        data_more_threshold.append([ID_more_threshold, station, \
                                                    lat, lon, date, rainfall_total, avg_total, anomaly])
                        ID_more_threshold += 1

                    if avg_total < avg_rainfall_threshold:
                        data_less_threshold.append([ID_less_threshold, station, \
                                                    lat, lon, date, rainfall_total, avg_total, anomaly])
                        ID_less_threshold += 1

                    ID += 1
                    k += 3

                else:
                  k += 1

            else:
                k += 1


        if j == len_df - 1:
            break

        # update the station
        station = df.loc[j, "Location Name"]
        lat = df.loc[j, "Latitude"]
        lon = df.loc[j, "Longitude"]
        months.clear()

    else:
        year = int(df.loc[j, "Date"][0:4])
        month = int(df.loc[j, "Date"][5:7])
        rainfall = round(df.loc[j, "Rainfall (mm)"], 5)
        avg_rainfall = round(df.loc[j, "Avg Rainfall (mm)"], 5)
        months.append([year, month, rainfall, avg_rainfall])
        j += 1

columns = ['ID','Location Name','Latitude','Longitude','Date','Rainfall (mm)','Avg Rainfall (mm)','Rainfall (% anomaly)']
full_new_df = pd.DataFrame(data, columns=columns)
more_threshold_new_df = pd.DataFrame(data_more_threshold, columns=columns)
less_threshold_new_df = pd.DataFrame(data_less_threshold, columns=columns)

full_new_df.to_csv('/content/rainfall_seasonal.csv')
more_threshold_new_df.to_csv('/content/rainfall_seasonal_rainy.csv')
less_threshold_new_df.to_csv('/content/rainfall_seasonal_dry.csv')