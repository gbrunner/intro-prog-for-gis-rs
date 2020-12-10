import arcpy
import os
from arcpy import env

in_gdb = r"C:\Answers\project1.gdb"
report = r"C:\Answers\crime_report_2.txt"

env.workspace= in_gdb
env.overwriteOutput = True

print("Generating Report.")
with open(report, 'w') as f:
    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        fcdescribe = arcpy.Describe(fc)
        result = arcpy.GetCount_management(fc)
        f.write("In " + fcdescribe.name[:-10] + " there were " + str(result) + " crimes.\n")
f.close()

pring("Done.")
