# Reading
Please read Chapters 2 and 3 of [Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12). These two chapters cover Python IDEs and Geoprocessing in ArcGIS Pro. This will set a foundation for much of what we do.

# Lecture Notebooks
Lecture notebooks can be found in the [GIS 4090\5090 Unit 2 Notebooks](https://slustl.maps.arcgis.com/home/group.html?id=724c1bfb085843debf8f1020b3654045#overview) group.

# Classwork Exercise
Please complete the following exercises. You do not need to submit anything, but it is recommended that you complete these.
- Please Complete [Python Scripting Exercise 3](https://learngis.maps.arcgis.com/home/item.html?id=3978b52f1e5847c69ef7eaded85780b2). You can find the data [here](https://learngis.maps.arcgis.com/home/item.html?id=d7c05cf515c046c2bedacb2e8e24722c).
- [Beginner's guide to Python in ArcGIS Pro, Part 3: Tutorial](https://www.esri.com/arcgis-blog/products/arcgis-pro/uncategorized/beginners-guide-to-python-in-arcgis-pro-part-3-tutorial/)
- (**Optional**)Please run through the ArcGIS Notebook sample for [Forest-based Classification: Predict asthma rates](https://slustl.maps.arcgis.com/home/item.html?id=56f418e2fd4f4030917d048fd87c078f). This is both an exelent example of how to work with ```arcpy``` in ArcGIS Notebooks and using GIS to perform predictive analysis.

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
