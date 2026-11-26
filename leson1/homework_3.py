from loguru import logger

LOCAL_DATABASE = dict()


def local_database():
    print("enter first student")
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
    logger.info(f"Студент {name} успешно добавлен.")




    print("enter second student")
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
    logger.info(f"Студент {name} успешно добавлен.")



    print("enter third student")
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
    logger.info(f"Студент {name} успешно добавлен.")



local_database()
germanj

logger.info(f"Все 3 студента добавлены: {LOCAL_DATABASE}")














