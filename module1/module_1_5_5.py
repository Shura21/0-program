immutable_var ='apple','day',100,200,True,'list'
print(immutable_var)
#immutable_var['day']= 'new day'# так как day находится в неизменяем кортеже .
imutable_list=['apple','day',100,200,True,'list']
imutable_list[1]=2024
print(imutable_list)
imutable_list.append('big bos')
print(imutable_list)
imutable_list.extend('string')
print(imutable_list)
imutable_list.remove(200)
print(imutable_list)