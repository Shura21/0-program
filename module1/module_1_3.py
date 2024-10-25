#1# a=int(input('Введите число' ))
#print('Следущее за числом',a,'будет', a+1)
#print('Для числа ', a, 'предыдущее будет',a-1)
#2# Напишите программу, которая считывает целое положительное число xx и выводит на экран
# последовательность чисел x, 2x, 3x, 4x, 5x, разделённых тремя черточками.
#a=int(input('Введите число'))
#print(a,a*2,a*3,a*4,a*5,sep ='-'*3)
#3# Напишите программу, которая находит полное число метров по заданному числу сантиметров.
#a=int(input('Введите число'))
#print(a//100)
#if a<400:
#    print('метра')
#elif a>400:
#    print('метров')
#4# Напишите программу, которая определяет, разрешен пользователю доступ
# к интернет-ресурсу или нет.
#Формат входных данных
#На вход программе подаётся целое число — возраст пользователя.
#Формат выходных данных
#Программа должна вывести текст «Доступ разрешен» если возраст не менее 18,
#и «Доступ запрещен» в противном случае.
#a= int(input('введите число'))
#print('доступ разрешен') if a>=18 else print('доступ запрещен')
#5#1. Создать произвольный список
#Если все числа равны между собой, то вывести 3
#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#Если равных чисел среди 3-х вообще нет, то вывести 0
#6#print(1,2,3,end=(' '))
#print(4,5,6,sep=('+'))
#a=float(input('Ведите длину стороны квадрата:'))
#p=a*4
#print('периметр квадрата=',round(p,1))
#m=float(input('Введите ваш вес кг:'))
#h=float(input('Введите ваш раст в метрах:'))
#imt=m/h**2
#print('ваш ИМТ',round(imt,2))
#for a in range(0,10):
   # print(a)
# задача1:
# с клавиатуры вводитса 2 целых числа a и b. нужно выести все
#числа в диапозоне от а до b,а так же указать количество этих чисел
#a=int(input('Ведите первое число:' ))
#b=int(input('Введите второе число:'))
#q=0
#for a in range(a,b+1):
  #  print(a)
 #   q=q+1
#print('количество чисел', q)
# Задача 2:
# Дано вещественое число ,стоимость 1 кг конфет. вывести на экран
# стоимость 1.2....10кг конфет.
#b=float(input('Цена  за 1 кг. кофет'))
#cost=0
#for a in range(1,11):
#    cost=b*a
#    print('Стоимость',a,'кг. конфет=',cost)
from random import random


#for i in 1,2,3,4:
 #   print(i)
#for i in "Heloy":
 #   print(i)
#list_= ['one','two','fre']
#for i in list_:
#    if i == 'fre':
#        list_.remove(i)
#print(list_)
#list_= ['one','two','fre']
#for i in range(len(list_)):
#    print(list_[i])

#list_2=[2,3,4,5,1]
#sum_=0
#for i in range(len(list_2)):
#    sum_ += list_2[i]
#print(sum_)

#for i in range(1,11):# функция range принимает три параметра start.stop.step
 #   for j in range(1,11):
  #      print(f'{i}x{j}={i*j}')

#def say_hello(name): - принимаюшая функция
#    print('Hello',name)
#say_hello('shura')
#say_hello('sveta')
#say_hello('vala')

#import random #возврашаюшая функция
#def lottery():
#    tickets=[1,2,3,4,5,6,7,8,9,10]
 #   win = random.choice(tickets)
#    return win
#win=lottery()
#print(win)

#import random
#def lottery(mon,thue):
#    tickets=[1,2,3,4,5,6,7,8,9,10]
#    win1=random.choice(tickets)
#    tickets.remove(win1)
#    win2=random.choice(tickets)
#    print(mon,thue)
#    return win1, win2
#win1,win2=lottery('mon','thue')
#print(win1,win2)

def test(a=2,b=True):
    print(a, b)
test(False,'ok')
test([1,2])
test(*[1,2])
test(**[1,2])
