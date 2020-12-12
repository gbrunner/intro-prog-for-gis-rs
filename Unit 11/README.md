# Previous Year's Lecture
- [Fall 2020](https://slu.zoom.us/rec/share/OYxYPZzy_TpNM1QVYzBIRZOVcuzdTOrbbV_q4x5kbctsg7dP2JlGXQLf_Uebk-f7.kxUonORNQubTQrjf?startTime=1603917998000)

# Project 2 Solutions
- Project_2_Solutions.ipynb
- problem_2.py
- problem_2.tbx 

# Unit 10 Assignment Solutions
- batch_geocode.ipynb
- geocode.ipynb

# Unit 11 Lectures as ArcGIS Notebooks
- [ArcGIS Notebooks on ArcGIS Online](https://slustl.maps.arcgis.com/home/group.html?id=b3d8431a10c64970b43e4ff59dd083d6#overview)

# Unit 11 Data
- Thunder_Departures_gjb.csv
- Thunder_Acquisitions_gjb.csv
- STL_Crime_gjb.gdb.zip
- STL_Crime_1.gdb.zip
- nbrhds_wards_demo1.zip
- national_rainfall_data_demogjb.zip 

# Helpful Links
- [The Color Wheel](https://www.colorspire.com/rgb-color-wheel/)

# Unit 11 Exercise and Discussion Questions 
1. For context, read this tutorial on [Adding Spreadsheet data to ArcGIS Online.](https://www.esri.com/arcgis-blog/products/arcgis-online/data-management/add-spreadsheet-data-to-arcgis-online/)
2. Optionally, watch the videos in [Symbolize Data and Publish Maps.](https://learn.arcgis.com/en/paths/symbolize-data-and-publish-maps/)
3. Download the attached CSVs. Rename them to "Thunder_Departed_" followed by your initials and ".csv" and "Thunder_Acquisitions_" followed by your initials and ".csv". Create a notebook that geocodes those CSVs of addresses and adds each to the same map object with a different symbology (see [this tutorial](https://developers.arcgis.com/python/sample-notebooks/publishing-sd-shapefiles-and-csv/#Publish-a-CSV-file-and-move-it-into-a-folder if you need help)). Save this as a webmap following from this example (https://developers.arcgis.com/python/guide/working-with-web-maps-and-web-scenes/#Saving-or-Updating-a-web-map). Be sure to go to ArcGIS online and check that the Webmap is there!

Hint: You can change the symbology by changing the renderer. For example, if you change the color values in this renderer, the points will change color accordingly.

```
simple_renderer = {
  "renderer": {
    "type": "simple",
    "symbol": {
      "color": [
        0,
        0,
        128,
        128
      ],
      "size": 15,
      "angle": 0,
      "xoffset": 0,
      "yoffset": 0,
      "type": "esriSMS",
      "style": "esriSMSCircle",
      "outline": {
        "color": [
          0,
          0,
          128,
          255
        ],
        "width": 0.99975,
        "type": "esriSLS",
        "style": "esriSLSSolid"
      }
    }
  }
}

map1.add_layer(acled, simple_renderer)
```

