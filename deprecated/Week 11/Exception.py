import os
import arcpy
from arcpy import env

input_table = r"C:\Answers\fakelocation\January2018.CSV"
output_fc =  r"C:\Answers\crime.gdb\January2018_Crime"
spRef = arcpy.SpatialReference("NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)")

gdb_name = os.path.dirname(output_fc)
fc_name  = os.path.basename(output_fc)

#env.overwriteOutput = True

try:
    print("Creating File GDB")
    arcpy.CreateFileGDB_management(os.path.dirname(gdb_name),
                                os.path.basename(gdb_name))

    ##Create table from csv file
    print(gdb_name)
    table_name = "January2018_Table"
    out_table = os.path.join(gdb_name, table_name)
    print("Converting CSV to GDB Table")
    arcpy.TableToTable_conversion(input_table, gdb_name, table_name, "", "", "")

    ##Make XY events layer
    events_layer = "crime_points"
    print("Make FC Layer")
    arcpy.MakeXYEventLayer_management(out_table, "xcoord", "ycoord", events_layer, "", "")

    ##Output events layer to feature class
    print("FC to FC")
    arcpy.FeatureClassToFeatureClass_conversion(events_layer, gdb_name, fc_name, "", "", "")

    ##Define projection
    print("Defining Projection.")
    arcpy.DefineProjection_management(output_fc, spRef)

except Exception:
    ex_type, ex_obj, tb = sys.exc_info() #exception type, exception object, tracback
    print(ex_obj.args[0])
    print("------------------------------------")
    print("At line number " + str(tb.tb_lineno))
    print("------------------------------------")
    print(ex_type.message)

    # If using this code within a script tool, AddError can be used to return messages
    #   back to a script tool.  If not, AddError will have no effect.
    #arcpy.AddError(e.args[0])


print("Done.")