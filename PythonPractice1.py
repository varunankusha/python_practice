#1st program
print "Hello World!"

#indentaion
if(5>2):
    print("5 is greter than 2")
    
#comments
#multiline1
#multiline2
"""more than just one line"""
'''more than just a line '''

#variables
x= 5   #type int
y = "john" #type str

print(x,y)


#casting
a = str(3)
b= int (3)
c= float(3)

print(a,b,c)

#type checking
print(type(a), type(b), type(c))

#multiple assignment
c,d,e = 1,2,3

#single line assignement for multiple variables
c=d=e=1
print(c,d,e)


#unpacking a list

fruits = ["mango", "banana", "orange"]

x,y,z = fruits

print(x,y,z)

#global variables and global keyword

x = "global"
def local_fun():
    x="local"
    print(x)
local_fun()
print(x)

x = "global"
def local_fun():
    global x
    x="local"
    print(x)
local_fun()
print(x)


#int,float,complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#random
import random
print(random.randrange(1,10))


#strings
a="varun"
b='engineering'
c="""varun has completed engineering"""
print(a,b,c)
#strings are arrays
print(a[1],a[2],a[3])
print(len(b))
#looping through strings
#for i in c:
    #print(i)

#checking in string
print("varun" in  c)
print("varun" not in c)

if "has" in c:
    print("yes")

if "has" not in c:
    print("No")    
    
#slicing
print(c[2:5])
print([c[:6]]) 
print(c[2:])
print(c[-5:-2])

#strip , split, upper, lower, replace
print(c.strip())
print(a.upper())
print(b.lower())
print(a.replace('n', 'k'))
print(c.split(","))
print(a+b)

#format string
age = 24
txt = "varun is {} old guy"
print(txt.format(age))
txt2 = "varun {2} and {1} and {0}"
print(txt2.format(a,b,c))
