my_dict = {'oneus_luna': {1, 2, 3, 'miss'}, 'bts_run': (0, 0, 0, 0)}  # даже множество включила в словарь
print(my_dict)
print(my_dict.get('bts_run'))
print(my_dict.get('lay_lit', 'be careful bro'))  # вывод значения, по ключу которого нет с заданным текстом вместо 'None'
my_dict['lay_lit'] = 200601   # запросим элмент которого нет
print(my_dict)   # при выводе пара была добавлена в словарь
my_dict.update({'seventeen_hit': 190805, 'bibi_vengeance': 221118})
print(my_dict)
my_dict_1 = my_dict.pop('seventeen_hit') # del_ - не сработала у меня, пошла через .pop
print(my_dict_1)  # значение из удаленной пары
print(my_dict)  # словарь без удаленного элемента

my_set = {'oneus_luna', 1, 2, 3, 'm', 'i', 's', 's', 'bts_run', (0, 0, 0, 0)}  # словарь в множество не включается?
print(my_set)
my_set.add('nct_boss') # только для одного элемента
my_set.update({'nct_boss', 3.14})
print(my_set) # добавила два новых значения с разными типами в рамках множества
my_set.discard((0, 0, 0, 0))
print(my_set)



