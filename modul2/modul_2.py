#from time import sleep
#a=5
#print(a)
#print('я тут')
#sleep(4)
#print('Фух, 4 секунду прощло')
#name=input('Ведите свое имя ')
#if name=='urban':
#    print('Здраствуй ,администратор')
#if name=='sveta':
#    print('Привет, любимая ')
#else:
#     print('Привет', name )
number=int(input('Ведите число ')) # fizz-если делится /3, bazz-если /5, fizzbuzz-если/3и5
if  number %3==0 and number %5==0:
     print('many')
elif number %3==0:
     print('free')
elif number %5==0:
     print('five')
else:
     print('long')


