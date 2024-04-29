Task: Collect the rainfall data from https://climexp.knmi.nl/selectstation.cgi?id=someone@somewhere with specified parameters through web scraping.

Instructions:

1. After you finish selecting the parameters, click the button "Get stations" and you will be led to a new webpage. Download this webpage entirely in html. I have attached a sample called "sample_rainfall_data.html" in the rainfall_data directory. The reason I did this instead of just using the link is that using the link messed up the html format somehow.

2. I recommend using Colab (so use the Cloud). I tried running this script on my local machine and it kept crashing because of intensive     http connection requests (I was using MacOS 12.5 with M2 chip). Colab environment had no problem running it.

3. For each station listed in the sample_rainfall_data, I was asked to extract two raw data (from two new nested links). If you are asked to do something different, you will have to modify the scraper script yourself. 

4. To use the script, upload the rainfall data html file onto Colab's environment. Make sure you change the path correspondingly at lines
   
```
# read the html file of the search results
with open(your_path_to_the_html_file) as fp:
    all_stations_soup = BeautifulSoup(fp, 'html.parser')
```

5. If you are asked to calculate rainfall anomaly, you can uncomment the line that calculates it and comment out the next line. 

```
anomaly = round(year_and_rainfall[i][1] / year_and_rainfall[i][2] * 100 , 2)
# anomaly = 0
```

   Otherwise, it is defaulted to 0. There might be some numerical issues you'll have to fix. It sometimes appeared, and sometimes didn't. It seems to be depending on different stations since some stations have messed-up formats.

6. The notebook has two sections: "Regular scraper script" and "Scraper script for large scale scraping". The large scale scraper script has a try-except block that disregards stations with incompatible formats. If that is what you desire, use this instead of the regular scraper script. I recommend using the large scale one.

7. It is normal that it could take hours to finish running the script.
    
8. The resulting files are:
   
   8.1. A csv file for each station. This was designed as a checkpoint. If your program crashes, you can start with the stations you haven't scraped.
   
   8.2. An all_stations_data_csv. This is the csv that has all the data and the one you should hand in. See all_stations_data.csv in this directory as an example.
