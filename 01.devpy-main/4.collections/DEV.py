# кол-во поисковых запросов из 1го слова, 2ух и тд

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
sum_dict_extra = {3: 3}


for q in queries:
		# получаем количество слов в текущей строке
		w_count = q.count(' ')+1
		# помещаем в контрольный сэт значение
		control_set.update(set({w_count}))
		
		# if индекс словарика равен q.count(' ')+1,
		for my_id in sum_dict_extra.values():
				if my_id == w_count:
						# в вэлью с данным индексом пишем вэлью + q.count(' ')+1
						sum_dict_extra.setdefault(my_id, w_count)
				else:
						# добавляем новый элемент словарика с индексом = q.count(' ')+1 и вэлью = q.count(' ')+1
						print(w_count)
		sum_dict_extra.update({w_count: w_count})

print(f'\nКоличество айтемов queries: {len(queries)}')
print(f'Сет контрольных значений количества слов: {control_set}')

print(f'Дикшинари Финального результата: {sum_dict_extra}')






# a = 0
# control_set = set()
# list1 = []
# count = 0
# for q in queries:
# 		# print(q.count(' ')+1)
# 		# for index, value in enumerate(list1):
# 		# 		if value == q.count(' ')+1:
# 		# 				list1[index] = value + q.count(' ')+1
# 		list1.append(q.count(' ')+1)
# 		if set({q.count(' ')+1}) & control_set:
# 				a += q.count(' ')+1
#
# 		control_set.update(set({q.count(' ')+1}))
#
# 		count += 1
#
# print(control_set)
# print(list1)
# print(a)
#
#
# my_list = ['apple', 'banana', 'orange', 'grape']
# for index, value in enumerate(my_list):
# 		if value == 'orange':
# 				my_list[index] = 'melon'
# print(f'\n{my_list}')  # Вывод: ['apple', 'banana', 'melon', 'grape']