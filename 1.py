numbers_list = []

def add_number(num):
    if num in numbers_list:
        print("Это число уже есть в списке.")
    else:
        numbers_list.append(num)
        print("Число добавлено в список.")

def remove_number(num):
    numbers_list[:] = [x for x in numbers_list if x != num]
    print("Все вхождения числа удалены из списка.")

def show_list(reverse=False):
    if reverse:
        print(numbers_list[::-1])
    else:
        print(numbers_list)

def check_value(num):
    if num in numbers_list:
        print("Значение присутствует в списке.")
    else:
        print("Значение отсутствует в списке.")

def replace_value(old_num, new_num, replace_all=False):
    if replace_all:
        numbers_list[:] = [new_num if x == old_num else x for x in numbers_list]
    else:
        try:
            index = numbers_list.index(old_num)
            numbers_list[index] = new_num
        except ValueError:
            print("Значение для замены не найдено.")

while True:
    print("Меню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Показать содержимое списка в обратном порядке")
    print("5. Проверить есть ли значение в списке")
    print("6. Заменить значение в списке")

    choice = input("Выберите действие (1-6): ")

    if choice == '1':
        num = int(input("Введите число для добавления: "))
        add_number(num)
    elif choice == '2':
        num = int(input("Введите число для удаления: "))
        remove_number(num)
    elif choice == '3':
        show_list()
    elif choice == '4':
        show_list(reverse=True)
    elif choice == '5':
        num = int(input("Введите число для проверки: "))
        check_value(num)
    elif choice == '6':
        old_num = int(input("Введите значение для замены: "))
        new_num = int(input("Введите новое значение: "))
        replace_all = input("Заменить все вхождения? (да/нет): ").lower() == 'да'
        replace_value(old_num, new_num, replace_all)
    else:
        print("Некорректный выбор. Попробуйте еще раз.")