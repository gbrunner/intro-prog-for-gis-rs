# Reading
- [Beginner's guide to Python in ArcGIS Pro, Part 1: Why?](https://www.esri.com/arcgis-blog/products/arcgis-pro/uncategorized/beginners-guide-to-python-in-arcgis-pro-part-1-why/)
- [Beginner's guide to Python in ArcGIS Pro, Part 1: Why?](https://www.esri.com/arcgis-blog/products/arcgis-pro/analytics/beginners-guide-to-python-in-arcgis-pro-part-2-how/)
- Read [Chapters 1 and Chapters 4 of Python Scripting for ArcGIS Pro](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=384&moduleID=12)

# Homework Exercises
Complete the [Hello, Notebook!](https://www.arcgis.com/home/item.html?id=282e3eb54e844e25b2687d66f59b91be) excercise. After you complete it, add another map object and a different dataset to the map. Save the Notebook and share the link to the Notebook here. I will be able to see your notebook even if you don't explicitly share it with me in ArcGIS Online becuase I am an administrator in the ArcGIS Online organization.

# Homework Problems
Submit a word document, text file, or ArcGIS Notebook with answers to the following questions:

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
  
