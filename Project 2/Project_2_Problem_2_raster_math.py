# Using raster math

import arcpy

arcpy.env.workspace = r"C:/Users/greg6750/GIS5090/Project2/Landsat"

if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")

nn10 = arcpy.Raster("p114r075_7t20000501_z50_nn10.tif")
nn20 = arcpy.Raster("p114r075_7t20000501_z50_nn20.tif")
nn30 = arcpy.Raster("p114r075_7t20000501_z50_nn30.tif")
nn40 = arcpy.Raster("p114r075_7t20000501_z50_nn40.tif")

# The manual way - with raster algebra
raster_count = 4
mean_raster = (nn10 + nn20 + nn30 + nn40) / raster_count

# Save mean raster
mean_raster.save("Landsat_mean.tif")

# release Spatial Analyst extension
arcpy.CheckInExtension("Spatial")