# IOWC-Projects

This is the code archive of the [Indian Ocean World Centre at McGill University](https://indianoceanworldcentre.com/) for the years 2023-2024. Please contact Sienna Hsu (shih-ching.hsu@mail.mcgill.ca) if you have questions about the code. The projects included are as follows:

  - `rainfall_data`: Collection of rain gauge data from the [KNMI Climate Explorer](https://climexp.knmi.nl/start.cgi?id=someone@somewhere).
  - `rainfall_selection`: Calculation of yearly and seasonal statistics of the rain gauge data collected from the KNMI Climate Explorer.
  - `phyda`: Collection, statistics calculation, and graphing of PDSI, SPEI, and ENSO data from the [Paleo Hydrodynamics Data Assimilation product (PHYDA)](https://zenodo.org/records/1198817).
  - `ocr_pdf`: Widgets for PDF file processing, OCR, and image processing.
  - `lmr`: Extraction and calculation of mean precipitation rates based on [Last Millennium Reanalysis (LMR) Project Global Climate Reconstructions Version 2](https://www.ncei.noaa.gov/access/paleo-search/study/27850).
  - `tree_ring`: Exploratory data analysis and visualization of tree ring data from [NOAA Paleo Data Search](https://www.ncei.noaa.gov/access/paleo-search/?dataTypeId=18).
  - `icoads_grouping`: Adding climate zone information to the ship log data from [ICOADS](https://icoads.noaa.gov/products.html). The climate zoning scheme developed here is used in `icoads_analysis` and `reanalysis`. 
  - `icoads_analysis`: Collection of data from the [NCAR Research Data Archive](https://rda.ucar.edu/) to expand the ship log data mentioned above. Statistical analysis and visualization of data.
  - `reanalysis`: Collection of precipitation rate data from the [NOAA-CIRES-DOE Twentieth Century Reanalysis (20CR) project](https://psl.noaa.gov/data/20thC_Rean/). Statistical analysis and visualization of data. Comparison to ICOADS data.
  - `ghcnm`: Collection and analysis of rain gauge data from [Global Historical Climatology Network - Monthly (GHCN-M) v2](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00835).

## Resources
1. For instructions on how to use the offline [IOWC Historical Climate Site](https://github.com/coconutcastle/historical-climate-data), see `ghcnm/iowc_offiline_guide.pdf`.
2. For a quick start on NetCDF, see this [tutorial](https://towardsdatascience.com/read-netcdf-data-with-python-901f7ff61648) by Konrad Hafen.
3. Most of the scripts here use Pandas and Numpy. This [official tutorial](https://pandas.pydata.org/docs/user_guide/10min.html) by Pandas should be enough.
4. If you need a refresher on Matplotlib, check out their [quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start).
5. ChatGPT is your good friend.
