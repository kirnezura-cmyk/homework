from loguru import logger

LOCAL_DATABASE = dict()

#создание студентов

def local_database():
    print("========="
          "enter first student"
          "=========")

    name = input( "enter student name: ")
    age = int(input("enter student age: "))
    height = int(input("enter student height: "))
    weight = int(input("enter student weight: "))


    student = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight
    }

    LOCAL_DATABASE.update({name: student})





    print("========="
          "enter second student"
          "=========")
    name = input("enter student name: ")
    age = int(input("enter student age: "))
    height = int(input("enter student height: "))
    weight = int(input("enter student weight: "))

    student = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight
    }



    LOCAL_DATABASE.update({name: student})




    print("========="
          "enter third student"
          "=========")
    name = input("enter student name: ")
    age = int(input("enter student age: "))
    height = int(input("enter student height: "))
    weight = int(input("enter student weight: "))

    student = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight
    }



    LOCAL_DATABASE.update({name: student})

#проверка

local_database()
if len(LOCAL_DATABASE) == 3:
    print("все ученек добавлены")
else:
     print("неверное количество учеников")

# поиск студента

def search ():
  print ("========="
         "search student"
         "=========")

searchstudent = input("enter student name: ")
if searchstudent in LOCAL_DATABASE:
 logger.info(f"Студент найден: {LOCAL_DATABASE[searchstudent]}")
else:
    print("такого ученика нет")








