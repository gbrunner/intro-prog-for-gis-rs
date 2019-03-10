import os
import arcpy
from arcpy import env

input_table = arcpy.GetParameterAsText(0)#"C:\Answers\January2018.CSV"
output_fc =  arcpy.GetParameterAsText(1)#r"C:\Answers\crime.gdb\January2018_Crime"
spRef = arcpy.SpatialReference("NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)")

gdb_name = os.path.dirname(output_fc)
fc_name  = os.path.basename(output_fc)

env.overwriteOutput = True

arcpy.AddMessage("Creating File GDB")
#arcpy.CreateFileGDB_management(os.path.dirname(gdb_name),
#                            os.path.basename(gdb_name))

##Create table from csv file
arcpy.AddMessage(gdb_name)
arcpy.AddMessage("Converting CSV to GDB Table")
arcpy.TableToTable_conversion(input_table, gdb_name, "temp", "", "", "")

##Make XY events layer
events_layer = "crime_points"
arcpy.AddMessage("Make FC Layer")
arcpy.MakeXYEventLayer_management(os.path.join(gdb_name, "temp"), "xcoord", "ycoord", events_layer, "", "")

##Output events layer to feature class
arcpy.AddMessage("FC to FC")
arcpy.FeatureClassToFeatureClass_conversion(events_layer, gdb_name, fc_name, "", "", "")

##Define projection
arcpy.AddMessage("Defining Projection.")
arcpy.DefineProjection_management(output_fc, spRef)

arcpy.AddMessage("Done.")