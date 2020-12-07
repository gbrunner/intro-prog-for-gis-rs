
# This Week's Reading
This week, please read the following:

- [Beginner's guide to Python in ArcGIS Pro, Part 1: Why?](https://www.esri.com/arcgis-blog/products/arcgis-pro/uncategorized/beginners-guide-to-python-in-arcgis-pro-part-1-why/)
- [Beginner’s guide to Python in ArcGIS Pro, Part 2: How?](https://www.esri.com/arcgis-blog/products/arcgis-pro/analytics/beginners-guide-to-python-in-arcgis-pro-part-2-how/)
- [Chapters 1 and Chapters 4 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12)

# Previous Year's Lectures
Here are the links to the first lecture from last year. This link is not intended to be used in place of this week's lecture. I am providing it as an additional resource for extra context.

## Spring 2020 Lecture
- [First half of lecture](https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e01fab5b-e86b-4f7a-b584-ab41016e8a56)
- [Second half of lecture](https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d55b6de0-817d-479d-86d6-ab410188ecf4)

## Fall 2020 Lecture
- [Zoom recording](https://slu.zoom.us/rec/play/FeNAZ1ruxVAa3FwrttmrPTxuTHrOyQceStUPoJc9Qj6jpcXRGvwnZcCmVilK10_dbni_oJqzLlYNt_WT.pD2l6-QK2IjXEoiH?continueMode=true&_x_zm_rtaid=oY7Wzfb7TYef6MXTUOGbmQ.1607305401735.4169a61a5e210c03dc5417b54ccddc08&_x_zm_rhtaid=53) - Fast forward 15 minutes to when the class starts.

# Presentations
See the [Welcome.pptx](https://github.com/gbrunner/intro-prog-for-gis-rs/blob/master/Unit%201/Welcome.pptx) and [Unit_1_Slides.pptx](https://github.com/gbrunner/intro-prog-for-gis-rs/blob/master/Unit%201/Lecture_1_Slides.pptx).

# Data and Notebooks
This week's lecture notebooks can be found in the GIS [4090\5090 Unit 1 Notebooks group on ArcGIS Online](https://slustl.maps.arcgis.com/home/group.html?id=7ec8ff1c45d94eb28c6c6ddaadcf0333#overview) or [downloaded here](https://slustl.maps.arcgis.com/home/group.html?id=7ec8ff1c45d94eb28c6c6ddaadcf0333#overview). Please download the Missouri.gdb.zip so that we can use it for the lecture.

# Configuring Jupyter Notebooks
This document [**configuring_the_notebook_directory.html**]() provides instructions to configure Jupyter Notebooks on your computer. We will go through this process to setup Jupyter Notebooks on your lab computer or personal computer.

#  Unit 1 Exercise and Discussion Questions 
## Homework Exercises
Before completing the assignment, I recommend completing the following exercises. Completing these 3 exercises should not take more than an hour.

1. Complete the [Hello, Notebook!](https://www.arcgis.com/home/item.html?id=282e3eb54e844e25b2687d66f59b91be) excercise. After you complete it, add another map object and a different dataset to the map. Save the Notebook and share the link to the Notebook here. I will be able to see your notebook even if you don't explicitly share it with me in ArcGIS Online becuase I am an administrator in the ArcGIS Online organization.
2. Please complete [Python Scripting for ArcGIS Pro Exercise 1](https://learngis.maps.arcgis.com/home/item.html?id=450cc6119d7a45849e7290461c5bdde3). This should take no more than 15 minutes.
3. Please complete [Python Scripting for ArcGIS Pro Exercise 4](https://learngis.maps.arcgis.com/home/item.html?id=45c4696b6c4c4f449d2f875d24efd950). This will take a little bit longer but I think you will find it very helpful. Please submit the Python scripts that you create.

## Discussion Questions
Please submit a Word file or text file that answers the following questions.

1. What is the version Python that comes with ArcGIS Pro?
2. Name 3 methods of string objects in Python and give an example of each.
3. What two values can a boolean take on?
4. How do you denote a comment line in Python and what should yo use comments?


# Unit 1 Assignment
Please submit a Word file, text file, or ArcGIS Notebook that answers the following questions. If you do this in ArcGIS Notebooks, you can save the notebook and just send me a URL to the item in ArcGIS Online. 

1. What is the version Python that comes with ArcGIS Pro?
2. Name 3 methods of string objects in Python and give an example of each.
3. What two values can a boolean take on?
4. How do you denote a comment line in Python and what should yo use comments?
5. (From page 54-55 of Tateosian) Consider the following variable called ```happyCow```
  
```happyCow = 'meadows.shp'```
  
Determine the following:
  - ```happyCow[0]```
  - ```happyCow[0:5] + happyCow[-4:]```
  - ```len(happyCow)```
  - ```happyCow[0:5]```
  - ```happyCow[-4:]```
  - ```happyCow[11]```
  - ```happyCow[:5]```
  - ```happyCow in "5meadows.shp"```
  - ```happyCow[5]```
  - ```'W' in happyCow```
  
6. (From page 54-55 of Tateosian) Determine if each statement is ```True``` or ```False``` using the variable ```LCS_ID = '0017238'```
  - ```'17' in LCS_ID``` 
  - ```LCS_ID.isdigit()```
  - ```LCS_ID.lstrip('0') == '17238'```
  - ```LCS_ID.zfill(10) == '10101010'```
  - ```LCS_ID + '10' == 17248```
  - ```LCS_ID[6] == '3'```
  - ```len(LCS_ID) == 7```
  - ```LCS_ID[0:7] == '0017238'```
  - ```int(LCS_ID) + 10 == 17248```
  - ```LCS_ID != 17238```
  
7. (From page 72-73 of Tateosian) The list variable valled **census** is as follows:

```census = ['4', '3', '79', '1', '66', '9', '1']```

Determing the following:
- ```len(census)```
- ```census.insert(0,2)```
- ```census.append(2)```
- ```census.remove('1')```
- ```census = '0'.join(census)```
- ```census.pop(3)```
- ```census.count('1')```
- ```census.sort()```
- ```census.reverse()```
  
8. Consider the following list:
  
```mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]```
  
Determine the results of the following:
  - ```len(mylist)```
  - ```mylist[2]```
  - ```mylist[1:]```
  - ```mylist[-1]```
  - ```mylist.index("Cairo")```
  - ```mylist.pop(1)```
  - ```mylist.sort(reverse = True)```
  - ```mylist.append("Berlin")```
    
These operations are all to be performed on the original list—that is, not
as a sequence of operations. Try to determine the answer manually first,
and then check your result by running the code.
