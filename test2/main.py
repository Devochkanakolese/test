import os
import time

while True:
    sayt = input("Введите адрес сайта")
    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
        print('elif')
    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)
        print('else')
    break
os.system("start https://www.youtube.com/")
time.sleep(5)
os.startfile("C:/Users/Professional/Desktop/рглорп")