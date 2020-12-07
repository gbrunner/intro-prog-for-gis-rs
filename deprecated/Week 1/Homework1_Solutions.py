#Problem 1

happyCow = 'meadows.shp'

print(happyCow[0])
print(happyCow[0:5] + happyCow[-4:])
print(len(happyCow))
print(happyCow[0:5])
print(happyCow[-4:])
try:
    print(happyCow[11])
except:
    ('Index out of range')
print(happyCow[:5])
print(happyCow in "5meadows.shp")
print(happyCow[5])
print('W' in happyCow)

#Problem 2
#(From page 54-55 of Tateosian) Determine if each statement is True or False using the variable
LCS_ID = '0017238'

print('17' in LCS_ID)
print(LCS_ID.isdigit())
print(LCS_ID.lstrip('0') == '17238')
print(LCS_ID.zfill(10) == '10101010')
print(LCS_ID + '10' == 17248)
print(LCS_ID[6] == '3')
print(len(LCS_ID) == 7)
print(LCS_ID[0:7] == '0017238')
print(int(LCS_ID) + 10 == 17248)
print(LCS_ID != 17238)

#Problem 3
#(From page 72-73 of Tateosian) The list variable valled census is as follows:
census = ['4', '3', '79', '1', '66', '9', '1']

#Determing the following:

census = ['4', '3', '79', '1', '66', '9', '1']
print(len(census))
census = ['4', '3', '79', '1', '66', '9', '1']
census.insert(0,2)
print(census)
census = ['4', '3', '79', '1', '66', '9', '1']
census.append(2)
print(census)
census = ['4', '3', '79', '1', '66', '9', '1']
census.remove('1')
print(census)
census = '0'.join(census)
print(census)
census = ['4', '3', '79', '1', '66', '9', '1']
census.pop(3)
print(census)
census = ['4', '3', '79', '1', '66', '9', '1']
census.count('1')
print(census)
census = ['4', '3', '79', '1', '66', '9', '1']
census.sort()
print(census)
census = ['4', '3', '79', '1', '66', '9', '1']
census.reverse()
print(census)

#Problem 4
#Consider the following list:
mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]
#Determine the results of the following:
print(len(mylist))
print(mylist[2])
print(mylist[1:])
print(mylist[-1])
print(mylist.index("Cairo"))
mylist.pop(1)
print(mylist)
mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]
mylist.sort(reverse = True)
print(mylist)
mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]
mylist.append("Berlin")
print(mylist)
