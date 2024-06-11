# num =  (1,2,3,-6)
# print(num)
# print(type(num))

# # output---
# # (1, 2, 3, -6)

# tup = ('Damodar','Girisola','Sales Executive')
# print(tup)
# print(type(tup))

# # output---

# # ('Damodar', 'Girisola', 'Sales Executive')
# # <class 'tuple'>



# tup_con = tuple(('Nucleya','Hardwell','Dj Snake','Afrojack'))

# print(tup_con)
# print(type(tup_con))

# # output---

# # ('Nucleya', 'Hardwell', 'Dj Snake', 'Afrojack')
# # <class 'tuple'>


# tuple1 = [1,2,3,4,5,6]
# print(tuple(tuple1))
# print(type(tuple(tuple1)))


# # output---
# # (1, 2, 3, 4, 5, 6)
# # <class 'tuple'>


# float_values = (1.2, 3.4, 2.1)
# print(float_values)
# print(type(float_values))

# # output---

# # (1.2, 3.4, 2.1)
# # <class 'tuple'>

# languages = ('Python','JavaScript','C++')

# print(languages[0])
# print(languages[1])
# print(languages[2])

# # Tuple Cannot be Modified---

# cars = ('Nexon','Xuv 300','Punch','Xuv 700')

# for car in cars:
#     print(car)

# print(len(cars))


# # otuput---

# # Nexon
# # Xuv 300
# # Punch
# # Xuv 700
# # 4



# colors = ("Red","Pink","Blue")

# print('Yellow' in colors)
# print("Pink" in colors)
# print("blue" in colors)


# # output---

# # False
# # True
# # False


# # names = ('Damo','Ahuti','Sai','alekha')
# # print(names)

# # names[1] = 'Dar'

# # print(names)

# # output---

# # TypeError: 'tuple' object does not support item assignment


# # names = ('Damo','Ahuti','Sai','alekha')

# # del names
# # print(names)

# # output---
# # TypeError: 'tuple' object does not support item assignment



# var = ('Hello')
# print(var)
# print(type(var))

# # output---

# # Hello
# # <class 'str'>

# var1 = ('Hello',)

# print(var1)
# print(type(var1))


# # output---
# # ('Hello',)
# # <class 'tuple'>

# # Tuple Methods---


# vowel = ('a','r','f','w','r','x','r')

# count = vowel.count('r')

# print(count)

# # output---
# # 3

# random = ('a',('a','b'),[3,4],('a','b'))

# count = random.count('a')
# print("The count of 'a' is :", count)

# count = random.count(('a','b'))
# print("\nThe count of('a','b') is: ",count)

# count = random.count([3,4])
# print("\nThe count of [3,4] is: ",count)

# # output---
# # The count of 'a' is : 1

# # The count of('a','b') is:  2

# # The count of [3,4] is:  1




# tuple1 = ()
# print("Initial empty tuple: ")
# print(tuple1)

# tuple1 = ("Damodar","Sahu")
# print("\nnTuple with the use of string: ")
# print(tuple1)

# list1 = [1,2,3,4,5,6]
# print("\nTuple using List: ")
# print(tuple(list1))



# tuple1 = tuple('Damodar')
# print("\nTuple with the use pf function: ")
# print(tuple1)

# Creating a Tuple---
# with Mixed Datatype---

# tuple1 = (3, 'Damodar', 7, 'Sahu')
# print("\nTuple with Mixed Datatypes: ")
# print(tuple1)

# Creating a Tuple---
# with nested tuples---

# tuple2 = (0,1,2,3)
# tuple3 = ('Python','Numbers')
# tuple4 = (tuple2,tuple3)
# print("\nTuple with Nested Tuples: ")
# print(tuple4)

# Creating a Tuple---
# with repetition---

# tuple1 = ('Damodar ') * 3
# print("\nTuple with repetition")
# print(tuple1)

# tuple1 = ('Damodar ') * -3
# print("\nTuple with repetition")
# print(tuple1)

# Creating a Tuple---
# with the use of loop---

# tuple = ('Damodar Sahu')
# n = 10

# print("\Tuple with a loop")
# for i in range(int(n)):
#     tuple = (tuple,)
#     print(tuple)


# tuple = ('Damodar sahu')
# n = 5

# print("\nTuple with a loop")
# for i in range(int(n)):
#     print(tuple)

# Accessing Tuple---
# with Indexing---

# tuple1 = tuple("Damodar")
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])
# print(tuple1[3])
# print(tuple1[4])
# print(tuple1[5])
# print(tuple1[6])

# Tuple unpacking---
# tuple1 = ("Damodar", "For", "Swapna")
# a,b,c =  tuple1
# print(a)
# print(b)
# print(c)

# Concatenation of tuples---

# tuple1 = (0,1,2,3,4)
# tuple2 = ("Damodar", "Loves", "Swapna")

# tuple3 = tuple1 + tuple2
# print(tuple3)

# Slicing of a Tuple---
# tuple1 = ("Damodarsahu")
# print("\nRemove of first Element: ")
# print(tuple1[1:])

# print("\nTuple after sequence of Element is reversed: ")
# print(tuple1[::-1])

# print("\nPrinting elements between Range 4-9: ")
# print(tuple1[4:9])

word = (True,False)
print(all(word))

word1 = (False,True)
print(all(word1))

word2 = (True,True,True,False)
print(all(word2))

num = [1,2,3]
print(all(num))

num1 = [1,2,-3,5]
print(all(num1))

# All elements of tuple are true
t = (2, 4, 6)
print(all(t))
 
# All elements of tuple are false
t = (0, False, False)
print(all(t))
 
# Some elements of tuple
# are true while others are false
t = (5, 0, 3, 1, False)
print(all(t))
 
# Empty tuple
t = ()
print(all(t))