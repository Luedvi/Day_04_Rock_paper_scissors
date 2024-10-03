# modules are created in other python files and can be imported to use the code that's writen there.
# the "main.py" is the entry point to our programm and it's the one that will be executed when we run our code.

# The "import" syntax does not add the names of the functions defined in "chido" directly to the current namespace, it only adds the module name "chido". Using the module name you can access the functions and variables
import chido
print(chido.tejuino)
# If you intend to use a function often you can assign it to a local name
fermento = chido.tejuino
print(fermento)
chido.function_from_chido()
bark = chido.function_from_chido
bark()
# The "import as" statement helps the user provide an alias name to the original module name.
import ocean as o
print(o.shark)
print(o.seafood)
# Importing single class/functions from a module
from cool import balnearios
print(balnearios)
from cool import tuba
print(tuba)
# you can call many specific functions at a time
from party import zoo,open_door,business
print(zoo)
print(open_door)
print(business)
# The import * statement imports all the methods and constants of a particular module so you don't have to call for them individually
from sauce import*
print(breakfast)
print(dinner)
print(meal)

# There are several built-in modules in Python, which you can import whenever you like
import platform
x = platform.system()
print(x)

import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
print(local)
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)
# to use random functions first we have to import the random module
import random

# dir() function: list all the function names (or variable names) in a module
everything = dir(random)
print(everything)
print(dir(chido))
# Without arguments, dir() lists the names you have defined currently, it lists all types of names: variables, modules, functions, etc.
print(dir())
# it does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module builtins
import builtins
print(dir(builtins))

# The seed() method: is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number. By default the random number generator uses the current system time. Use the seed() method to customize the start number of the random number generator. If you use the same seed value twice you will get the same random number twice.
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())

for i in range(5):
    random.seed(0)
    print(random.randint(1, 1000))

random.seed(3)
print(random.randint(1, 1000))
random.seed(3) 
print(random.randint(1, 1000))
print(random.randint(1, 1000))
print(random.randint(1, 1000))
# randint() function generates a random integer between two numbers including both of those numbers
random_integer=random.randint(1,8)
print(random_integer)
# random() function generates a float between 0.0 to 1.0 without including the 1.0 so it could only generate .9999999 as maximum
random_float=random.random()
print(random_float)
# we can do this to increase the range of the random function
print(random_float*5)
# or simply use the uniform() function that does the same
random_float1=random.uniform(0,5)
print(random_float1)

# Lists are a type of data structure, a way of organizing and storing data, it can do the CRUD (Create, Read, Update, Delete)
#lists can store mixed data types
colors=["red",4.56,'green',True,"blue",2376,"purple",'yellow']
print(colors)

# we can use the order of the items in the list and the index or offset "[]" to call out for a specific item.
print(colors[1])
print(colors[2])
# we can use negative index as well
print(colors[-1])
print(colors[-6])
# we can even store it in another variable
color_blue=colors[4]
print(color_blue)
# to change the items in the list we write the name of the list with the index of the item we want to change and assign it to whatever we want
colors[0]="rojo"
colors[3]=1989
colors[4]=False
# append() function adds a single item to the end of the list
colors.append("white")
colors.append(45)
colors.append(True)
# extend () function adds a bunch of items to the end of the list
colors.extend(["black",98,"orange","brown"])
print(colors)

# the len() function can be used on lists to know the number of items it contains
num_of_colors=len(colors)
print(num_of_colors)
# remember the index always starts at "0" so we need to substract 1 to the total number of items the list contains to use it in the index and avoid the "index out of range" error
print(colors[num_of_colors-1])

# split() used to split a string into a list on the basis of the given separator. When maxsplit is specified, the list will contain the specified number of elements plus one.
long_string1="onebananatwobananathreebananafour"
string_as_list1=long_string1.split("banana")
print(string_as_list1)

# setting the maxsplit parameter to 1, will return a list with 2 elements
sesho = "apple#banana#cherry#orange"
duka = sesho.split("#", 1)
print(duka)

# By default, if we do not pass anything to the split() method it splits up the string on the basis of the position of spaces or line jumps "\n"
long_string="el lobo aullaba en la montaña"
print(long_string)
string_as_list=long_string.split()
print(string_as_list)

long_string2 = "el\nelefante\nse\ncolumpiaba"
print(long_string2)
string_as_list2 = long_string2.split()
print(string_as_list2)

# choice() function randomly pick up an item from a List/sequence.
random_word=random.choice(string_as_list)
print(random_word)

# list not assigned to a variable can still be printed along with random data types
print("guayaba","melon","coco",234,True)
print(f"guayaba melon coco {234} {True}")
print(["marco","polo",47,False])

# nested lists: lists inside another list
print(["France","Germany",["guadalajara","Mazatlán"],"Japan"])

warm_colors=["red","yellow","orange","brown","white"]
cold_colors=["green","blue","purple","black"]

range_of_colors=[warm_colors,cold_colors]
print(range_of_colors)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# index in nested lists: the first index is for the number of the nested list and the second digit is the item inside that nested list
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

print(range_of_colors[0])
print(range_of_colors[0][4])
print(range_of_colors[0][0])

# you can print emojis too
print("😀")

# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# https://docs.python.org/3/tutorial/datastructures.html
# https://www.askpython.com/python/string/convert-string-to-list-in-python
# https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list-in-python
# https://docs.python.org/3/library/stdtypes.html#str.split

# https://www.w3schools.com/python/ref_string_split.asp
# https://www.geeksforgeeks.org/random-seed-in-python/
# https://www.w3schools.com/python/ref_random_seed.asp
# https://docs.python.org/3/library/random.html#bookkeeping-functions
# https://docs.python.org/3/tutorial/modules.html
