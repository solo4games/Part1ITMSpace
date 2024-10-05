def check_positive(value):
    return value > 0


def check_not_parity(value):
    return value % 2 != 0


def check_parity(value):
    return value % 2 == 0


def check_statement_task4(a, b):
    return a > 2 and b <= 3


def check_statement_task5(a, b):
    return a >= 0 or b < -2


def check_statement_task6(a, b, c):
    return a < b < c


def check_statement_task7(a, b, c):
    return a < b < c or c < b < a


def check_statement_task8(a, b):
    return check_not_parity(a) and check_not_parity(b)


def check_statement_task9(a, b):
    return check_not_parity(a) or check_not_parity(b)


def check_statement_task10(a, b):
    parity_a = check_not_parity(a)
    parity_b = check_not_parity(b)
    return parity_a ^ parity_b


# task1
print("A > 0: ", check_positive(10))

# task2
print("A % 2 != 0: ", check_not_parity(4))

# task3
print("A % 2 == 0: ", check_positive(10))

# task4
print("A > 2 and B <= 3: ", check_statement_task4(10, 5))

# task5
print("A >= 0 or B < -2: ", check_statement_task5(-2, -4))

# task6
print("A < B < C: ", check_statement_task6(19, 11, 12))

# task7
print("B between A and C: ", check_statement_task7(12, 13, 14))

# task8
print("A % 2 != 0 and B % 2 != 0: ", check_statement_task8(4, 5))

# task9
print("A % 2 != 0 or B % 2 != 0: ", check_statement_task9(4, 6))

# task10
print("A % 2 != 0 ^ B % 2 != 0: ", check_statement_task10(5, 5))
