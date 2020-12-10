import arcpy
import os

fc =r'C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_6\Polygon.gdb\features'
gdb_path = os.path.dirname(fc)
fc_name = os.path.basename(fc)
gdb_folder = os.path.dirname(gdb_path)
gdb_name = os.path.basename(gdb_path)

##print(gdb_name)
##arcpy.CreateFileGDB_management(gdb_folder, gdb_name)
##
##print(fc)
##arcpy.CreateFeatureclass_management(gdb_path, fc_name,
##                                "POLYGON", "#", "DISABLED",
##                                "DISABLED", arcpy.SpatialReference(3857))

print("Insert Cursor")
fields = ('SHAPE@')
cursor = arcpy.da.InsertCursor(fc, fields)

rectangle = [(0, 533.3),
         (1000, 533.3),
         (1000, 0),
         (0, 0)]
cursor.insertRow([rectangle])

del cursor
print("Done.")