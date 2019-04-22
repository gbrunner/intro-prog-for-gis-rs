# Solution Using arcpy Cell Statistics tool

import arcpy
from arcpy import env
from arcpy.sa import *

# Moved/saved four raster to separate folder names Results
env.workspace = "C:/Users/greg6750/GIS5090/Project2/Landsat_p114r75/Results"

# Checkout Spatial Analyst Extension
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")

# List rasters in the folder
rasters = arcpy.ListRasters()

# Run CellStatistics
calc = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")

# Save Raster
calc.save("C:/Users/greg6750/GIS5090/Project2/mean_raster.tif")

# Check In Extension
arcpy.CheckInExtension("Spatial")