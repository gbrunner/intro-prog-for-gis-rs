import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "roads.shp"

#Create new FERRY field
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)

#create cursor object
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])

#Update fields
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1]= "NO"
    cursor.updateRow(row)
