# Task 

This task extracts the PDSI, SPEI, and ENSO indices of years 1630-1690 from the netCDF files at https://zenodo.org/records/1198817. We further use these data to produce the following graphs:

  - Raw PDSI and SPEI time series graphs for specified locations from 1630 to 1690, using Jun-Aug and Dec-Feb datasets.
  - Year-on-year and season-on-season differences of PDSI and SPEI time series graphs for specified locations from 1630 to 1690, using Jun-Aug and Dec-Feb datasets.
  - Annual ENSO index time series, globally, 1630 to 1690, using the Apr-Mar dataset.

# Preparation and Environment

1. Go to https://zenodo.org/records/1198817 and download the datasets you need.

    <img width="1213" alt="source" src="https://github.com/siennahsu/IOWC-Projects/assets/104809870/7772ca4f-9de4-4c33-8d6c-b6f6e554392b">


2. Here I describe the uses of each script:

     - `pdsi-spei-jun-to-aug.ipynb`: This script extracts PDSI and SPEI information from the Jun-Aug netCDF dataset. 
     - `pdsi-spei-dec-to-feb.ipynb`: This script extracts PDSI and SPEI information from the Dec-Feb netCDF dataset. 
     - `pdsi-spei-graphs.ipynb`: This script calculates the year-on-year and season-on-season differences and graphs all the PDSI and SPEI graphs.
     - `enso-data.ipynb`: This script extracts ENSO information from the Apr-Mar dataset (it can also work with the Jun-Aug and Dec-Feb datasets). It graphs any graphs regarding ENSO.

3. Except for `pdsi-spei-graphs.ipynb`, you need to install the following package to run the code:

    ```
    pip install netcdf4
    ```
        
4. I recommend using your local machine to run as some scripts run for a long time and need persistent storage (so don't use Colab).

# Code customization

1. Change the file paths in the code according to your file organization.

2. If you are asked to extract information from different regions (specified in coordinates) or years, change the following global variables in the `pdsi-spei-jun-to-aug.ipynb` and `pdsi-spei-dec-to-feb.ipynb` scripts:
   
    ```
    MIN_YEAR = 1630
    MAX_YEAR = 1690
    MIN_LAT = -40
    MAX_LAT = 50
    MIN_LON = 13
    MAX_LON = 155
    ```
      As ENSO is a global index, no coordinates are specified in the `enso-data.ipynb` script.

3. Feel free to change any graph attributes––font size, title, colors, etc.

4. If you are asked to extract indices other than PDSI, SPEI, or ENSO, the code here should be able to be reused. Just change the variables accordingly.

5. **IMPORTANT.** In the `pdsi-spei-graphs.ipynb` code, you can graph graphs for specific coordinates. You need to add the tuple `(latitude, longitude, location_name)` into the variable `targets` in the second code block. You can separate the locations into different groups (like Asia, Africa, etc.) under the section "Grouping". However, **the code will not work if a location appears in more than one group**. So if you already have a group that includes a location you want to graph for another group, comment out the former group first. Here is an example:

    ```python
    # The original groups that existed before I would like to put some countries into focus groups.
    # I commented out these 3 groups so I could include those countries in the focus groups.
    """
    # Africa
    group1 = ["Cape Town, South Africa", "Taolagnaro, Madagascar", "Maputo, Mozambique", "Mombasa, Kenya", 
              "Gondar, Ethiopia"]
    
    # South Asia and the Middle East
    group2 = ["Muscat, Oman", "Bandar Abbas, Iran", "Surat, India", "Delhi, India", "Chennai, \
              India", "Kolkata, India"]
    
    # Southeast and East Asia
    group3 = ["Bago, Myanmar", "Rakhine, Myanmar", "Jakarta, Indonesia", "Beijing, China", \
              "Mataram City, Indonesia", "Ambon, Indonesia"]
    """

    # Dummy code on the existing groups. We basically make group1, group2, group3 into empty groups.
    group1 = []
    group2 = []
    group3 = []

    # spei_jja_focus_group
    group4 = ["Surat, India", "Cape Town, South Africa", "Ambon, Indonesia", "Beijing, China", \
                           "Bandar Abbas, Iran", "Kolkata (Calcutta), India", "Delhi, India"]
    
    # spei_djf_focus_group
    group5 = ["Jakarta (Batavia), Indonesia", "Rakhine (Arakan), Myanmar", "Bago (Pegu), Myanmar", \
                           "Chennai (Madras), India", "Jaffna, Sri Lanka"]
    ```
    Why is the code like this? Because I was not asked to graph the focus groups when I first wrote the code, and the groups I was working with were all mutually exclusive.
    
# Runtime and Results

1. The `pdsi-spei-jun-to-aug.ipynb` and `pdsi-spei-dec-to-feb.ipynb` each ran for around 2 days, so be sure to allocate enough time. The extracted SPEI and PDSI files are attached in this directory, named `jun_to_aug.csv` and `dec_to_feb.csv` respectively. If you are only going to work with SPEI and PDSI, you can reuse these two csv files.

2. The graphs graphed in the `pdsi-spei-graphs.ipynb` and `enso-data.ipynb` are not automatically saved. You will need to manually download the graphs.

3. The `enso-data.ipynb` does not export the dataframe of ENSO data into a csv. If you need that, you can easily add the code to do it.
