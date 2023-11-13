## Задание 2
"""
Выведите на экран все уникальные гео-ID из значений словаря ids.
Т.е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
"""
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# ids_extra = set(ids.values())
ids_extra = set()
for my_data in ids.values():
    # ids_extra.add(my_data)
    # ids_extra.append(set(my_data))
    # ids_extra = ids_extra | (set(my_data))        # variant 1
    ids_extra.update(set(my_data))                  # variant 2
    # print(my_data)
    # print(f'{ids_extra}\n')

print(f'\n{list(ids_extra)}')

