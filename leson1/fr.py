from os import name
from unittest import result


def getmulti():
    multiplier = input("Enter a number: ")
    if multiplier.isdigit():
        print("good")
        return int(multiplier)
    else:
        print("error")
        return getmulti()
if name == '__main__':
    getmulti()

def Newlist():
    MList = input("Enter a list: ")
    if MList.isdigit():
        print("good")
        return int(MList)
    else:
        print("error")
        return Newlist()

result = [int(x) for x in MList.split()]
return result


def multiplication(multiplier, result):
        Dlist = [x * multiplier for x in result]
        print(Dlist)

m = getmulti()
lst = Newlist()

mult=(m, lst)

#недороботаная часть хочу сделоть проверку в функцыи создание листа

#def probing(MList):
    #if MList.isdigit():
      #  print("good")
      #  return int(MList)
  #  else:
   #     print("error")
  #      return MList
