# Task

Given the csv file `IOWC-Projects/icoads_grouping/grid_ICOADS_R3.0_Rqst747821_17950101-18360101.csv`, we expand the dataset with comments in IMMA1 files from [NCAR](https://rda.ucar.edu/datasets/ds548.0/dataaccess/#).

The `grid_ICOADS_R3.0_Rqst747821_17950101-18360101.csv` records (rows) have unique IDs that correspond to IDs in the IMMA1 files. IMMA1 files are however not formatted in a csv-friendly way. This task extracts the texts that comment qualitatively on weather in the IMMA1 files. The texts roughly correspond to 9 specific positions in a line; therefore we extract the information in those 9 positions in each line. Some comment examples are "CLOUDY", "GOED WEER", "SMALL RAIN", "HAZY", "MODERATE BREEZES", "DIKKE EN TEEGENS DEN ANDER SCHOORENDE LUCHT", "CIELO ACHUBASCADO Y LLOVIENDO".

We are interested in the number of accounts that mention rain in any language. For each target zone (see `IOWC-Projects/icoads_grouping` for explanation), on a given date, we calculate the percentage of accounts in that zone on that date that mention rain (we call this rainfall percentage). We also calculate the mean air temperature (AT) and sea-level pressure (SLP) of the zone on the date.

We further aggregate the daily statistics into monthly and yearly statistics for graphing.

# Preparation and Environment

1. Go to [NCAR](https://rda.ucar.edu/datasets/ds548.0/dataaccess/#) and download the dataset and years you are working with. 
   
    <img width="1000" alt="site1" src="https://github.com/siennahsu/IOWC-Projects/assets/104809870/d5023dc0-0b48-4427-8c69-cb46e7a16627">
  
    <img width="1000" alt="site2" src="https://github.com/siennahsu/IOWC-Projects/assets/104809870/77f77725-e27b-4a21-8846-efc70dc4b36a">


2. I used my local machine to run this. It took a while to run so I would suggest running it locally instead of in a volatile environment (like Google Colab).

# Code customization

1. Change the paths in the code according to your file organization.

2. Before you run the main code (the sections "Load the dataframe" and "Write data into the dataframe"), use the "Verification Script" first to confirm the format of the IMMA1 files. There are several helper functions in this section, each provides a different verification method. Read the code's comments for more information. If the format of your IMMA1 files is different from the ones I used, you need to figure out the indices of comments in each line (with help from the helper functions), then you need to modify the start_index of each comment in the main code block under "Write data into the dataframe".

     ```
     # comment 1
     comment1 = ""
     start_index = your_start_index
     ```  

# Runtime and Results

Several csv files and plots are generated and saved. The files are:

1. `ship_data_zone_comments.csv`: The original `grid_ICOADS_R3.0_Rqst747821_17950101-18360101.csv` file augmented with the column "comments".
2. `clean_ship_data_zone_comments.csv`: The same file as #1 but any data point outside of target zones 1, 2, 3.1, 3.2, and 4 are dropped.
3. `zone{i}_ICOADS_comments.csv`: Zone-specific files extracted from #2.
4. `zone{i}_daily_rain_percentage.csv`: Daily rainfall percentage of the zone.
5. `zone{i}_monthly_rain_percentage.csv`: Monthly rainfall percentage of the zone.
6. `zone{i}_monthly_data.csv`: Monthly rainfall percentage, average AT, and average SLP of the zone.
7. `zone{i}_annual_data.csv`: Yearly rainfall percentage, average AT, and average SLP of the zone.
8. `zone{i}_{stat}.jpg`: A plot of zone i with specified stat.

For all files, i ∈ {1, 2, 3.1, 3.2, 4} and stat ∈ {"rainfall_percentage", "avg_at", "avg_slp"}.

Some other information may be mistakenly extracted as they are at the positions where there are usually comments, but as long as the real comments are also extracted, it is okay.
