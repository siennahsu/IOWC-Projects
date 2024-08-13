# Task

With data from [ICOADS](https://icoads.noaa.gov/products.html), we have compiled a csv file called `ICOADS_R3.0_Rqst747821_17950101-18360101.csv`. Every row of data (a data point) has a coordinate. We assign each data point to its corresponding grid group. Grid groups are coordinates in whole numbers. A data point with coordinate `(x, y)` is assigned to the grid group `(floor(x), floor(y))`. Then we assign the grid groups into different climate zones mostly based on the climate zoning of [IPCC](https://interactive-atlas.ipcc.ch/regional-information#eyJ0eXBlIjoiQVRMQVMiLCJjb21tb25zIjp7ImxhdCI6OTc3MiwibG5nIjo0MDA2OTIsInpvb20iOjQsInByb2oiOiJFUFNHOjU0MDMwIiwibW9kZSI6ImNvbXBsZXRlX2F0bGFzIn0sInByaW1hcnkiOnsic2NlbmFyaW8iOiJzc3A1ODUiLCJwZXJpb2QiOiIyIiwic2Vhc29uIjoieWVhciIsImRhdGFzZXQiOiJDTUlQNiIsInZhcmlhYmxlIjoidGFzIiwidmFsdWVUeXBlIjoiQU5PTUFMWSIsImhhdGNoaW5nIjoiU0lNUExFIiwicmVnaW9uU2V0IjoiYXI2IiwiYmFzZWxpbmUiOiJwcmVJbmR1c3RyaWFsIiwicmVnaW9uc1NlbGVjdGVkIjpbXX0sInBsb3QiOnsiYWN0aXZlVGFiIjoicGx1bWUiLCJtYXNrIjoibm9uZSIsInNjYXR0ZXJZTWFnIjpudWxsLCJzY2F0dGVyWVZhciI6bnVsbCwic2hvd2luZyI6ZmFsc2V9fQ==). 

The resulting climate zones 1, 2, 3, and 4 correspond to the yellow lines below. Each dot on the map is a data point from the csv file. Note that any area outside of the four climate zones is designated as climate zone -1. 

<img width="810" alt="Screen Shot 2024-08-13 at 12 50 28 PM" src="https://github.com/user-attachments/assets/7a0310c2-721f-4d9c-be1e-dd33f2937734">

For each grid group, we define the density of the grid group as the number of data points in the group. For each climate zone, we set different thresholds (after some EDA and manual inspection) to categorize a grid group into "high density" or "low density." For climate zone 3, we additionally have the tag "median density." For climate zones 1, 2, and 4, we further qualify high-density grid groups into target zones. For climate zone 3, we qualify the high-density grid groups and median-density grid groups into target zones 3.1 and 3.2 respectively. This results in the graph below (purple is high-density, green is median, and red is low):

![ICOADS Regions Density](https://github.com/user-attachments/assets/f099d357-5a00-4e4a-80fc-c9aa7ffa252c)

The zoning data is important for the next task, which is detailed in the directory `IOWC-Projects/icoads_analysis`. The same zoning scheme is also used in `IOWC-Projects/reanalysis`.

# Preparation and Environment

Nothing specific is required to run this script.

# Code Customization

There is a section called "Deciding threshold" and a section called "EDA." If for any reason, you'd like to change the thresholds of high/median/low densities for a climate zone, you can play around these two sections.

# Runtime and Results

There are quite a few resulting csv files based on the OG csv file `ICOADS_R3.0_Rqst747821_17950101-18360101.csv`:

1. `grid_ICOADS_R3.0_Rqst747821_17950101-18360101.csv`: The ultimate csv file that we will be using for the next task. For each line of data, we have added the information "grid_group," "climate_zone," and "target_zone."
2. `grid_thres_ICOADS_R3.0_Rqst747821_17950101-18360101.csv`: For each line of data, we have added "grid_group," "climate_zone," and "density." 
3. `grid_clean_ICOADS_R3.0_Rqst747821_17950101-18360101.csv`: The same file as #1 but the rows whose coordinate is not in any target zones are dropped. It has a smaller size and could be easier to work with.
4. `zone{i}_ICOADS.csv` where i ∈ {1, 2, 3.1, 3.2, 4}: These five files are obtained from file #3 to be zone-specific. It has the same columns as #1 and #3. 
5. `grid_count.csv`: Information about grid groups. The columns are "lon," "lat," "count," and "climate_zone". It was used for some EDA.
6. `grid_thres.csv`: The same file as #5 with an additional column "density". It was used to graph the second map above.
7. `grid_thres_clean.csv`: The same file as #6 but the grid groups outside of the four climate zones are dropped.
8. `grid_target.csv`: Information about grid groups in the target zones. The columns are "target_zone,"	"longitude," and "latitude." It was used for mapping in QGIS.
