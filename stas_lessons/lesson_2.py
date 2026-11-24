# -*- coding: utf-8 -*-
##############################################################################
__author__ = "stas.savinov"
__version__ = "$ Version 1.0 $"
__data__ = "$ Lesson # 2 $"

##############################################################################
#                                    IMPORTS GLOBAL
##############################################################################
import sys
import os
import time
import signal
import dis

##############################################################################
#                                    IMPORTS LOCAL
##############################################################################


##############################################################################
# CONST VALUES
##############################################################################

python1_string = "--<==========Oo>~"
python2_string = "--<=====(O.O)"
python3_string = "__<=========;>~"

spaces = "\n\n\n"


##############################################################################
# Name                  - ex1
# Parameters            - none
# Description           - example of tuple as data structure
##############################################################################
def ex1():
    print("\n Today we will continue with data structures.\n Tuplets and strings \n")
    print("'Strings' and 'tuples' are immutable sequence types: such objects cannot be modified once created.\n"
          "Also 'xrange', but that we leave for later.")

    print("\nAnd tuples don’t have methods the way lists do.")

    input("If we separate values with comas in () --> we have tuplets")

    input("\n Example >>> ('O','.','O') ")

    print("\n>>> 42,")
    print(42, )

    input("\n Example >>> 3*(30+3,) ")
    print(3 * (30 + 3,))


##############################################################################
# Name                  - ex1mutable
# Parameters            - none
# Description           - explaining of mutable data structure
##############################################################################
def ex1mutable():
    input("s[i] = x	item i of s is replaced by x")
    input("s[i:j] = t	slice of s from i to j is replaced by the contents of the iterable t	 ")
    input("del s[i:j]	same as s[i:j] = []	 ")
    input("s[i:j:k] = t	the elements of s[i:j:k] are replaced by those of t	")
    input("del s[i:j:k]	removes the elements of s[i:j:k] from the list	 ")
    input("s.append(x)	same as s[len(s):len(s)] = [x]	")
    input("s.extend(x)	same as s[len(s):len(s)] = x	")
    input("s.count(x)	return number of i‘s for which s[i] == x	 ")
    input("s.index(x[, i[, j]])	return smallest k such that s[k] == x and i <= k < j")
    input("s.insert(i, x)	same as s[i:i] = [x]	")
    input("s.pop([i])	same as x = s[i]; del s[i]; return x")
    input("s.remove(x)	same as del s[s.index(x)]	")
    input("s.reverse()	reverses the items of s in place")
    input("s.sort([cmp[, key[, reverse]]])	sort the items of s in place")


##############################################################################
# Name                  - ex2
# Parameters            - none
# Description           - example of tuples as data structure
##############################################################################
def ex2():
    print("\n Tuples can be created as lists! \n")

    input("Remember my_list = list('Gena')\n")
    my_list = list('Gena')
    input("\n Preaty the same my_tuple = tuple('gena')\n")
    my_tuple = tuple('gena')

    input("\n Let's print them \n")

    print(my_list)
    print(my_tuple)

    input("\n Let's look at there attributes \n")

    attribute_my_list = dir(my_list)
    attribute_my_tuple = dir(my_tuple)

    print(getattr(my_list, attribute_my_list[0]))
    print(getattr(my_tuple, attribute_my_tuple[0]))


##############################################################################
# Name                  - ex3
# Parameters            - none
# Description           - example of tuples as data structure
##############################################################################
def ex3():
    print("\n Tuples can be used like lists! \n")
    input("Genadij = ('+','<','=','=','0','-','0') \n")
    Genadij = ('+', '<', '=', '=', '0', '-', '0')
    input("Genadij[0] \n")
    print(Genadij[0])

    input("Genadij[0:3] \n")
    print(Genadij[0:3])

    input("\n But Genadij[0]='!' will show error! \n")


##############################################################################
# Name                  - ex4
# Parameters            - none
# Description           - first explanation for what do we need tuples
##############################################################################
def ex4():
    print("\n So why do we need tuples, if we have lists ??? \n")

    print("They are returned by some built-in functions and methods, which"
          "means that you haveto deal with them.\n")

    input("They can be used as keys in mappings—lists can’t be.\n")

    input("We need to touch tupls!\n But to do so, we need to learn"
          " one more thing -> dictionary! So lets look at them, and"
          "then return to 'strings' !\n\n")

    input("\nOnce more about toplets \n Let's creat tuple"
          ">>>\n  lab_rat = ('python', 'Genadij') ")
    lab_rat = ('python', 'Genadij')

    input("\n>>>  (whois, name) = lab_rat")
    (whois, name) = lab_rat

    input("\n>>> print(whois) ")
    print(whois)
    input("\n>>>  print(name)")
    print(name)


