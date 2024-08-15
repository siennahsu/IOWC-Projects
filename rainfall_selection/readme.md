# Task 

We first define seasons and a year as follows:
  
  - Winter: Dec of the previous year - Feb
  - Spring: Mar - May
  - Summer: Jun - Aug
  - Autumn: Sept - Nov
  - Year: Sept to Aug of the next year.

For a given threshold (which is set to 100 in the code), we define the following:

  - A dry season is where the total average rainfall of that season is less than the threshold.
  - A rainy season is where the total average rainfall of that season is more than or equal to the threshold.
  - For example, if location A's (Dec avg rainfall + Jan avg rainfall + Feb avg rainfall) < threshold, then location A's winter is considered a dry season.

For this task, we do the following: 

1. Using the resulting `all_stations_data.csv` file from the task listed in `/IOWC-Projeccts/rainfall_data`, extract seasonal and annual rainfall and their averages.

2. Additionally, we produce a csv file of only the dry seasons of each location and a csv file of only the rainy seasons.

3. For seasonal data, a rainfall anomaly of the season is calculated.

# Preparation and Environment

1. Be sure to have the `all_stations_data.csv` generated in `IOWC-Projects/rainfall_data/` for the `rainfall_selection.ipynb` script.

2. This script runs pretty fast so using your machine is fine.

# Code Customization

1. If you wish to set a different threshold, remember to change it accordingly in the second code block of the notebook.

2. Remember to change the paths of all files used and produced according to your file organization.

# Runtime and Results

1. The notebook contains two sections: "Seasonal Rainfall" and "Annual Rainfall". Run whichever you need, which should be straightforward.

2. The possible resulting files are:
   
   - `rainfall_seasonal.csv` that contains all the seasonal data.
   - `rainfall_seasonal_dry.csv` that contains all the dry seasons' data.
   - `rainfall_seasonal_rainy.csv` that contains all the rainy seasons' data.
   - `rainfall_annual.csv` that contains the annual rainfall data.
