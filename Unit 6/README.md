# Video
[AWS re:Invent 2017: How Esri Optimizes Massive Image Archives for Analytics in the Cloud](https://www.youtube.com/watch?reload=9&v=U486YxlDoeM)

# Previous Year's Lecture Recordings
## [Fall 2020](https://slu.zoom.us/rec/play/sQpqa49bkamXCndF8fFowQLA-Q0dfTDnt5V4_crPJ_BQAohd8r8QRiARAteB6-_vCAg7HK7zS-9eb3gw.U7IL4813ozLnb-hc?startTime=1600894614000&_x_zm_rtaid=zm-zJ_rzSxmT4kO2ip8ayQ.1607655790439.f38412494adf72fbc4a7b032e2af6420&_x_zm_rhtaid=779)

# Reading
[Chapter 10 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=0)

# Lecture
Slides on rasters followed by three Notebooks, in this order:
1. unit_6_lesson_1_working_with_rasters_arcpy.ipynb
2. unit_6_lesson_2_working_with_rasters_numpy.ipynb
3. unit_6_lesson_3_working_with_rasters_in_the_cloud.ipynb

# Data
- DEMS.zip from previous weeks
- Check data in Azure and AWS before lecture

# In Class Exercise
- Please complete [Exercise 10 from Python Scripting for ArcGIS Pro](https://www.arcgis.com/home/item.html?id=1372abc4fb0c4ff0a7c66e8d9c869038). The data can be found [here on ArcGIS Online](https://www.arcgis.com/home/item.html?id=862c63f5a50e4a29bb237369a9854838).

# Final Project Proposal
Pitch your final prroject on the Blackboard Discussion.
Read and comment on two other students proposals.
Due in 2 weeks.

# Unit 6 Exercise and Discussion Questions 
## In class exercise
Compete exercises for Chapter 10 of Python Scripting for ArcGIS Pro
Exercise: https://www.arcgis.com/home/item.html?id=1372abc4fb0c4ff0a7c66e8d9c869038
Data: https://www.arcgis.com/home/item.html?id=862c63f5a50e4a29bb237369a9854838

## Questions
1. What is a "Raster" object, and why do geoprocessing operations and map algebra expressions using rasters often result in temporary outputs?
2. What are the differences between raster datasets and raster bands?
3. What is the difference between raster functions in ArcGIS Pro and their equivalent functions in arcpy.sa or arcpy.ia?

# Unit 6 Assignment 
## Challenge 1
Create a script that determines what areas meet the following conditions:
- Moderate slope: between 5 and 20 degrees
- Southerly aspect: between 150 and 270 degrees
- Forested: land cover types of 41, 42, or 43
Be sure to use the map algebra expressions of the ```arcpy.sa``` module.

## Challenge 2
Write a script that copies all the rasters in a workspace to a new file geo-database. You can use the rasters in the **Exercise09** folder as an example. If you do Challenge 2, you may get an error:

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx#RasterToGeodatabase_conversion.InitializeParameters.py in <module>

AttributeError: 'ToolValidator' object has no attribute 'isLicensed'

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx#RasterToGeodatabase_conversion.InitializeParameters.py in <module>

AttributeError: 'ToolValidator' object has no attribute 'isLicensed'


**If you get this error, check to see whether the tool worked anyway!**
