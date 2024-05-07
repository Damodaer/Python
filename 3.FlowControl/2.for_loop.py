# languages = ["Python","JavaScript","Go"]

# for i in languages:
#     print(i)


# Pro_language = "Python"

# for x in Pro_language:
#     print(x)

# for Loop with Python range---

# for i in range(4):
#     print(i)


# digits = [0,1,2,3,4]

# for i in digits:
#     print(i)
# else:
#     print("No item left.")

# languages = ['Swift','Python','Go']

# for language in languages:
#     print('Hi')

# for i in range(2):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")

# sum = 0

# for num in range(101):
#     sum += num
# print(sum)


# sum = 10

# for num in range(101):
#     sum += num
# print(sum)

# Python For Loop with Dictionary---

# print('Dictionary Iteration')

# d = dict()

# d['xyz'] = 123
# d['abs'] = 456
# for i in d:
#     print("%s %d" %(i, d[i]))

# d = dict()

# d['ABC'] = 102030
# d['XYZ'] = 405060

# for i in d:
#     print("%s %d" % (i, d[i]))

# Python For Loop with a step size---

# for i in range(0,10,2):
#     print(i)

# for i in range(2,12,4):
#     print(i)

# for i in range(2,16,4):
#     print(i)

# for i in range(1,4):
#     for j in range(1,4):
#         print(i, j)

# for i in range(10,100):
#     for j in range(10,100):
#         print(i, j)

# Python For Loop with a step size---

# fruits = ["Apple","Mango","Cherry"]
# colors = ["Red","Yellow","Green"]
# for fruit,color in zip(fruits,colors):
#     print(fruit, "is", color)

# names = ["Ahuti","Sawapna"]
# genders = ["Male","Female"]

# for name,gender in zip(names,genders):
#     print(name,"Is",gender)

print("Popular Car Brands Popular Cars")
brands = ["Tata","Mahindra","Suzuki","Skoda"]
cars = ["Punch","Thar","Alto","Kushaq"]

for brand,car in zip(brands,cars):
    print(brand,"Popular car is",car)