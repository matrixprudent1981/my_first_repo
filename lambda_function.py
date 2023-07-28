
# execise 1

# obiom_corobki = lambda a, b, c: print(f'Объем коробки = {a * b * c}')

# obiom_corobki(4, 5, 6)

# execise 2

# summa_2h_cub = lambda a, b: print(a ** 3 + b ** 3 )

# summa_2h_cub(2, 2)


#execise 3

#list_3 = [4, 5, 7, 8, 9]

# def nechetnye_odd(n):
#     if n <= 0:
#         return
#     if n % 2 != 0:
#         print(n)
#     nechetnye_odd(n - 1)

# print(nechetnye_odd(20))

# execise 4

# col_dnei_newyear = lambda a: print(f'Ostalic {365 - a} dnei')
# 
# col_dnei_newyear(90)

# execise 5

# col_let_vgodu = lambda b: print(b * 365)

# col_let_vgodu(4)

# execise 6

# dannye_list = [1,2,3,4,5]

# def udalenie_elem(test_list: list):
#     if len(test_list) == 0:
#         return
#     test_list.pop()
#     print(test_list)
#     udalenie_elem(test_list)

# udalenie_elem(dannye_list)

# execise 7


# list_dannyi = [2, 5, 20, 100, 9, 1, 6, 7, 12, 8]

# function_qwadrad = lambda i: i ** 2

# perebor_kajdogo = list(map(function_qwadrad, list_dannyi))

# print(perebor_kajdogo)

# execise 8

# function_prob = lambda i: i % 3 == 0

# even_normal = list(filter(function_prob, list_dannyi))

# print(even_normal)

#execise 9


# def sum_of_digits(n) -> int:
#     str_num = str(n)
#     len_str = len(str_num)

#     if len_str == 1:
#         return n
#     else:
#         return int(str_num[0]) + sum_of_digits(int(str_num[1:]))

# result = sum_of_digits(256)
# print(result)



# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n-1)

# result = summa(5)

# print(result)
