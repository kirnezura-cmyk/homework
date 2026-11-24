# -*- coding: utf-8 -*-
##############################################################################
__author__ = "stas.savinov"
__version__ = "$ Version 1.0 $"
__data__ = "$ Lesson # 3 $"

##############################################################################
#                                    IMPORTS GLOBAL
##############################################################################
import sys
import os
import time
import signal
import dis

import string

# from string import maketrans
##############################################################################
#                                    IMPORTS LOCAL
##############################################################################

## from string import Template --- don't forget to show this

##############################################################################
# CONST VALUES
##############################################################################

spaces = "\n\n\n"


##############################################################################
# Name                  - ex1mutable
# Parameters            - none
# Description           - explaining of muttable data structure
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
# Name                  - ex1
# Parameters            - none
# Description           - example of tuple as data structure
##############################################################################
def ex1():
    print("\n Strings are simple and easy to use! \n")

    tongue_twister = ("If you understand, say - understand.\n\n"
                      "If you don't understand, say  - don't understand'\n"
                      "But if you understand and say - don't understand.\n"
                      "How do I understand that you understand? Understand!\n")

    print("\n Let's say we have string:\n", tongue_twister)

    input("\n Buy the way! Do you still remember lists, tuples?")
    print("\n 1. lists      = list()  or list  as  []"
          "\n 2. tuples     = tuple() or tuple as  ()"
          "\n 3. dictionary = dict()  or dict  as  {}")

    input("\nSo we can do something like string[-12:]\n")
    print(tongue_twister[-12:])

    input("\n BUT! Strings are immutable, so if you try: \n")
    print(">>>string[-12:] = 'NO!' ")
    input("")
    tongue_twister[-12:] = 'NO!'


##############################################################################
# Name                  - ex2
# Parameters            - none
# Description           - example of tuples as data structure
##############################################################################
def ex2():
    print("\n But let's go step by step :) Shall we? \n")

    input("String formating \n\n")

    print(" format_string = 'We like %s. %s next'   \n")
    print(" adding_strings = ( 'Python', 'What's ') \n")
    print(" print (format_string % adding_string)   \n")

    format_string = "We like %s. %s next"
    adding_strings = ("Python", "What's")
    input(spaces)
    print(format_string % adding_strings)

    print("\n\n Magic with '%' character. Remember where we used it? ")
    input(spaces)

    print(" format_string = 'What is the answer? That is:%d' ")
    print(" adding_value = 42")
    format_string = "What is the answer? That is: %d"
    adding_value = 42
    input(spaces)
    print("print('format_string % adding_value') ")
    print(format_string % adding_value)

    # attribute_my_list  = dir(my_list)
    # print(getattr(my_list, attribute_my_list[0] ))


##############################################################################
# Name                  - ex3
# Parameters            - none
# Description           -
##############################################################################
def ex3():
    print("\n What this %d or just % ???? \n")
    input(spaces)

    print("1. '%d' or '%i' Signed integer decimal                                                    \n"
          "2. '%o' Unsigned octal                                                                \n"
          "3. '%u' Unsigned decimal                                                              \n"
          "4. '%x' Unsigned hexadecimal (lowercase)                                              \n"
          "5. '%X' Unsigned hexadecimal (uppercase)                                              \n"
          "6. '%e' Floating point exponential format (lowercase)                                 \n"
          "7. '%E' Floating point exponential format (uppercase)                                 \n"
          "8. '%f' F Floating point decimal format                                               \n"
          "9. '%g' Same as e if exponent is greater than –4 or less than precision, f otherwise  \n"
          "10. '%G' Same as E if exponent is greater than –4 or less than precision, F otherwise \n"
          "11. '%c' Single character (accepts integer or single character string)                \n"
          "12. '%r' String (converts any Python object using repr)                               \n")
    print("\n Well, this is easy: \n")
    input(spaces)

    print("\n I don't remember them all :( \n")
    input(spaces)
    print("\n But we are no lazy! Let's just try: \n")

    print(">>> format_string = 'If we multiply %s and %s we will have %s' ")
    format_string = "If we multiply %s and %s we will have %s"
    print(">>> format_string % (1,1,2) ")
    input(spaces)
    print(format_string % (1, 1, 2))

    input("But that has trick.... we can't use 1,1,2 without () round brackets, or ")
    print(format_string % 1, 1, 2)

    # We will return to this a few lections later :) Don't worry, I will not
    # forget.


