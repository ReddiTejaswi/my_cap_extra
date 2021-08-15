# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:22:01 2021

@author: Dell
"""

l1=["teju","india",1,2,3]
l1.append(4)
print(l1)#Adds an element at the end of the list

x = l1.copy()
print(x)
#copy() method returns a copy of the specified list.


x = l1.count("india")
print(x)

fruits=["apple","banana","cherry"]
l1.extend(fruits)
print(l1)

print(fruits.index("cherry"))

x=fruits.insert(0,"mango")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

l1.reverse()
print(l1)

fruits.sort()
print(fruits)

l1.clear() #Removes all the elements from the list
print(l1)

