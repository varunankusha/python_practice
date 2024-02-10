# boolean
print(10>9)
print(10==10)
print(10<9)    

print(bool("name"))
print(bool(15))
print(bool(0))
print(bool(1))


#list
list1 = ["varun", "good", "boy"]
print(list1)
list2 = ["Varun", 9, 3.4, 'soul']
print(list2)
print(type(list1))
print(type(list2))
thislist = list(("apple", "banana", "cherry")) 
print(thislist)

print(list1[0:])
if "varun" in list1:
    print("Yes")

list1[1] = "bad"
print(list1)
list1.insert(2, "boyyy")
print(list1)
list1.append("ram")
print(list1)
list1.extend(list2)
print(list1)
list1.remove(list1[0])
print(list1)
list1.pop(2)
print(list1)
#del list2
print(list2)
list2.clear()
print(list2)

for x in list1:
    print(x)
for i in range(len(list1)):
    print(list1[i])
    
#list comprehension
list3 = [print(x) for x in list1]
print(list3)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#list1.sort()
#list1.sort(reverse = True)
#print(list1)

list4 = list3 + list1


#tuples: unchangeable, ordered, indexed, duplicated
mytuple = ("apple", "banana", "cherry")
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#unpack tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#sets:unchangeble, unordered, unindexed, nonduplicated
myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())


