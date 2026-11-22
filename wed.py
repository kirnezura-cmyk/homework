def get_number():
    multipli = input("Enter a multiplication number: ")

    if multipli.isdigit():
        return int(multipli)  # Если всё верно — отдаём число
    else:
        print("Не то! Попробуй ещё раз.")
        return get_number()  # Если ошибка — возвращаем обратно в начало этой же функции


# Запускаем функцию и получаем проверенное число
multipli = get_number()

Thislist = input("Введите элементы через пробел: ")
Then = Thislist.split()

print(multipli)
print(Then)
