# Reading
- [Using the Jupyter Notebook Environment](https://developers.arcgis.com/python/guide/using-the-jupyter-notebook-environment/)
- [Chapter 5 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12)
- [Chapter 6 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12)

# Previous Semester Recordings
## Fall 2020 Recording
[Zoom recording](https://slu.zoom.us/rec/share/iv0CionXr7sL9J3ShF9tz_XBc5_1HsZfyK4wTB48GoB7YAy5bE4-69Ya9OdFLJfI.kmSyusDlS3A5fzrE?startTime=1599080306000)

# Lecture
We will begin by setting up our Jupyter Notebook using ArcGIS Pro. Then, we will work with our local jupyter notebook to understand geoprocessing with Python following from Chapter 5 of Python Scripting for ArcGIS Pro and also how to explore data following from Chapter 6 of Python Scripting for ArcGIS Pro.

# Data
- af_dem_30s.tif (and other DEMs)
- Features.gdb
- OSM.gdb
- Monthly_Pre-Existing_Condition_Insurance_Plan_Enrollment__State_by_State.csv
- coordinates.txt

# Lecture Notebooks
- unit_3_lesson_1_exploring_spatial_data.ipynb
- unit_3_lesson_2_environments_and_coordinates_systems.ipynb
- unit_3_lesson_3_text_files_and_csvs.ipynb
- [unit_3_lesson_1_environments_and_coordinates_systems.ipynb](https://github.com/gbrunner/intro-prog-for-gis-rs/blob/master/Week%203/unit_3_lesson_1_environments_and_coordinates_systems.ipynb)
- [unit_3_lesson_1_exploring_spatial_data.ipynb](https://github.com/gbrunner/intro-prog-for-gis-rs/blob/master/Week%203/unit_3_lesson_1_exploring_spatial_data.ipynb)


# Unit 3 Exercise and Discussion Questions 
## Exercises
- Please complete [Python Scripting for ArcGIS Pro Exercise 05](https://learngis.maps.arcgis.com/home/item.html?id=d3618832b89844dda4c0b97c44ccf151). You can download the data from [here](https://learngis.maps.arcgis.com/home/item.html?id=a944af0becbf47df98336a9e4881a6b8). Please submit the scripts that you create through the exercise. If you are doing the exercise in a Jupyter Notebook, feel free to submit the notebook instead of the script.
- Please complete [Python Scripting for ArcGIS Pro Exercise 06](https://learngis.maps.arcgis.com/home/item.html?id=cef0aa5df9c54993a6c1cb1dfec5f553). You can download the data from [here](https://learngis.maps.arcgis.com/home/item.html?id=3df07f29a0844d62af4338c52a40fda9). If you are doing the exercise in a Jupyter Notebook, feel free to submit the notebook instead of the script.

## Discussion Questions:
1. What are some typical environment variables that get set in a script?
2. What is the difference between required and optional parameters of geoprocessing tools and how can this impact writing a script?
3. In the [```numpy.zeros```](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html) function, what are the required paratmers and what are the optional parameters?

# Homework Problems
1. Using the OSM.gdb as input, write a script that reads all the feature classes in a workspace and prints the name of each feature class and the geometry type of that feature class in the following format, for example: *roads is a polyline feature class*
2. Uding the OSM.gdb as input, write a script that reads all the feature classes in a personal or file geodatabase and copies only the polygon feature classes to a new file geodatabase. You can assume there are no feature datasets in the exist-ing data, and the feature classes can keep the same name.
 
# Challenge (if the homework is too easy!)
- **freq.py** - Write a Python script to solve the following problem. The input data can be found in **ch06.zip**. The land cover types in 'park.shp' include 'woods', 'orchards', and 'other.' Park rangers would like a table including the frequencies of polygons with each cover type. Write a script to perform Frequency (Analysis) on the 'COVER' field that will generate this table. Name the output 'COVER_freq.dbf'.




