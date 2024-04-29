# Task

Given the csv file `ICOADS_R3.0_Rqst705541_18150101.csv`, expand the dataset with comments in IMMA1 files from this site: https://rda.ucar.edu/datasets/ds548.0/dataaccess/#.

The `ICOADS_R3.0_Rqst705541_18150101.csv` records (rows) have unique IDs that correspond to IDs in the IMMA1 files. IMMA1 files are however not formatted in a csv-friendly way. This task extracts the texts that comment qualitatively on weather in the IMMA1 files. The texts roughly correspond to 9 specific positions in a line; therefore we extract the information in those 9 positions in each line. Some comment examples are "CLOUDY", "GOED WEER".

# Preparation and Environment

1. Go to https://rda.ucar.edu/datasets/ds548.0/dataaccess/# and download the dataset and years you are working with. 
   
    <img width="1000" alt="site1" src="https://github.com/siennahsu/IOWC-Projects/assets/104809870/d5023dc0-0b48-4427-8c69-cb46e7a16627">
  
    <img width="1000" alt="site2" src="https://github.com/siennahsu/IOWC-Projects/assets/104809870/77f77725-e27b-4a21-8846-efc70dc4b36a">


2. I used my local machine to run this. It took a while to run so I would suggest running it locally instead of in a volatile environment (like Google Colab).

# Code customization

1. Change the paths in the code according to your file organization so the program has access to the IMMA1 files you downloaded.

2. Before you run the main code (the sections "Load the dataframe" and "Write data into the dataframe"), use the "Verification Script" first to confirm the format of the IMMA1 files. There are several helper functions in this section, each provides a different verification method. Read the code's comments for more information. If the format of your IMMA1 files is different from the ones I used, you need to figure out the indices of comments in each line (with help from the helper functions), then you need to modify the start_index of each comment in the main code block under "Write data into the dataframe".

     ```
     # comment 1
     comment1 = ""
     start_index = your_start_index
     ```  

# Runtime and Results

The resulting file is `ship_data_with_comments.csv`. Some other information may be mistakenly extracted as they are at the positions where there are usually comments, but as long as the real comments are also extracted, it is okay.
