# For Project 1, please complete 3 of the 4 problems below. Each problem is worth 33.3% of your total score.

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
| C:/gispy/tree.tif | TIFF |
| C:/gispy/spreedsheet.xlsx | FileType is Unknown |

3. Unzip project1.gdb.zip. In the geodatabase in that folder, there are 5 months worth of crime points. I want you to write a Python script that looks at each month, determines how many crimes occurred per month (using **GetCount_management**), and writes a crime report text file that lists the number of crimes per month in St. Louis. A sample output text file is attached as crime_report.txt. Your results should look similar.

4. **For an A+** Name the following script **shape2kml.py**. It takes two steps to convert a shapefile to KML using ArcGIS.
  - First, make a feature layer from the input shapefile with Make Feature Layer (Data Management) tool.
  - Second, Use the Layer to KML (Conversion) tool to convert the layer to KML.
 
 Write a Python script that converts a shapefile to a KML file.
