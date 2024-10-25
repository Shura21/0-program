my_dirt={'ruslan':1991,'liza':1996,}
print(my_dirt)
print(my_dirt['liza'])
print(my_dirt)
my_dirt['roma']=2017
print(my_dirt.get('vitalik', 'номер отсутствует '))
print(my_dirt)
my_dirt.update({'egor':2019,
                'mark':2023})
print(my_dirt)
del my_dirt['egor']
print(my_dirt)
print(my_dirt.keys())
my_set={10,11,12,13,14,15,11,12,13,14}
print(my_set)
my_set.add('apple')
my_set.add('book')
my_set.discard(15)
print(my_set)
