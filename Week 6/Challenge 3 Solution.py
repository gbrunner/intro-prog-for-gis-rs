import arcpy
from arcpy import env

env.workspace = "C:/EsriPress/Python/Data/Exercise08"
fc = "Hawaii.shp"
newfc = "envelope8.shp"

desc = arcpy.Describe(fc)
spatialref = desc.spatialReference
extent = desc.extent
arcpy.CreateFeatureclass_management("C:/EsriPress/Python/Data/Exercise08", newfc, "Polygon", "", "", "", spatialref)
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
array.append(extent.upperLeft)
array.append(extent.upperRight)
array.append(extent.lowerRight)
array.append(extent.lowerLeft)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor