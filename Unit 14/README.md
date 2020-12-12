# Working with Image Services
- [This weeks notebooks are in ArcGIS Online as ArcGIS Notebooks](https://slustl.maps.arcgis.com/home/group.html?id=8924b798d1884dd1b86d9f3ec73e13fe#overviewIS%204090\5090)

# Previous Year's Lexctures
- Fall 2020: [Part 1](https://slu.zoom.us/rec/share/qSK0U3_c7_TFtMCICgBoflQKADQeRWXv9tCA29gQ6qaUGVytxozrkyc2VbTxsWAn.ZGCiCWw7bDtmGjyh?startTime=1605736770000) and [Part 2](https://slu.zoom.us/rec/share/qSK0U3_c7_TFtMCICgBoflQKADQeRWXv9tCA29gQ6qaUGVytxozrkyc2VbTxsWAn.ZGCiCWw7bDtmGjyh?startTime=1605741203000)
- [Spring 2020](https://slu.zoom.us/rec/share/2HHDMs-SPt0FzJgZLdJfuJ-kt301BHK_htQcNpHKhC5SdV9xpYMruOmKclRFWQtz.dOTafNgJAfNaXcwy?startTime=1588021338000)

# This week's lesson plan
## Lecture 1 - Image Services with ArcGIS Online
1. Show using the Landsat Service in ArcGIS Online.
2. Go into ArcGIS Notebooks and show manipulating the same service with the ArcGIS API for Python.

## Lecture 2 - Multidimensional Data in ArcGIS Pro
1. Create a new ArcGIS Pro Map Project
2. Add Data
3. Choose Multidimensional Raster Layer and then add **daymet_v3_tmin_monavg_2017_na.nc4***.
![](https://github.com/gbrunner/developing-with-imagery/blob/master/Week%205/add_multidim_raster_layer.png?raw=true)

4. Notice how th data gets added with a time-slider in the view.
![](https://github.com/gbrunner/developing-with-imagery/blob/master/Week%205/multidim_raster_layer.png?raw=true)

5. Right click on layer in Table of Contents. **Select Create Chart** -> **Temporal Profile**
6. Set chart parameters.
7. Choose **Point** for **Area of Interest** and click on map to see temperature profile.
![](https://github.com/gbrunner/developing-with-imagery/blob/master/Week%205/temp_profiles.png?raw=true)

8. Export Raster as CRF. We will use this as input into the arcpy API.

## Lecture 3 - Multidimensional Data with Arcpy
Demonstrate how we can use **Raster** objects using the **arcpy API** to do similar analysis. This can be demonstrated through the [**multidimensional_data_using_arcpy_api.ipynb**](https://github.com/gbrunner/developing-with-imagery/blob/master/Week%205/multidimensional_data_using_arcpy_api.ipynb) Notebook.

# What does *Advanced Programming for GIS and Remote Sensing* cover?
- [Here is the GitHub page!](https://github.com/gbrunner/adv-python-for-gis-and-rs/)

# What's Next
- [Conda](https://www.youtube.com/watch?v=23aQdrS58e0)
- [ArcGIS Javascript API](https://www.youtube.com/watch?v=pYHWoSNsSIU) 
- [Leaflet](https://leafletjs.com/examples.html)

# Helpful Links
- [ArcGIS Javascript API Documentation](https://developers.arcgis.com/javascript/latest/showcase/)
- [Esri GeoDev Hacker Labs](https://github.com/Esri/geodev-hackerlabs)
