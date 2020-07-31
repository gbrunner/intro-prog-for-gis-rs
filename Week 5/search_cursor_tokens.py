import arcpy
import os

#gdb = r"C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Project 1\Crime.gdb"
gdb = r'C:\Users\greg6750\Documents\IPython Notebooks\intro-prog-for-gis-rs\Project 1\project1.gdb'
feature_class = "December2017_Crime"

fc = os.path.join(gdb, feature_class)

fields = ['SHAPE@XY', 'SHAPE@AREA', 'SHAPE@LENGTH', 'SHAPE@JSON', 'SHAPE@WKT']

# For each row print the WELL_ID and WELL_TYPE fields, and the
# the feature's x,y coordinates
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        #print row[0]
        if row[2] != None:
            print 'SHAPE@XY: ' + str(row[0])
            print 'SHAPE@AREA: ' + str(row[1])
            print 'SHAPE@LENGTH: ' + str(row[2])
            print 'SHAPE@JSON: ' + str(row[3])
            print 'SHAPE@WKT: ' + str(row[4])