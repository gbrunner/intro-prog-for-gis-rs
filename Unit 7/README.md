# [Teaching with ArcGIS Notebooks](https://learn.arcgis.com/en/paths/teach-with-arcgis-notebooks/)

# Project 1 Solutions
- Project 1 Solutions - Spring 2020.html
- Project 1 Solutions - Spring 2020.ipynb

# Unit 6 Homework Solutions
- unit_6_rasters.html
- unit_6_rasters.ipynb
- Unit_6_Discussion_Questions.docx 

# GP Tool Slides
- Python_GP_Tools.ppt

# Demo GP Tool Scripts
- problem1_script.py
- problem2_script.py

# More Imagery - GDAL and Python (THIS DID NOT WORK WELL!)
- unit_7_boto_and_azure.ipynb
- unit_7_gdal.ipynb 

# Unit 7 Exercise and Discussion Questions  (THIS DID NOT WORK WELL!)
This goes with Chapter 3 of Advanced Scripting for ArcGIS Pro

Please complete this tutorial on creating script tools: https://www.arcgis.com/home/item.html?id=cdb970479d5f4439ac5d2eb155bdd6f6

Here is the data: https://www.arcgis.com/home/item.html?id=fbb1335ef10944259899a3af6206e10e

Please complete the following question. Submit screen shots of the results for 1 and 2. Submit the Python script for 3:

1. Create a cloud storage connection to Landsat 8 in Amazon S3 if you haven’t already. [Download the Landsat Descending Path Row shapefile](https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/WRS2_descending_0.zip). Unzip it and view the shapefile in ArcGIS Pro. Identify a path row that covers Northern California. Use that path row to find the imagery over California in the Landsat 8 cloud storage connection. If you are interested in a challenge, find a path row over Northern California from the early September 2020 time frame and try to identify the locations of wildfires in the Landsat 8 imagery.


2. [SpaceNet](https://registry.opendata.aws/spacenet/) is an open geospatial dataset consisting of freely available imagery. [That dataset is used as a test bed for computer vision, machine learning, deep learning, and GeoAI research](https://spacenetchallenge.github.io/datasets/datasetHomePage.html). Create a new ArcGIS Pro project. In that project, create a cloud storage connection to the SpaceNet dataset. You do not need to specify the region when creating the cloud storage connection. Search through the SpaceNet S3 bucket. Add a few images from the SpaceNet S3 bucket to the map. What cities does SpaceNet have imagery for?

3. Make a copy of the random_sample.py script and call it random_percent.py. Modify the script so that the third parameter is a percentage of the number of input records as an integer between 1 and 100. Modify the script tool settings so that the input for this parameter is validated on the tool dialog box
