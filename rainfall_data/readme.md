# Task

Given a specified range of areas (typically in coordinates) and a given range of years, collect the rainfall data from https://climexp.knmi.nl/selectstation.cgi?id=someone@somewhere through web scraping. The two metrics to collect are:

   - For a location, obtain its monthly rainfall during the specified years.
   - For a location, obtain its average monthly rainfall (calculated throughout history).

# Preparation and Environment

1. Figure out what years and locations you need. Go to the site linked above.

2. After you finish selecting the parameters, click the button "Get stations" and you will be led to a new webpage. Download this webpage entirely in html. I have attached a sample called "sample_rainfall_data.html" in the rainfall_data directory. The reason I did this instead of just using the link is that using the link messed up the html format somehow. Below is an example of parameters:

   <img width="850" alt="parameters" src="https://github.com/siennahsu/IOWC-Projects/assets/104809870/9b621b49-d68f-4d06-9e49-9ef7bba718fb">

3. I recommend using Colab (so use the Cloud). I tried running this script on my local machine and it kept crashing because of intensive     http connection requests (I was using MacOS 12.5 with M2 chip). Colab environment had no problem running it.

# Code customization

1. Set the START_YEAR and END_YEAR global variables according to your task.

2. To use the script, upload the rainfall data html file onto Colab's environment. Make sure you change the path correspondingly at lines
   
   ```
   # read the html file of the search results
   with open(your_path_to_the_html_file) as fp:
       all_stations_soup = BeautifulSoup(fp, 'html.parser')
   ```

3. If you are asked to calculate rainfall anomaly, you can uncomment the line that calculates it and comment out the next line. 

   ```
   anomaly = round(year_and_rainfall[i][1] / year_and_rainfall[i][2] * 100 , 2)
   # anomaly = 0
   ```
      Otherwise, it is defaulted to 0. There might be some numerical issues you'll have to fix. It sometimes appeared, and sometimes didn't. It seems to be depending on different stations since some stations have messed-up formats.

4. For each station listed in the sample_rainfall_data, I was asked to extract the first two raw data (monthly rainfall and average monthly rainfall from two nested links). If you are asked to do something different, you will have to modify the scraper script yourself.


# Runtime and Results

1. The notebook has two sections: "Regular scraper script" and "Scraper script for large scale scraping". The large scale scraper script has a try-except block that disregards stations with incompatible formats. Additionally, it doesn't require that a station has data from every year between START_YEAR and END_YEAR (so for example, a station can have only 2 years of data out of 1885-1900). The regular scraper script is for a more fine-tuned search, which requires that a station has all data out of the specified START_YEAR to END_YEAR (so for example, a station has to have 6 years of data out of 1885-1900). I recommend using the large scale script unless you're searching only a small area within a small timeline.

2. It is normal that it could take hours to finish running the script.
    
3. The resulting files are:
   - A csv file for each station. This was designed as a checkpoint. If your program crashes, you can start with the stations you haven't scraped.
   - An all_stations_data_csv. This is the csv that has all the data and the one you should hand in. See all_stations_data.csv in this directory as an example.
