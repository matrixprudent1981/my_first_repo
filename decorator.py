# def my_new_decorator(function_decorat):
#     def wrapper():
#         print('я код до вызова')

#         function_decorat()
#         print('я код до вызова')

#         return wrapper
    
# def hello():
#     print("я код декорирумой функции")

# decorator_hello = my_new_decorator(hello)
# decorator_hello()

# 29.06.2023

# execise 1

# def vozvedenie_qwadrat(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result ** 2
#     return wrapper


# @vozvedenie_qwadrat
# def proizvedenie_chisel(a, b):
#     return a * b

# result = proizvedenie_chisel(10, 10)
# print(result)



#execise 2

# import random

# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         print(result)
#         return result.upper()
#     return wrapper


# @uppercase_decorator
# def random_word():
#     words_list = ['apple', 'kiwi', 'banana']
#     random_word = random.choice(words_list)
#     return random_word

# result = random_word()
# print(result)


# execise 3

#  Напишите функцию которая генерирует 100 рандомных чисел 
# в диапазоне от 10 до 50 и возвращает их в листе. Напишите ДЕКОРАТОР
# для этой функции которая удалит все дубликаты в первой функции
# и вернёт всё так же лист.

# import random

# def udolit_dublikaty(func):

#     def wrapper():
#         list_of_words = func()
#         result = set(list_of_words)
#         return result
#     return wrapper


# @udolit_dublikaty

# def random_list():
#     words_list = []
#     n = 1
#     while n <= 100:
#         choice = random.choice(range(10,50))
#         words_list.append(choice)
#         n += 1
#     return ords_list

# result = random_list()
# print(result)

# execise 4


# def shifrovanie_pass_log(func):
    
#     def wrapper():
#         varianty = func()
#         log_na_vyhod = []
#         for i in varianty[0]:
#             log_na_vyhod.append(ord(i))
#         pass_na_vyhod = []
#         for j in varianty[1]:
#             pass_na_vyhod.append(ord(j))
        
#         print(f'Зашифрованый лог равен = {log_na_vyhod}   '
#               f'Зашифрованный пароль равен = {pass_na_vyhod}')

#     return wrapper()
      
        
# @shifrovanie_pass_log

# def vesty_svoy_log_pass():
    
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')

#     return login, password

#execise 5

#Cоздайте декоратор, который записывает значение оборачиваемой функции в файл.


# def raspechatka_my_file(func):

    
#     def wrapper():
#         varianty = func()
#         file = open('new_file_for_write', 'w')
#         file.write(varianty)
#         file.close
        
        
#     return wrapper()  


# @raspechatka_my_file


# def hello_my():
#     return ('Всем привет! Всем будущим бек-энд разработчикам!'
#           'Желаю всем достичь поставленных целей!')









