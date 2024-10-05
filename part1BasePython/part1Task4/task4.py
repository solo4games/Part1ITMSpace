start_list = [1, 2, 3, 4, 5]


def get_list_items(start_list):
    return start_list[0], start_list[2], start_list[:3]


def change_city_name(bad_name):
    bad_name_str = ','.join(bad_name)

    return bad_name_str.replace('+', '-').split(',')

# def change_city_name(bad_name):
#     for i in range(len(bad_name)):
#         if bad_name[i] == '+':
#             bad_name[i] = '-'
#
#     return bad_name


def split_list(start_list):
    only_letters = []
    only_numbers = []
    for element in start_list:
        if element.isdigit():
            only_numbers.append(element)
        else:
            only_letters.append(element)

    return only_letters, only_numbers


def change_letter_list(letter_list: list):
    letter_list.pop()
    print("List after deleting last element", letter_list)
    letter_list.reverse()
    return letter_list


# task1
first_item, third_item, cut = get_list_items(start_list)
print(f"First item: {first_item}, Third item: {third_item}, Cut: {cut}")

# task2
bad_name = ['Ростов', '+', 'на', '-', 'Дону']
print("Good Name", change_city_name(bad_name))

# task3
start_list = ['a', 's', '1', 'a', '32', '23']
only_letters, only_numbers = split_list(start_list)
print(f"Only Letters: {only_letters}, Only Numbers: {only_numbers}")

# task4
print("Reversed Letter list: ", change_letter_list(only_letters))

# task5
print("From List to Set: ", set(start_list))

