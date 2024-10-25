example = "Топинамбур"
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1:10:2])
immutable_var=['apple', 'orenge', 100,200]
print(immutable_var)
immutable_var[2]='peach'#замена списка с помошью []
print(immutable_var)
immutable_var.append('day')# добавление слов в конец строки
print(immutable_var)
immutable_var.extend(['string',2])#
print(immutable_var)
immutable_var.remove('orenge')#убирание из списка слов
print(immutable_var)
print('apple' in immutable_var)# смотрит есть ли слово из списка
print('apple'not in immutable_var)#сморит остался ли это слово из списка
print(immutable_var[0:-1:2])
tuple_=([1,2],0)+(1,2)#сожение строк(кортеджей)
print(tuple_)
tuple_[0][0]=23# изменение внутри кортеджа
print(tuple_)