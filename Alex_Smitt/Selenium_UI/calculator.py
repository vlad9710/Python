def calc():
    def get_input():
        while True:
            try:
                num_1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Введенные данные не корректны. Введите число")

        while True:
            op = str(input("\nКакую операцию хотите выполнить? "))
            if op in ["*", "/", "+", "-"]:
                break
            else:
                print("Вы ввели некорректное действие")

        while True:
            try:
                num_2 = int(input("\nВведите второе число: "))
                break
            except ValueError:
                print("Введенные данные не корректны. Введите число")

        return num_1, op, num_2

    num_1, op, num_2 = get_input()

    match op:
        case "*":
            result = num_1 * num_2
            print(int(result))
        case "/":
            try:
                result = num_1 / num_2
                print("\nРезультат операции : " + str(round(result, 3)))
            except ZeroDivisionError:
                print("\nНа ноль делить нельзя")
                calc()
        case "+":
            result = num_1 + num_2
            print(int(result))
        case "-":
            result = num_1 - num_2
            print(int(result))
    retry()


def retry():
    cont = str(
        input("\nХотите выполнить операцию еще раз? Введите '+' если хотите продолжить или '-' чтобы завершить работу"))
    match cont:
        case "+":
            calc()
        case "-":
            exit()
        case _:
            retry()

calc()