import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"

#SQL statements to select features
sql1 = " \"FEATURE\" = 'Airport'"
sql2 = " \"FEATURE\" = 'Seaplane Base'"

#Select
arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp", sql1)
arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sql2)

#Buffer
arcpy.Buffer_analysis("Results/airports_final.shp", "Results/aiports_ buffers.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_ buffers.shp", "7500 METERS")