##############################################################################
# Name                  - ex5
# Parameters            - none
# Description           -  explanation for what do we need dict
##############################################################################
def ex5():
    print("\n\n Ok! We use 'LISTS'  when you want to group values into a"
          " structure and refer to each value by number.\n\n")

    input("But dictionary--> ")
    print("\n a data structure in which you can refer to each value by name.")

    input("\n\n What can do dictionary? ")

    input("The values in a dictionary don’t have any order, but "
          "are stored under a key (number,string,tuple).")

    input("\n\n More examples: ")

    input("\n\n     >>>  pythons_names  = ['Gena',Roma']")
    pythons_names = ['Gena', 'Roma']

    input("\n\n     >>>  pythons_lenght = [5,3]")
    pythons_lenght = [5, 3]

    input("\n Using lists, search can be like this\n >>> pythons_lenght[pythons_names.index('Gena')]")
    length = pythons_lenght[pythons_names.index('Gena')]
    print(length)

    input("\n\n With dictionary it can be like this: ")
    input("\n\n >>> python_dict={'Gena':5,'Roma':3} ")

    python_dict = {'Gena': 5, 'Roma': 3}

    input("\n\n >>> python_dict['Gena']  ")
    print(python_dict['Gena'])
    print(spaces)


##############################################################################
# Name                  - ex6
# Parameters            - none
# Description           -
##############################################################################
def ex6():
    print("\n\n Ok! What a surprise, but if we had: \n\n"
          "\n 1. lists      = list()"
          "\n 2. tuples     = tuple()"
          "\n 3. dictionary = dict()")

    input("\n\n We can creat it like this:  ")
    input("\n\n >>> record = [('name', 'Gena'), ('length', 42)] ")

    record = [('name', 'Gena'), ('length', 42)]
    input("\n\n >>> dictionary = dict(items) ")

    dictionary = dict(record)

    input("\n\n >>> print(dictionary['name']) ")
    print(dictionary['name'])

    input("\n\n OR We can creat it like this:  ")
    input("\n\n  dictionary = dict(name='Gena', length=42)  ")
    dictionary = dict(name='Gena', length=42)
    input("\n\n >>> print(dictionary['name']) ")
    print(dictionary['name'])


##############################################################################
# Name                  - ex7
# Parameters            - none
# Description           -
##############################################################################
def ex7():
    print("\n\n Let's make little complicated :) \n\n")
    print("1. Dictionary keys don't have to be integers\n"
          "\n If we create list                        \n"
          ">>>Name = []                                \n"
          ">>>Name[5]='Gena'                           \n"
          ">>>Name                                     \n"
          "We will have an error                       \n")

    print("But with dict!!!"
          ">>>Name = {} \n"
          ">>>Name[5]='Gena' \n"
          ">>>Name")

    Name = {}
    Name[5] = 'Gena'
    print(Name)


