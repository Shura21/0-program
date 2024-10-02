first=int(input('Введите первое число'))
secod=int(input('Ведите второе число'))
third=int(input('Ведите трете число'))
if first==secod and first==third:
    print(third)#Если все числа равны между собой, то вывести 3
elif first==secod or first==third or secod==third:
    print(2)#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print(0) #Если равных чисел среди 3-х вообще нет, то вывести 0
