# Task
Collect the monthly precipitation rate (prate) data from the [NOAA-CIRES-DOE Twentieth Century Reanalysis (20CR) project](https://psl.noaa.gov/data/20thC_Rean/). Convert the prate unit into mm/day, convert the monthly mean prate into annual mean prate with a year defined as June to May, calculate the average annual prate over 1806-2015, and at last, calculate the anomaly with formula (annual prate / average annual prate * 100). 

Each data point has a coordinate in whole numbers. This corresponds to the grid groups in `IOWC-Projects/icoads_grouping` and can be categorized into target climate zones (see `IOWC-Projects/icoads_grouping` for explanation). For each zone, we calculate the annual prate averaged over the zone and graph the time-series data.

Lastly, we compare the zone annual prate to the zone rainfall percentage calculated in `IOWC-Projects/icoads_analysis`. We graph the respective time-series values and calculate the correlation.

# Preparation and Environment

1. Go to the [NOAA Physical Sciences Laboratory](https://downloads.psl.noaa.gov/Datasets/20thC_ReanV3/Monthlies/sfcSI-MO/) and download the file `prate.mon.mean.nc`.

2. I recommend using your local machine as the script takes some time to run and needs persistent storage (so don't use Colab).
   
3. You will need to install the netCDF library:
    ```
    pip install netcdf4
    ```
4. The comparison section of the code requires `zone{i}_annual_data.csv` generated in `IOWC-Projects/icoads_analysis` to run.

# Code Customization
1. Change the file path according to your file organization.
2. You can specify the date range and region range:
    ```
    MIN_YEAR = 1806
    MAX_YEAR = 2015
    
    MIN_LAT = -60
    MAX_LAT = 30
    MIN_LON = 13
    MAX_LON = 120
    ```
# Runtime and Results
While running, the script will first collect data year-by-year to act as checkpoints. These data will then be compiled into a big csv file named `rean_v3_prate_wide_1806_2015.csv` in the script. You can safely delete the year-specific data afterward. The csv file is then used to generate annual data, named `rean_v3_prate_wide_annual_1806_2015.csv` in the script. All time-series and comparison plots generated are saved to specified directories.
