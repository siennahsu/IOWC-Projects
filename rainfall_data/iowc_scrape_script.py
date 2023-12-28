# -*- coding: utf-8 -*-
"""IOWC-scrape-script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zpS0hjoYIQfB7u0QwYfG0hvpKf4_Zv8O
"""

START_YEAR = 1883
END_YEAR = 1885

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

# create a directory where the individual station data will be stored
individual_station_data_path = "./individual_station_data"
os.mkdir(individual_station_data_path)

# create the file for all stations' data
file_name = "all_stations_data.csv"
file_path = "./" + file_name

all_data_file = open(file_path, "w")
all_data_file.write("ID,Location Name,Latitude,Longitude,Date,Rainfall (mm),Avg Rainfall (mm),Rainfall (% anomaly)\n")

ID_all = 1

# read the html file of the search results
with open("/content/Climate Explorer_ Found station data.html") as fp:
    all_stations_soup = BeautifulSoup(fp, 'html.parser')

# gather all the station links
all_stations_links = all_stations_soup.find_all("a", text='get data')

# process each station's data

station_ID = 1

for station_link in all_stations_links:
    # go to the page of the station
    station_link = station_link['href']
    #station_link.replace("amp", "")
    url = station_link
    html = urlopen(url)
    station_link_soup = BeautifulSoup(html, 'lxml')

    # get the monthly rainfall data
    data_links = station_link_soup.find_all("a", text='raw data')
    first_raw_data_link = "https://climexp.knmi.nl/" + data_links[0]["href"]
    url = first_raw_data_link
    html = urlopen(url)
    first_raw_data_soup = BeautifulSoup(html, 'lxml')

    # get the mean montly rainfall data
    second_raw_data_link = "https://climexp.knmi.nl/" + data_links[1]["href"]
    url = second_raw_data_link
    html = urlopen(url)
    second_raw_data_soup = BeautifulSoup(html, 'lxml')

    # process the monthly rainfall data
    first_raw_data_content = first_raw_data_soup.find("p")
    first_raw_data_content = str(first_raw_data_content)
    first_raw_data_content = first_raw_data_content.split("\n")

    # get the location name
    location_name = first_raw_data_content[1]
    location_name = location_name.replace("#", "")
    replace_slash = ["/ ", " /", " / "]
    for slash in replace_slash:
        if slash in location_name:
            location_name = location_name.replace(slash, "/")
    location_name = ' '.join(location_name.split())

    # get the coordinates
    coordinates = [i for i in first_raw_data_content if "coordinates" in i][0]
    coordinates = coordinates.replace(",", "").replace("#", "")
    coordinates = coordinates.split()
    latitude = coordinates[1]
    longtitude = coordinates[2]

    # get the montly rainfall data from start year to end year
    data = []
    for year in range(START_YEAR, END_YEAR + 1):
        year = str(year)
        row = [i for i in first_raw_data_content if year in i][0]
        if row[0] == " ":
            row = row[1:]
        row = row.split()
        if len(row) != 13:
            raise Exception("Year " + year + "has missing data.")
        data.append(row)

    # format the monthly rainfall data and add the year and month
    year_and_rainfall = []
    for datapoint in data:
        year = datapoint[0]
        for i in range(1,13):
            if i > 9:
                month = str(i)
            else:
                month = '0' + str(i)

            date = year + "-" + month + "-01"
            rainfall = float(datapoint[i])
            year_and_rainfall.append([date, rainfall])

    # process the mean monthly rainfall data
    second_raw_data_content = second_raw_data_soup.find("p")
    second_raw_data_content = str(second_raw_data_content)
    second_raw_data_content = second_raw_data_content.split("\n")

    mean_rainfalls = []
    for i in range(1,13):
        if i > 9:
            month = str(i)
        else:
            month = "0" + str(i)
        month = "2000" + month + "01"
        monthly_data = [i for i in second_raw_data_content if month in i][0].split()
        mean_rainfall = monthly_data[1]
        mean_rainfalls.append(mean_rainfall)

    # combine the monthly rainfall data and mean montly rainfall data, calculate the anomaly
    for i in range(len(year_and_rainfall)):
        month = (i+1) % 12
        mean_rainfall = float(mean_rainfalls[month-1])
        year_and_rainfall[i].append(mean_rainfall)
        anomaly = round(year_and_rainfall[i][1] / year_and_rainfall[i][2] * 100 , 2)
        year_and_rainfall[i].append(anomaly)

    # store the content into files
    file_name = str(station_ID) + "_" + location_name.split()[0].lower().replace("/", "-") + ".csv"
    file_path = individual_station_data_path + "/" + file_name

    f = open(file_path, "w")
    f.write("ID,Location Name,Latitude,Longitude,Date,Rainfall (mm),Avg Rainfall (mm),Rainfall (% anomaly)\n")

    ID = 1
    for data in year_and_rainfall:
        new_row = str(ID) + "," + location_name + "," + latitude + "," + longtitude + \
                  "," + data[0] + "," + str(data[1]) + "," + str(data[2]) + "," + str(data[3]) + "\n"
        f.write(new_row)
        ID +=1

        new_row_all = str(ID_all) + "," + location_name + "," + latitude + "," + longtitude + \
                  "," + data[0] + "," + str(data[1]) + "," + str(data[2]) + "," + str(data[3]) + "\n"
        all_data_file.write(new_row_all)
        ID_all +=1

    f.close()
    station_ID += 1

all_data_file.close()