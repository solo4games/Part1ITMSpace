personal_dict = {'name': 'Andrey',
                 'age': 22,
                 'gender': 'male',
                 'height': 188,
                 'weight': 115,
                 'foot size': 45}

def print_personal_dict(personal_dict):
    for key in personal_dict:
        print(f'{key}: {personal_dict[key]}')


print_personal_dict(personal_dict)

personal_dict['foot size'] = 50
print_personal_dict(personal_dict)
personal_dict.pop('age')
print_personal_dict(personal_dict)