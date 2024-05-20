class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Стек пустой")

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Стек пустой")


stack = Stack()

while True:
    print("""
    1. Поместить строку в стек
    2. Вытащить строку из стека
    3. Подсчет количества строк в стеке
    4. Проверка, пустой ли стек
    5. Очистка стека
    6. Получение значения без выталкивания верхней строки из стека
    7. Выход
    """)

    choice = int(input("Введите номер операции: "))

    if choice == 1:
        item = input("Введите строку: ")
        stack.push(item)
    elif choice == 2:
        print("Извлечена строка:", stack.pop())
    elif choice == 3:
        print("Количество строк в стеке:", stack.count())
    elif choice == 4:
        print("Стек пустой:", stack.is_empty())
    elif choice == 5:
        stack.clear()
        print("Стек очищен")
    elif choice == 6:
        print("Значение верхней строки в стеке:", stack.peek())
    elif choice == 7:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите существующую операцию.")