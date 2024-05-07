num =  (1,2,3,-6)
print(num)
print(type(num))

# output---
# (1, 2, 3, -6)

tup = ('Damodar','Girisola','Sales Executive')
print(tup)
print(type(tup))

# output---

# ('Damodar', 'Girisola', 'Sales Executive')
# <class 'tuple'>



tup_con = tuple(('Nucleya','Hardwell','Dj Snake','Afrojack'))

print(tup_con)
print(type(tup_con))

# output---

# ('Nucleya', 'Hardwell', 'Dj Snake', 'Afrojack')
# <class 'tuple'>


tuple1 = [1,2,3,4,5,6]
print(tuple(tuple1))
print(type(tuple(tuple1)))


# output---
# (1, 2, 3, 4, 5, 6)
# <class 'tuple'>


float_values = (1.2, 3.4, 2.1)
print(float_values)
print(type(float_values))

# output---

# (1.2, 3.4, 2.1)
# <class 'tuple'>

languages = ('Python','JavaScript','C++')

print(languages[0])
print(languages[1])
print(languages[2])

# Tuple Cannot be Modified---

cars = ('Nexon','Xuv 300','Punch','Xuv 700')

for car in cars:
    print(car)

print(len(cars))


# otuput---

# Nexon
# Xuv 300
# Punch
# Xuv 700
# 4



colors = ("Red","Pink","Blue")

print('Yellow' in colors)
print("Pink" in colors)
print("blue" in colors)


# output---

# False
# True
# False


# names = ('Damo','Ahuti','Sai','alekha')
# print(names)

# names[1] = 'Dar'

# print(names)

# output---

# TypeError: 'tuple' object does not support item assignment


# names = ('Damo','Ahuti','Sai','alekha')

# del names
# print(names)

# output---
# TypeError: 'tuple' object does not support item assignment



var = ('Hello')
print(var)
print(type(var))

# output---

# Hello
# <class 'str'>

var1 = ('Hello',)

print(var1)
print(type(var1))


# output---
# ('Hello',)
# <class 'tuple'>

# Tuple Methods---


vowel = ('a','r','f','w','r','x','r')

count = vowel.count('r')

print(count)

# output---
# 3

random = ('a',('a','b'),[3,4],('a','b'))

count = random.count('a')
print("The count of 'a' is :", count)

count = random.count(('a','b'))
print("\nThe count of('a','b') is: ",count)

count = random.count([3,4])
print("\nThe count of [3,4] is: ",count)

# output---
# The count of 'a' is : 1

# The count of('a','b') is:  2

# The count of [3,4] is:  1

