# Spring 2020

## Please Complete Both Problems
### Problem 1 (**60 Points**)
There is a tool in ArcGIS Pro and ArcMap called [Points to Line](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/points-to-line.htm). This tool creates line features from points. **For this problem, do not use that tool!**. What I want you to do is essentially create that tool using cursors.

What I would like you to do is create a line feature from the point features in **zoo_featues_wgs84.shp** by using a search cursor to retrieve the x,y locations of the points and an insert cursor to insert thost features into a new feature class.

Grading this problem breaks down as follows:
  - Read geometries from **zoo_features_wgs84.shp** (10 points)
  - Create a new *'Polyline'* features class (10 points)
  - Convert points to a line (10 points)
  - Insert points into *'Polyline'* feature class (10 points)
  - Create Python Script Tool to turn points into a polyline
    - User interface (10 points)
    - Connecting the script to the tool with right parameters (10 points)

If you a re looking for a starting point, I recoment looking at Zandbergen's Chapter 8 Challenge Problems and Solutions. 

### Problem 2 (**40 points**)
Write a Python script that uses *Raster* objects (see Zandbergen Chapter 9) and Spatial Analyst to create an average (mean) raster from p114r075_7t20000501_z50_nn10.tif, p114r075_7t20000501_z50_nn20.tif, p114r075_7t20000501_z50_nn30.tif, and p114r075_7t20000501_z50_nn40.tif found here (). Use mathematical operations similar to achieve this. If you need help, look to the exercises from Chapter 9 of Zandbergen.

# Fall 2020
