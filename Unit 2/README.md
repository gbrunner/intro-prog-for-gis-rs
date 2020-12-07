# Reading
Please read Chapters 2 and 3 of [Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12). These two chapters cover Python IDEs and Geoprocessing in ArcGIS Pro. This will set a foundation for much of what we do.

# Previous Semester's Lecture Recordings
## Spring 2020
- Part 1: https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d4e94b2a-8e89-47c0-bd5e-ab4f016ea1f8
- Part 2: https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fc541dcd-68e9-4a2c-8f7a-ab4f017f8ed7
- Part 3: https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=81b0afd2-d392-4713-8f09-ab50000572f1

## Fall 2020
[Zoom recording](https://slu.zoom.us/rec/share/vZeqgmDJhjAFZsTEsRL0hrMzQeVUZ8gn_b7iGgb9XOCqCgrPd8ZLfZOOLoQnBw.76gbPmyVceVzPQT5?startTime=1598475480000)

# Lecture Slides
- Lecture_1_Geoprocessing_and_Python_Window.pptx

# Data and Notebooks
Lecture notebooks can be found in the [GIS 4090\5090 Unit 2 Notebooks](https://slustl.maps.arcgis.com/home/group.html?id=724c1bfb085843debf8f1020b3654045#overview) group.

- unit_2_lesson_1_geoprocessing_in_arcgis_pro.ipynb
- unit_2_lesson_1_geoprocessing_in_arcmap.ipynb
- unit_2_lesson_2_arcpy_in_arcgis_notebooks.ipynb
- unit_2_lesson_2_arcpy_in_arcgis_pro.ipynb
- unit_1_lesson_2_more_python.ipynb
- Missouri.gdb.zip

# Getting Data into ArcGIS Notebooks
[Go through this example to demonstrate how to get data into ArcGIS Notebooks.](https://slustl.maps.arcgis.com/home/group.html?id=8779763b01f84632b83c084b086325de#overview). It uses the Singapore_Data.gdb.zip.

# Unit 1 Discussion Answers
- Unit 1 Discussion Answers.txt

# Unit 1 Assignment Answers
- Unit_1_Assignment_Solutions.py
- Unit_1_Assignment_Solutions.txt
- Unit_1_Assignment_Solutions.ipynb 

# Classwork Exercise
Please complete the following exercises. You do not need to submit anything, but it is recommended that you complete these.
- Please Complete [Python Scripting Exercise 3](https://learngis.maps.arcgis.com/home/item.html?id=3978b52f1e5847c69ef7eaded85780b2). You can find the data [here](https://learngis.maps.arcgis.com/home/item.html?id=d7c05cf515c046c2bedacb2e8e24722c).
- [Beginner's guide to Python in ArcGIS Pro, Part 3: Tutorial](https://www.esri.com/arcgis-blog/products/arcgis-pro/uncategorized/beginners-guide-to-python-in-arcgis-pro-part-3-tutorial/)
- (**Optional**) Please run through the ArcGIS Notebook sample for [Forest-based Classification: Predict asthma rates](https://slustl.maps.arcgis.com/home/item.html?id=56f418e2fd4f4030917d048fd87c078f). This is both an exelent example of how to work with ```arcpy``` in ArcGIS Notebooks and using GIS to perform predictive analysis.

# Homework Questions
1. What does IDE stand for?
2. What is the extension of a Python script file?
3. What is the extention of a Jupyter notebook (or ArcGIS Notebook) file? **Hint:** Download an ArcGIS Notebook.

# Homework Exercise
Following from today's lecture, I want you to perform the same analysis in two different ways:
1. In the ArcGIS Pro Python Window, find the number of St. Louis City blocks that are found in the blocks shapefile (blocks.shp) using [get count](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/get-count.htm). Then, create a [minimum bounding geometry](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/minimum-bounding-geometry.htm) polygon of the same blocks shapefile. Add that polygon to the map, take a screenshot, and submit the screenshot.
2. Using an ArcGIS Notebook, perform the same analysis. First, unzip the **blocks.zip**. Upload all of the files from blocks.zip to the ArcGIS Notebooks **Files** so that it looks similar to this:

![](https://raw.githubusercontent.com/gbrunner/intro-prog-for-gis-rs/master/images/blocks_files.png)

In the ArcGIS Notebook, find the number of St. Louis City blocks that are found in the blocks shapefile (blocks.shp) using [get count](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/get-count.htm). Then, create a [minimum bounding geometry](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/minimum-bounding-geometry.htm) polygon of the same blocks shapefile and add the minimum bounding geometry to a map in the notebook. Submit a link to the notebook.

# Helpful links
- [St. Louis Open GIS Data](https://www.stlouis-mo.gov/data/formats/format.cfm?id=21)
