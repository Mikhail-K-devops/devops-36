## Задание 3
"""
Дан список поисковых запросов. Получить распределение количества слов в них.
Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
"""

def inc(word_count):
    word_count = set({word_count+1})
    return word_count

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'eda'
    ]

control_set = set()
sum_dict = {}
sum_dict_extra = {}

countx = 0
count = 0

for q in queries:
   # sum_dict.update({count: q.count(' ') + 1})
    word_count = inc(q.count(' '))

  # control_set.update({q.count(' ') + 1})
    control_set.update(word_count)
    # if (q.count(' ') + 1): #& count_set:
    #     sum_dict_extra.update({q.count(' ') + 1: (count + q.count(' ') + 1)})
    if word_count & control_set:
        print(f'set1 & set2: {word_count & control_set} {control_set}')
        control_set.pop()
        value = int(list(word_count)[0])
        countx = value
        sum_dict_extra.update({value: countx+value})
                                                        # sum_dict_extra[int(next(iter(word_count)))]
      # count = sum_dict_extra('value')

        count += 1
# print(f'xx: {int(next(iter(control_set)))}')
print(f'\nКоличество айтемов queries: {len(queries)}')
print(f'Сет контрольных значений количества слов: {control_set}')

print(f'Дикшинари Финального результата: {sum_dict_extra}')
# print(sum_dict)

