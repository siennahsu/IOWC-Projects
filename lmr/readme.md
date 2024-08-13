# Task

This task extracts the mean precipitation rate (prate) from the [Last Millennium Reanalysis (LMR) Project Global Climate Reconstructions Version 2](https://www.ncei.noaa.gov/access/paleo-search/study/27850). You can specify the time range and region from which you'd like to extract the prates. The LMR project conducts 20 simulations for each year, so we calculate the mean prate of those 20 simulations for each region and time. 

# Preparation and Environment

1. Go to https://www.ncei.noaa.gov/access/paleo-search/study/27850 and download the v2.0 netCDF files.

2. I recommend using your local machine as the script takes some time to run and needs persistent storage (so don't use Colab).
   
3. You will need to install the netCDF library:
    ```
    pip install netcdf4
    ```
4. Change the file path according to your file organization.

# Code customization

1. Change the file paths in the code according to your file organization.

2. Customize the year and region range:
   ```
   MIN_YEAR = 1880
   MAX_YEAR = 1887
   MIN_LAT = 18
   MAX_LAT = 54
   MIN_LON = 73
   MAX_LON = 135
   ```

# Runtime and Results

1. It took tens of minutes to run on my machine (MacBook Air M2).
2. The output is a QGIS-compatible csv file, where each row has the columns "Date", "Latitude", "Longitude", and "mean_prate".