##############################################################################
# Name                  - ex4
# Parameters            - none
# Description           -
##############################################################################
def ex4():
    print("\n We can try more? Yes! \n")

    format_string = "Integer %d \n"
    input(">>> format_string = 'Integer %d' \n>>>print(format_string % 42)")
    print(format_string % 42)
    input(spaces)

    input(">>> format_string = 'Heximal %x' \n>>>print(format_string % 42)")
    format_string = "Heximal %x \n"
    print(format_string % 42)
    input(spaces)

    input(">>> format_string = 'Octal %o' \n>>>print(format_string % 42)")
    format_string = "Octal %o \n"
    print(format_string % 42)
    input(spaces)

    input(">>> format_string = 'Float %f' \n>>>print(format_string % 42.00001)")
    format_string = "Float %f \n"
    print(format_string % 42.00001)
    input(spaces)

    input(">>> format_string = 'Converted as object %r' \n>>>print(format_string % format_string)")
    format_string = "Object %r \n"
    print(format_string % format_string)
    input(spaces)
    pass


##############################################################################
# Name                  - ex5
# Parameters            - none
# Description           - Width and Precision
##############################################################################
def ex5():
    print("\n And what about string convertion Width and Precision \n")
    print("\n>>>import pi from math")

    import math  # <--- Don't do this in functions

    print("\n>>> '%10f' % pi")
    input("Width will be 10")
    print('%10f' % math.pi)

    print("\n>>> '%10.2f' % pi")
    input("Precision will be 2")
    print('%10.2f' % math.pi)

    print("\n>>> '%-10.2f' % pi")
    input("Precision will be? And spaces?")
    print('%-10.2f' % math.pi)

    print("\n>>> '%.12s' % 'Understand this?' ")
    input("so....")
    print('%.10s' % 'Understand this?')

    input("\n And remember 'Python' * 5 ???")
    print('Python' * 5)


##############################################################################
# Name                  - ex6
# Parameters            - none
# Description           - String constants
##############################################################################
def ex6():
    print("\n String constants! \n")
    input(spaces)
    print("\nstring.digits A string containing the digits 0–9")
    print("\nstring.ascii_letters A string containing all letters (upper- and lowercase)")
    print("\nstring.ascii_lowercase A string containing all lowercase letters")
    print("\nstring.ascii_uppercase A string containing all uppercase letters")
    print("\nstring.printable A string containing all printable characters")
    print("\nstring.punctuation A string containing all punctuation characters")

    input(spaces)

    input("\n>>>string.digits\n")
    print(string.digits)

    input("\n>>>string.ascii_letters\n")
    print(string.ascii_letters)

    input("\n>>>string.ascii_lowercase\n")
    print(string.ascii_lowercase)

    input("\n>>>string.printable\n")
    print(string.printable)

    input("\n>>>string.punctuation\n")
    print(string.punctuation)

    input("\n>>>string.ascii_uppercase\n")
    print(string.ascii_uppercase)

    input(spaces)
    print(
        "\nstring.whitespace A string containing all ASCII characters that are considered whitespace. "
        "This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.")
    print(string.whitespace)
    input("\n>>>string.hexdigits - The string '0123456789abcdefABCDEF'.\n")
    input("\n>>>string.octdigits - The string '01234567'..\n")

    input(spaces)
    print("\nSo where and how we can use it??? For now remember just '.translate'\n")


##############################################################################
# Name                  - ex7
# Parameters            - none
# Description           - FIND & JOIN & REPLACE
##############################################################################
def ex7():
    print("\n FIND ? JOIN ? REPLACE\n")
    input(spaces)

    print("\nWe will start from find\n method finds a substring within a larger"
          "string. It returns the leftmost index where the substring is found."
          "If it is not found, –1")

    print("\n>>>example='I've done my homework' ")
    example = "I've done my homework"
    print("\n>>>example.find('done') ")
    print(example.find('done'))

    input(spaces)
    print("\n>>>example.find('Liar') ")
    print(example.find('Liar'))

    print("\n>>>What will be if we try to find 'o'? ")
    input(spaces)

    print("\nWhat about JOIN? - is used to join the elements of a sequence")
    print("\n>>>sequance=('I', 'love', 'Python') ")
    print("\n>>>join_string='+' ")

    join_string = "+"
    sequance = ("I", "love", "Python")

    print("\n>>>join_string.join(sequance) ")
    print(join_string.join(sequance))

    input(spaces)
    print("\nWhat about REPLACE? - method returns a string where all the occurrences "
          "of one string have been replaced by another:")

    print("\n>>>example = ' I've done my homework ' ")
    print("\n>>>example.replace('done','forget') ")
    example = "I've done my homework"
    print(example.replace('done', 'forget'))

    input(spaces)
    print("So guess what will be print if\n>>>example.replace('done','forget')\n>>>print example")


