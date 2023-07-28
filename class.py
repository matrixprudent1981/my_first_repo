
#from datetime import date

# class Human:
    
#     def __init__(self, name, age, nation, birth_date) -> None:
#         self.name = name
#         self.age = age
#         self.nation = nation
        
#         self.birth_date = birth_date

#     def say_hello(self):
#         print("hello")

#     def say_nation(self):
#         print(f"my nation {self.nation}")
#     def say_calculat_age(self):
#         today = date.today()
#         age = today.year - self.birth_day
    
#         print(f"my age is {self.age}")





# class Dog:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def say_dog(self):
#         print(f'I {self.name} my age {self.age}')

# dog_1 = Dog('doberman', 3)
# dog_1.say_dog()

# dog_2 = Dog('ovcharka', 3)
# dog_2.say_dog()

# dog_3 = Dog('terrer', 4)
# dog_3.say_dog()

# class Phone:
#     def __init__(self, number: str, model: str) -> None:
#         self.number = number
#         self.model = model

#     def get_number(self):
#         print(f'vash nomer telefona: {self.number}')

#     def recieve_call(self, name: str):
#         print(f'vam zvonit {name}')


# telefon = Phone(number=777777777, model='iphone')
# telefon.get_number()
# telefon.recieve_call(name='Adyl')


# class Laptop:
#     def __init__(self, model: str) -> None:
#         self.model = model
#         self.ram = None
#         self.size_monitor = None
#         self.memory = None

#     def set_memory(self, memory):
#         self.memory = memory

#     def set_size_monitor(self, size_monitor):
#         self.size_monitor = size_monitor

#     def set_ram(self, ram):
#         self.ram = ram

#     def full_information(self):
#         print(f'Full information: your laptop have: {self.memory}, {self.ram}, {self.size_monitor}')

# nout = Laptop(model='acer')
# nout.set_memory(512)
# nout.set_size_monitor(41)
# nout.set_ram(4)
# nout.full_information()


# class Car:
#     def __init__(self, model: str, max_speed: int):
#         self.model = model
#         self.max_speed = max_speed

#     def upgrade_speed(self):
#         self.max_speed += 1


# bmw = Car('i3', 250)
# print(bmw.max_speed)
# bmw.upgrade_speed()
# bmw.upgrade_speed()
# bmw.upgrade_speed()
# bmw.upgrade_speed()
# print(bmw.max_speed)


# class Bancomat:
#     def __init__(self, balans: int):
#         self.balans = balans

#     def discard(self, money):
#         if money > self.balans:
#             print(
#                 f'''
#                 Вам отказано выдача наличностей!
#                 Насчету Ваш баланс меньше той суммы
#                 которой вы запросили
#                 '''
#                 )
#         else:
#             self.balans -= money

#     def cash_in(self, money):
#         self.balans += money

    
#     def ostatok_balans(self):
#         print(f'Ваш остаток на текущий момент {self.balans}')

# bankomat = Bancomat(5000)
# #bankomat.ostatok_balans()
# #bankomat.discard(500)
# #bankomat.ostatok_balans()
# #bankomat.cash_in(2000)

# bankomat.discard(8000)
# bankomat.ostatok_balans()



# 08.07.2023 Домашнее обучение классам:

class MyClass:
    def set(self, n):
        self.number = n
    def show(self):
        print(f'Pole number = {self.number}')

# a = MyClass()
# b = MyClass()

# a.set(100)
# b.set(200)

# a.show()
# b.show()

# a.number = 123
# b.number = 321


# a.show()
# b.show()
# obj = MyClass()
# print(hasattr(obj, 'number'))

# try:
#     obj.show()
# except AttributeError: 
#     print('Polia y obj not!')

# obj.number = 123
# print(hasattr(obj, 'number'))

# obj.show()
# obj.set(321)

# obj.show()

# book1.chek_out()

#book1.chek_in()

print('I kan and\nbeleave')