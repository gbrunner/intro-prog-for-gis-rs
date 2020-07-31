# Spring 2020
## Problem 1 (15 Points)¶

Unzip imagery.zip. Create a Notebook that uses arcpy Answer the following questions:

1. How many rasters are in the folder?
2. What is the projection of the rasters?
3. Do all the rasters have the same projection?
4. How many bands to the rasters have?
5. What is the raster format?

Please use markdown cells to explain your answers. I'm not looking for anything too fancy here, just show me how you can use Python and arcpy to answer these questions.

## Problem 2 (15 Points)

Unzip tlgdb_2019_a_us_school.gdb. Create a Notebook that uses arcpy to create a report about the features in the geodatabase. List out the following:

1. Feature class name
2. Number of features in the feature class
3. Projection of the feature class
4. Shape type of the feature class (point, polyline, polygon, etc.)

Bonus (5 points) Write your results out to a text file or comma separated text file.

## Problem 3 (15 Points)

Unzip usa_cities.gdb.zip. Identify the largest cities in the United States that have a population greater than 1 million people. Using Python, print a table that lists those largest cities and their corresponding population, according to the cities feature class. Use **POPULATION** as the population field.

I recommend using ```arcpy.da.SearchCursor``` to iterate through the cities feature class to create a list of the cities and corresponding populations.

## Problem 4 (15 Points)

Unzip usa_cities.gdb.zip. Create a list of city capitals and their corresponding state.

I recommend Using ```arcpy.da.SearchCursor``` to iterate through the cities feature class to create a list of the cities and corresponding populations.

## Problem 5 (20 Points)

Create a Python script or Notebook that copies all cities with a population over 1 million to a new feature class in the same geodatabase.

I recommend exploring the following GP tools:

- [Make Feature Layer](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-feature-layer.htm)
- [Select Layer by Attribute](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-attribute.htm)
- [Copy Features](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/copy-features.htm)

### Bonus (10 points) Using a for loop, write out the following 4 feature classes:

1. Feature class with a population greater than 1 million.
2. Feature class with a population between 500,000 and 1 million.
3. Feature class with a population between 100,000 and 500,000.
4. Feature class with a population less than 100,000

## Grading

The project is out of a total of 100 points, 80 points for the problems, 20 points for you code documentation. Please use Markdown cells in your notebooks to explain what you are doing or code comments such as ## in your code cells. Any Bonus points can your score above 100 percent.


# Spring 2019: For Project 1, please complete 3 of the 4 problems below. Each problem is worth 33.3% of your total score.

1. Write a temperature conversion script to convert between Celsius and Fahrenheit, using the following equations for  the conversion:
  - F = 1.8 * C + 32
  - C = (0.56) * (F - 32)
  
  The Script should take one numerical required argument and one optional argument (the scale, F or C). If the user gives one argument, a     number, assume that the number is given in Fahrenheit.
  
  The printed statements should look something like the following:
  - 32 Fahrenheit is equivalent to 0.0 Celsius
  - 100 Celsius is equivalent to 212.0 Fahrenheit
  
2. Write a script to take one required argument, the full path and name to a GIS file (shapefile, Feature Class, Raster, etc.) and return the filetype of the output. If the filetype is a shapefile or feature class, return the geometry type (Polygon, Polyline, or Point). If the input file is not something that ArcGIS can identify, return the statement "FileType is Unknown."

Example of the input and output:

| Input | Output |
|-------|--------|
| C:/gispy/park.shp | Polygon |
| C:/gispy/getty.tif | TIFF |
| C:/gispy/spreedsheet.xlsx | FileType is Unknown |

3. Unzip project1.gdb.zip. In the geodatabase in that folder, there are 5 months worth of crime points. I want you to write a Python script that looks at each month, determines how many crimes occurred per month (using **GetCount_management**), and writes a crime report text file that lists the number of crimes per month in St. Louis. A sample output text file is attached as crime_report.txt. Your results should look similar.

4. Name the following script **shape2kml.py**. It takes two steps to convert a shapefile to KML using ArcGIS.
  - First, make a feature layer from the input shapefile with Make Feature Layer (Data Management) tool. Use park.shp as that input shapefile.
  - Second, Use the Layer to KML (Conversion) tool to convert the layer to KML.
 
 Write a Python script that converts a shapefile to a KML file.