##############################################################################
# Name                  - ex8
# Parameters            - none
# Description           - SPLIT & STRIP
##############################################################################
def ex8():
    print("\n SPLIT ? STRIP\n")

    print("\nRemember JOIN? - 'Split' s inversed version of 'join' ")
    print("\n>>>split_string='I+love+Python' ")
    print("\n>>>split_string.split('+') ")

    input(spaces)
    split_string = "I+love+Python"
    print(split_string.split('+'))

    input(spaces)

    print("\nStrip method returns a string where whitespace on the left and right\n"
          "but not internally has been stripped (removed)\n\n\n")
    input("")

    print("\n>>>strip_string='         I love Python               ' ")
    print("\n>>>strip_string.strip()")
    strip_string = "                I love Python           "
    print(strip_string.strip())

    print("\n>>>strip_array=['I','love','Python'] ")
    print("\n>>>strip_search='Python' ")
    strip_array = ['I', 'love', 'Python']
    strip_search = 'Python'
    input("\n>>>if strip_search in strip_array: print ('Found it!')")
    if strip_search in strip_array: print('Found it!')

    # strip_search='Pythen'
    # if strip_search in strip_array: print ('Found it!') #<-- In such case no output


##############################################################################
# Name                  - ex9
# Parameters            - none
# Description           - TRANSLATE
##############################################################################
def ex9():
    print("\n TRANSLATE \n")
    input(spaces)

    print("Similar to replace, but translate replaces parts of a string,\n"
          "but unlike replace, translate only works with single characters.\n")
    input(spaces)
    print(">>>translate_string='I+love+Python' ")
    translate_string = "I+love+Python"

    print("maketrans() function takes two arguments: two strings of equal length,\n"
          "indicating that each character in the first string should be replaced by the\n"
          "character in the same position in the second string.\n")
    input(spaces)
    intab = "+"
    outtab = " "
    # trantab = maketrans(intab, outtab)

    print(">>>intab = '+'  ")
    print(">>>outtab = ' ' ")
    print(">>>trantab = maketrans(intab, outtab)")
    print(">>>translate_string.translate(trantab)")

    input(spaces)
    # print(translate_string.translate(trantab))


##############################################################################
# Name                  - ex10
# Parameters            - none
# Description           - String Formating
##############################################################################
def ex10():
    print("\nThe last one, but not the least - String Formating!\n")
    input(spaces)

    print("\n>>>  string_example = '{0} is better than {1}'.format('Python', 'Nothing') ")
    print("\n>>> string_example")
    string_example = "{0} is better than {1}".format("Python", "Nothing")
    print(string_example)
    input(spaces)

    print("\n 1. format  ")
    print("\n 2. vformat ")
    print("\n 3. parse    - Loop over the format_string and return an iterable of tuples")
    print(
        "\n 4. get_field   -  Given field_name as returned by parse() (see above), convert it to an object to be formatted. ")
    print("\n 5. get_value  -  Retrieve a given field value. The key argument will be either an integer or a string. ")
    print("\n 6. check_unused_args - Implement checking for unused arguments if desired. ")
    print(
        "\n 7. format_field - simply calls the global format() built-in. The method is provided so that subclasses can override it.")
    print(
        "\n 8. convert_field  - Converts the value (returned by get_field()) given a conversion type "
        "(as in the tuple returned by the parse() method). The default version understands ‘s’ (str), "
        "‘r’ (repr) and ‘a’ (ascii) conversion types.")
    input(spaces)


##############################################################################
def home():
    print('\n\n\n HOME TASK: Please provide at least one example on each String Formating\n from 8 \n\n')
    pass


##############################################################################
def fin():
    print('\n Thanks for your attention! See you all on next python lection\n')
    pass


##############################################################################
# Name                  - main
# Parameters            - argv - file name
# Created               -
# Date                  -
##############################################################################
if __name__ == "__main__":
    print("\n Today we will explain immutable data struncture - 'S T R I N G' \n")
    print(spaces)



