import arcpy
import os

#arcpy.env.overwriteOutput = True
#arcpy.env.XYTolerance = "0.02 Meters"
arcpy.AddMessage(arcpy.env.XYTolerance)

input_fc = arcpy.GetParameterAsText(0)  # rC:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\zoo_featues_wgs84.shp'
output_fc = arcpy.GetParameterAsText(1) # r'C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\new_polyline15.shp'

zoo = input_fc

array = arcpy.Array()
cursor = arcpy.da.SearchCursor(zoo,["SHAPE@XY"])
arcpy.AddMessage("Opening Search Cursor")
for row in cursor:
    x, y = row[0]
    array.add(arcpy.Point(x,y))
    print("{0}, {1}".format(x,y))

polyline = arcpy.Polyline(arcpy.Array(array))
del cursor, row

sp_ref = arcpy.Describe(input_fc).spatialReference
outloc = os.path.dirname(output_fc)
outfile = os.path.basename(output_fc)
arcpy.AddMessage("Creating POLYLINE Feature Class.")
arcpy.CreateFeatureclass_management(outloc, outfile, "POLYLINE",
                                    "", "ENABLED", "ENABLED", input_fc)

arcpy.AddMessage("Inserting Features into POLYLINE Feature Class")
i_cursor = arcpy.da.InsertCursor(
    output_fc, ['SHAPE@'])

i_cursor.insertRow([polyline])
del i_cursor
arcpy.AddMessage("Done.")
