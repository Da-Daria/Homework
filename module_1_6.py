# Работа со словарями
my_dict = {'Dan' : 1.75, 'Maria' : 1.68, 'Elli' : 1.82}
print (my_dict)
print(my_dict['Maria'])
print(my_dict.get('Phill'))
my_dict.update({'Maddie' : 1.59,
                'Sam' : 1.90})
val = my_dict.pop('Dan')
print(val)
print(my_dict)

#  Работа с множествами
my_set = {6, 6, 4, 3, 3, 3, 9, 9, 'tea', 'apple', 'tea'}
print(my_set)
my_set.add(7)
my_set.add('fall')
my_set.discard(3)
print(my_set)