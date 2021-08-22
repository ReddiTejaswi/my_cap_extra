# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:15:33 2021

@author: Dell
"""

"""
1. While and For loop - implement break and continue statement
"""
li=[1,2,3,5,7,8]
for i in li:
    if i==5:
        continue
    print(i)

for i in li:
    if i==5:
        break
    print(i)
    
i=1
while i<5:
    print(i)
    if i==4:
        break
    i=i+1
    
i=0
while i<5:
    i=i+1
    if i==4:
        continue
    print(i)
    



    
"""
2. For loop - create the following star triangle pattern using For Loop only
    *
   * *
  * * *
 * * * *
 """
n=4
k=n-1 
for i in range(0,4):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end=" ")
    print("\n")

    
    
"""
3. W3schools - Dictionary methods (just like strings and lists do it for dictionary)
"""
dict1={"name":"teju","place":"AP","age":20}
#The copy() method returns a copy of the specified dictionary.
print(dict1.copy())
#Returns a dictionary with the specified keys and value
x=("name","place","age")
y=("teju",20)
print(dict.fromkeys(x,y))
#The get() method returns the value of the item with the specified key.
print(dict1.get("place"))
# items() Returns a list containing a tuple for each key value pair
print(dict1.items())
#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
print(dict1.keys())
#pop() removes item from dictionary
print(dict1.pop("age"))
print(dict1)
# popitem() removes the last inserted key-value pair
print(dict1.popitem())
print(dict1)
#The setdefault() method returns the value of the item with the specified key.
print(dict1.setdefault("place","mumbai"))
#The update() method inserts the specified items to the dictionary
#key value pairs should be given
dict1.update({"color":"blue"})
print(dict1)
# values() method returns the values of dict as a list
print(dict1.values())
#clear() method removes all elements from the dict
x=dict1.clear()
print(dict1)