
# z, c , *v = [1,2,3,4,5,6]
# print(z,c,v)

# print(int(4.5),float(7))
#
# ww = 5
# if ww ==0:
#     ww += 1
# print(5/ww)
#
# qq = float(input("Введите число:"))
# if qq ==0:
#     qq ==1
# elif type(qq) == type(3) or type(qq) == type(1.2):
#     print("допустимое значение")
# else:
#     print("не допустимое значение")
#     qq == 1
# print(100/qq)
import os
import time

# while True:
#     sayt = input("Введите адрес сайта")
#     if 'https://' in sayt:
#         os.system('start ' + sayt)
#         print('if')
#     elif 'www.' in sayt:
#         sayt = 'https://' + sayt
#         os.system('start ' + sayt)
#         print('elif')
#     else:
#         sayt = 'https://www.' + sayt
#         os.system('start ' + sayt)
#         print('else')
#     break
# os.system("start https://www.youtube.com/")
# time.sleep(5)
# os.startfile("C:/Users/Professional/Desktop/рглорп")
#
import importlib
#
# def check_library(library_name):
#     try:
#         importlib.import_module(library_name)
#         print(f"The '{library_name}' library is installed.")
#     except ImportError:
#         print(f"The '{library_name}' library is not installed.")
#
# # Пример проверки наличия библиотеки 'numpy'
# check_library('time')


# while True:
#     i = int(input())
#     o = 0
#     y = 1
#
#     while o < i:
#         o += 1
#         y *= o
#     print(y)

# e = ""
#
# while len(e) < 5:
#     s = input("Ввод")
#     if s == "o":
#         continue
#     e += s
# print(e)

# r = "elert"
# count = 0
#
# for i in r:
#     if i == "e":
#         print("eeeeeeeee")
#     if i == "r":
#         continue
#     if i != "e":
#         print(i)
#     count +=1
#
# print(count)

# x = "йцукенгшщзхъёфывапролджэюбьтимсчя"
# y = input("Введите текст:")
#
# for i in x:
#     count = 0
#     for r in y:
#         if i == r:
#             count += 1
#     if count > 0:
#         print("букв", i, "было", count)

# rrr = list(range(1,21))
# sss = rrr[0::2]
# eee = []
#
# for i in rrr:
#     if i % 2 == 1:
#         continue
#     eee.append(i)
#     rrr.remove(i)
# print(eee,rrr,sss)
# spisok = []
# for adress,dirs,files in os.walk("C:\\Users\Professional\Desktop\куек"):
#     for file in files:
#         full = os.path.join(adress,file)
#         if ".mp4" in full:
#             spisok.append(full)
# print(spisok)
#
# x = (9,8,7,6,5,4,3)
# w = list(x)
# w[0]=10
# x = tuple(w)
# print(x)
#
# e = (1,2,3,4,5)
# e += 6,7,8
# print(e)

# r = 23
# inverted = 0
#
# while r != 0:
#     inverted = inverted * 10 + (r % 10) #23 % 10 = 3 Остаток от деления
#     print(inverted)
#     r //= 10 #23 // 10 = 2.3 = 2 Деление с округлением
#     print(r)
#
# s = range(0, 10)
# s = list(s)
# print(f'{len(s)}')
#
# w = 12
# d = 23
# q = 5.7
# print('{} - {} - {}'.format(d,q,w))
import re
# import main as m
# print(m.d(10))
#
# def fuck(*fuf):
#     res : int= 0 #res-переменная
#     for item in fuf:
#         res += item
#     return res
# print(fuck(1,5,5,9))
#
# def fib(n):
#     for n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)
#
# def fib1(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib1(n-1) + fib1(n-2)
#
# fib_list = []
# for e in range(0, 10):
#     fib_list.append(fib1(e))
#
# print(fib_list)

# dictionary = \
#     {
#         "left":'l',
#         "right":'r',
#         "top":'t',
#         "down":'d'
#     }
# for k in dictionary:
#     print(dictionary[k])

# def call(x):
#     return x + 10
# #print(call(10))
# def call1(x):
#     return  x * 10
# #print(call1(10))
#
# def math(op, x):
#     print(op(x))
# math(call1,10)
# math(call,10)

# sum = lambda x,y: x+y
#
# def mylt(a,b):
#     return a*b
#
# def calc(op,a,b):
#     print(op(a,b))
#     # return op(a,b)
#
# calc(sum,4,5)
# calc(lambda x,y: x+y
#      ,4,5)

# list = [(i , i) for i in range(1, 21)if i % 2 == 0]
# print(list)
#
# def f(x):
#     return x ** 3
#
# list = [(i , f(i)) for i in range(1, 21)if i % 2 == 0]
# print(list)

# path = 'C:/Users/Professional/Desktop/куек/r.txt'
# f = open(path,"r")
# data = f.read()+" "
# f.close()
#
# numbers = []
#
# while data != '':
#     space = data.index(" ") #найти пробел
#     numbers.append(int(data[:space])) #найти все что находится от 1 символа до позиции 1-го пробела, превратить это в числои добавить в список
#     data = data[space+1:] #Обновляет значение переменной data, отсекая первое число и пробел из строки
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)

li = [x for x in range(1,21)]
li = list(map(lambda x:x+10,li))
print(li)

name = "Pythonru"
type_of_site = "Блог"

print(f"{name} это {type_of_site}.")

class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f'Имя: {self.name}. Возвраст: {self.age}.'

user= Sample("Игорь", 19)
print(f"{user}")