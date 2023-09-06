# Напишите функцию для транспонирования матрицы

# def transp_matrix(matrix):
#     if not matrix:     # проверка на пустую матрицу
#         return []
    
#     rows = len(matrix)    # определение количества строк и солбцов
#     cols = len(matrix[0])

#     transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]  # создание пустой матрицы

#     for i in range(rows):     # транспонирование элементов
#         for j in range(cols):
#             transposed_matrix[j][i] = matrix[i][j]
#     return transposed_matrix

# matrix_1 = [[1, 15, 30, 13], [41, 45, 60, 25], [74, 48, 90, 14], [12, 50, 63, 2]]
# matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed_1 = transp_matrix(matrix_1)
# transposed_2 = transp_matrix(matrix_2)
# print(transposed_1)
# print(transposed_2)

############################################################################################

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

# def crate_arg_dict(**kwargs):
#     arg_dict = {}
#     for key, value in kwargs.items():
#         if not isinstance(key, (int, float, str, tuple, frozenset)):
#             key = str(key)
#         arg_dict[value] = key
#     return arg_dict


# arguments = crate_arg_dict(name = 'Света', age = '40', city = 'Москва')
# print(arguments)


###########################################################

def atm():
    balance = 0
    total_withdrawn = 0
    total_deposited = 0
    operations_counter = 0

    while True:
        print("Доступные действия:")
        print("1 - Пополнить счет")
        print("2 - Снять со счета")
        print("3 - Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":  # Пополняем счет
            deposit_amount = int(input("Введите сумму пополнения (кратную 50): "))

            if deposit_amount % 50 != 0:
                print("Сумма пополнения должна быть кратной 50.")
                continue

            if balance >= 5000000:  # Проверяем превышение суммы в 5 миллионов
                deposit_amount -= deposit_amount * 0.1  # Удерживаем налог на богатство

            balance += deposit_amount
            total_deposited += deposit_amount

            operations_counter += 1
            if operations_counter % 3 == 0:  # Проценты после каждой третьей операции
                balance += balance * 0.03

        elif choice == "2":  # Снимаем со счета
            withdrawal_amount = int(input("Введите сумму снятия (кратную 50): "))

            if withdrawal_amount % 50 != 0:
                print("Сумма снятия должна быть кратной 50.")
                continue

            if withdrawal_amount > balance:  # Проверяем достаточность средств
                print("Недостаточно средств на счете.")
                continue

            if balance >= 5000000:  # Проверяем превышение суммы в 5 миллионов
                withdrawal_amount += withdrawal_amount * 0.015  # Удерживаем комиссию

            balance -= withdrawal_amount
            total_withdrawn += withdrawal_amount

            operations_counter += 1
            if operations_counter % 3 == 0:  # Проценты после каждой третьей операции
                balance += balance * 0.03

        elif choice == "3":  # Выходим из программы
            print("Выход из программы.")
            break

        else:
            print("Недопустимый выбор. Повторите попытку.")

        print("Текущий баланс: ", balance)
        print()

    print("Итоговый баланс: ", balance)
    print("Всего пополнено: ", total_deposited)
    print("Всего снято: ", total_withdrawn)

atm()