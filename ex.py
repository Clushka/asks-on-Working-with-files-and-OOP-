# task1


# # create new file
# import os
# os.mkdir("folder")

# # delete
# import os
# # os.rmdir("example")

# # change
# import os
# os.mkdir("example")
# os.mkdir("folder")
# os.chdir("example")
# print (os.getcwd())

# # read
# import os
# print(os.listdir())


# task2

# lst_int = []
# num = int(input())

# for n in range(num):
#     numbers = int(input())
#     lst_int.append(numbers)

# print("Sum of elements in given list is :", sum(lst_int))


# task3

# str_list = ['3', '5', '1', '10', '23']

# def str_to_int(func):
#     def wrapper(*args):
#         print(str_list)
#         print("It's converting...")
#         func(*args)
#     return wrapper

# @str_to_int
# def conv_func(str_list):
#     str_list = list(map(int, str_list))
#     print("Modified list is : " + str(str_list))

# conv_func(str_list)


# task4
# class Shape:
#     def __init__(self, shirina, dlina):
#         self.shirina = shirina
#         self.dlina = dlina

#     def perim(self):
#         print(self.shirina+self.shirina+self.dlina+self.dlina)

#     def area(self):
#         print(self.dlina*self.shirina)

# class Rectangle(Shape):

#     def __init__(self, shirina, dlina):
#         self.shirina = shirina
#         self.dlina = dlina
# Pryamougolnik = Rectangle(5, 1)

# #Inheritance

# Pryamougolnik.perim()
# Pryamougolnik.area()







