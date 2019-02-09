import arcpy
import os
from arcpy import env

in_files = arcpy.GetParameterAsText(0).split(";") #r"C:\Answers\project1.gdb"
report = arcpy.GetParameterAsText(1)   #r"C:\Answers\crime_report.txt"

arcpy.AddMessage(in_files)

#env.workspace= in_gdb
#env.overwriteOutput = True

with open(report, 'w') as f:
    #fclist = arcpy.ListFeatureClasses()
    for fc in in_files:
        fcdescribe = arcpy.Describe(fc)
        result = arcpy.GetCount_management(fc)
        f.write("In " + fcdescribe.name[:-10] + " there were " + str(result) + " crimes.\n")
f.close()

arcpy.AddMessage("Done.")
