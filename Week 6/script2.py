import os
import arcpy
from arcpy import env

input_table = r"C:\Answers\January2018.CSV"
output_fc =  r"C:\Answers\crime.gdb\January2018_Crime"
spRef = arcpy.SpatialReference("NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)")

gdb_name = os.path.dirname(output_fc)
fc_name  = os.path.basename(output_fc)

env.overwriteOutput = True

print("Creating File GDB")
#arcpy.CreateFileGDB_management(os.path.dirname(gdb_name),
#                            os.path.basename(gdb_name))

##Create table from csv file
print(gdb_name)
print("Converting CSV to GDB Table")
arcpy.TableToTable_conversion(input_table, "im_memory", "temp", "", "", "")

##Make XY events layer
events_layer = "crime_points"
print("Make FC Layer")
arcpy.MakeXYEventLayer_management("in_memory/temp", "xcoord", "ycoord", events_layer, "", "")

##Output events layer to feature class
print("FC to FC")
arcpy.FeatureClassToFeatureClass_conversion(events_layer, gdb_name, fc_name, "", "", "")

##Define projection
print("Defining Projection.")
arcpy.DefineProjection_management(output_fc, spRef)

print("Done.")