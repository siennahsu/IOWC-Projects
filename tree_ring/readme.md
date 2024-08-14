# Task 

Here I do exploratory data analysis and visualization of tree ring data in China and Southeast Asia. The links to the China data are in the file `paleo_records.csv`. For Southeast Asia, the data wanted are listed in Table 1 of [this paper](https://www.researchgate.net/publication/266885910_Status_of_tree-ring_research_from_teak_Tectona_grandis_for_climate_studies). To obtain the links to those data, search with the keywords in the [NOAA Paleo Data Search](https://www.ncei.noaa.gov/access/paleo-search/?dataTypeId=18) database.

I explore both the raw measurements of tree growth and the Transformed Ring-Width Standardized Growth Index (TRSGI) here. I also group some sites and analyze the data group-wise.

# Preparation and Environment

This script scrapes some data from the NOAA site. I recommend using Colab because my local machine sometimes has problems with HTTP requests.

# Code Customization

1. As you might know, a lot of NOAA data are in .txt format and are not csv-friendly. In the script, some code clocks require a text file as input for graphing where the irrelevant lines are already deleted (like those that start with #). For other blocks, all you need to input is the link to the text files. Change the file paths in the code according to your file organization.
2. It should be straightforward to set the time ranges of the graphs once you see the code.

# Runtime and Results

The code transforms the NOAA text files into csv files, which you can save if you wish. The main thing is to produce graphs to better understand trends.


