# Reading
- [Using the Jupyter Notebook Environment](https://developers.arcgis.com/python/guide/using-the-jupyter-notebook-environment/)
- [Chapter 5 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12)
- [Chapter 6 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12)


# Lecture
We will begin by setting up our Jupyter Notebook using ArcGIS Pro. Then, we will work with our local jupyter notebook to understand geoprocessing with Python following from Chapter 5 of Python Scripting for ArcGIS Pro and also how to explore data following from Chapter 6 of Python Scripting for ArcGIS Pro.

# Data
- af_dem_30s.tif (and other DEMs)
- Features.gdb
- OSM.gdb
- Monthly_Pre-Existing_Condition_Insurance_Plan_Enrollment__State_by_State.csv
- coordinates.txt


# Lecture Notebooks
- Getting setup with Jupyter for ArcGIS Pro.
- I need a notebook that follows chapter 5.
- [unit_3_lesson_1_exploring_spatial_data.ipynb](https://github.com/gbrunner/intro-prog-for-gis-rs/blob/master/Week%203/unit_3_lesson_1_exploring_spatial_data.ipynb)

# In-Class Exercises
- Please complete [Python Scripting for ArcGIS Pro Exercise 05](https://learngis.maps.arcgis.com/home/item.html?id=d3618832b89844dda4c0b97c44ccf151). You can download the data from [here](https://learngis.maps.arcgis.com/home/item.html?id=a944af0becbf47df98336a9e4881a6b8). Please submit the scripts that you create through the exercise. If you are doing the exercise in a Jupyter Notebook, feel free to submit the notebook instead of the script.
- Please complete [Python Scripting for ArcGIS Pro Exercise 06](https://learngis.maps.arcgis.com/home/item.html?id=cef0aa5df9c54993a6c1cb1dfec5f553). You can download the data from [here](https://learngis.maps.arcgis.com/home/item.html?id=3df07f29a0844d62af4338c52a40fda9). If you are doing the exercise in a Jupyter Notebook, feel free to submit the notebook instead of the script.

# Homework Questions:
1. What are some typical environment variables that get set in a script?
2. What is the difference between required and optional parameters of geoprocessing tools and how can this impact writing a script?
3. In the [```numpy.zeros```](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html) function, what are the required paratmers and what are the optional parameters?

# Homework Problems
- Please complete any 3 of the 4 **Challenge** exercises on pages 22 and 23 and submit your answers as individual Python (.py) scripts.
 
# Challenge (if the homework is too easy!)
- **freq.py** - Write a Python script to solve the following problem. The input data can be found in **ch06.zip**. The land cover types in 'park.shp' include 'woods', 'orchards', and 'other.' Park rangers would like a table including the frequencies of polygons with each cover type. Write a script to perform Frequency (Analysis) on the 'COVER' field that will generate this table. Name the output 'COVER_freq.dbf'.