##############################################################################
# Name                  - ex8
# Parameters            - none
# Description           -
##############################################################################
def ex8():
    print("\n\n Methods of dictionary: \n\n")

    print("\n 1. clear      - removes all items from dict")
    print("\n 2. copy       - returns a new dictionary with the same key-value pairs")
    print("\n 3. fromkeys   - method creates a new dictionary with the given keys,"
          " each with a default corresponding value of None:")
    print("\n 4. get        - a forgiving way of accessing dictionary items.")
    print("\n 5. has_key    - method checks whether a dictionary has a given key.")
    print("\n 6. items and iteritems - method returns all the items of the "
          " dictionary as a list of items in which each item is of the form (key, value).")
    print("\n 7. keys and iterkeys   - method returns a list of the keys in the dictionary")
    print("\n 8. pop       - method can be used to get the value corresponding to a given key,"
          "and then remove the key-value pair from the dictionary:")
    print("\n 9. popitem   - popitem pops off a random item because dictionaries"
          " don’t have a “last element” or any order whatsoever.")
    print("\n 10. setdefault - somewhat similar to get, except that in addition"
          " to the get functionality, setdefault sets the value corresponding to the given key")
    print("\n 11. update     - method updates one dictionary with the items of another")
    print("\n 12. values and itervalues - method returns a list of the values in the dictionary")

    print("\n\n ---------------------------------------------- \n\n")

    print("\n\n Lets see examples")

    print("\n\n CLEAR ")
    input("\n\n >>> python_dict={'Gena':5,'Roma':3} ")
    python_dict = {'Gena': 5, 'Roma': 3}
    python_dict.clear()
    input("\n\n>>>python_dict.clear()")
    print(python_dict)

    print("\n\n COPY ")
    python_dict = {'Gena': 5, 'Roma': 3}
    print("\n\n >>> copy_dict = python_dict.copy() ")
    copy_dict = python_dict.copy()
    input("\n\n>>>copy_dict")
    print(copy_dict)

    print("\n\n FRONT_KEY ")
    print("\n\n >>> {}.fromkeys(['name', 'age'])")
    input("\n\n >>> {'age': None, 'name': None}")
    print({}.fromkeys(['name', 'age']))

    print("\n\n GET ")
    python_dict = {'Gena': 5, 'Roma': 3}
    input("\n\n >>> python_dict.get('Gena')")
    print(python_dict.get('Gena'))

    print("\n\n HAS_KEY ")
    python_dict = {'Gena': 5, 'Roma': 3}
    input("\n\n >>> python_dict.has_key('Gena')")
    # print(python_dict.has_key('Gena'))

    print("\n\n ITEMS -> return as list")
    python_dict = {'Gena': 5, 'Roma': 3}
    input("\n\n>>> python_dict.items() ")
    print(python_dict.items())
    print("\n\n now it's list ")
    python_dict = {'Gena': 5, 'Roma': 3}
    input("\n\n>>> And dict is like this ")
    print(python_dict)

    print("\n\n POP ")
    python_dict = {'Gena': 5, 'Roma': 3}
    input("\n\n >>> python_dict.pop('Gena')")
    print(python_dict.pop('Gena'))
    input("\n\n >>> python_dict")
    print(python_dict)

    print("\n\n POP ITEM -> get random elem... we have no last elements")
    python_dict = {'Gena': 5, 'Roma': 3}
    input("\n\n >>> python_dict.popitem()")
    print(python_dict.popitem())
    input("\n\n >>> python_dict")
    print(python_dict)

    print("\n\n SETDEFAULT ")
    input("\n\n >>> python_dict = {} ")
    python_dict = {}

    input("\n\n >>> python_dict.setdefault('name','HZ')")
    python_dict.setdefault('name', 'HZ')
    print(python_dict)

    input("\n\n But if we set value >>> python_dict['name'] = 'Gena' ")
    python_dict['name'] = 'Gena'
    print(python_dict)
    input("\n\n But if we set value >>> python_dict.setdefault('name','HZ') ")
    python_dict.setdefault('name', 'HZ')
    print(python_dict)

    print("\n\n UPDATE")
    print("\n\n update ONE dict with item from ANOTHER")
    input("\n\n >>> python_dict1 = {'Gena':42} ")
    input("\n\n >>> python_dict2 = {'Roma':33} ")
    input("\n\n >>> python_dict1.update(python_dict2)")
    python_dict1 = {'Gena': 42}
    python_dict2 = {'Roma': 33}
    python_dict1.update(python_dict2)
    print(python_dict1)

    print("\n\n VALUES")
    input("\n\n >>> python_dict1.values() ")
    print(python_dict1.values())


##############################################################################
# Name                  - answer1
# Parameters            - none
# Description           - This is few answers from previous lesson
##############################################################################
##############################################################################
def answer1():
    print("\nFrom Python 3.0 \n")
    print(" builtin.sorted() and list.sort() no longer accept the 'cmp' "
          " argument providing a comparison function. Use the key argument"
          "instead. N.B. the key and reverse arguments are now keyword-only")

    print("\n The cmp() function should be treated as gone")


##############################################################################
def answer2():
    print("\n a = True \n")
    a = True
    attribute = dir(a)
    print(getattr(a, attribute[2]))

    print("\n ------------------ \n")

    def f():
        b = True
        return b

    attribute1 = dir(f)
    print(getattr(f(), attribute1[2]))

    pass


##############################################################################
def answer3():
    print("\n Remember issue: int(100)  is int(100)  >>> True")
    print("\n and....         int(1000) is int(1000) >>> False")

    input("\n\n In reality this is cashing issue of interpretor")

    print("\n\n From [-5] to [256] or [255] --- when you create an int in that "
          "range you actually just get back a reference to the existing object")

    input("\n>>> int('256') is int('256') ")
    print(int("256") is int("256"))

    input("\n>>> int('-5') is int('-5') ")
    print(int("-5") is int("-5"))

    input("\n>>> int('-6') is int('-6') ")
    print(int("-6") is int("-6"))


##############################################################################
def home():
    print("\n Home Taks! \n")
    print("\n Please create database using dictionary, inputs, tuplets\n")
    print("\n Use 4-5 entries \n")
    print("\n You may not use loops \n")


##############################################################################
def fin():
    print('\n Thanks for your attention \n')


##############################################################################
# Name                  - main
# Parameters            - argv - file name
# Created               -
# Date                  -
##############################################################################
if __name__ == "__main__":
    print(spaces)
    #ex1()
    #ex1mutable()
    #ex2()
    #ex3()
    #ex4()
    # ex5()
    # ex6()
    # ex7()
    ex8()




