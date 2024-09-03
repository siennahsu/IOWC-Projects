# Task

Obtain the rain gauge data from [Global Historical Climatology Network - Monthly (GHCN-M) v2](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00835) accessed through the [IOWC Historical Climate Site](https://github.com/coconutcastle/historical-climate-data). Organize the data into seasonal data (Nov-Feb and Jun-Aug) and calculate anomalies.

The IOWC Historical Climate Site can be accessed [here](https://iowc.geog.mcgill.ca/). If you wish to access the site offline, see instructions on downloading relevant data and software at `iowc_offiline_guide.pdf`.

# Preparation and Environment

1. There are no specific requirements to run the script.

2. To access the data from the IOWC Historical Climate Site, make sure to check the boxes "Station Metadata" at Data Types and "Insert metadata" at Insert Station Metadata. This way, each row of data will have coordinates.
   <img width="894" alt="Screen Shot 2024-08-14 at 12 28 45 PM" src="https://github.com/user-attachments/assets/f048d0ab-f92f-4216-bdd1-cd0c89a598ae">
   <img width="893" alt="Screen Shot 2024-08-14 at 12 28 56 PM" src="https://github.com/user-attachments/assets/07996584-1db1-4916-83a8-3c565cb0603f">

3. Two example csv files downloaded from the IOWC Historical Climate Site and used in the script are included in the current directory. You can check out the format.

# Code Customization

Change the file path according to your file organization.

# Runtime and Results

The outputs are two csv files that contain seasonal precipitation readings, seasonal means, and anomalies. One csv file is for the season Nov-Feb; the other one is for the season Jun-Aug.


