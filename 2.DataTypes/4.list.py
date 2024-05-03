# list = ["Damo","dar","Sahu"]
# print(list)

# em_list = []
# print("Blank list: ")
# print(em_list)
# print(type(em_list))

# num = [10, 54, 40,]
# print("\nList of Numbers: ")
# print(num)

# var = ["Odisha","Ganjam","Berhampur"]
# print("\nList of Names: ")
# print(var)

# duplicate elements---

# List = [1,2,3,4,5,6,7,5,4,6,6,5,5]
# print("\nList with the use of Numbers: ") 
# print(List) 

# mixed type of values

# List2 = [1, "Damodar", 3,"AHuti",5,"Sahu"]
# print("\nList with the use of Mixed Values: ") 
# print(List2)

# Accessing elements from list---

# names = ["Ahuti","Damodar","Sai","Alekha","Loku"]
# print(names)
# print(len(names))
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[-1])
# print(names[-2])
# print(names[-3])
# print(names[-4])
# print(names[-5])



# Nesting list---

# name_list =  [["Santinagar","girisola","surola road"],["junction"]]

# print(name_list)
# print("\nAccessing a element from Nested List: ")
# print(name_list[1])
# print(name_list[0][1])
# print(name_list[1][0])


# Change List Items---

# colors = ["Pink", "Blue", "Red"]
# print("original List: ", colors)

# colors[2] = "Green"
# print("Updated List: ", colors)

# Python has many useful list methods that make it really easy to work with lists.---

# Taking Input of a Python List---

# x = 'xyz'

# result = list(x)
# print(result)

# num = input("Enter what you want to show to you")

# print(num)


# string = input("Enter elements (Space-Separated):")

# lst = string.split()
# print('The list is:',lst)


# name = input("Enter Names (Space-Separated):")

# name_list = name.split()
# print('The names is: ',name_list)

# bikes = input("Enter Bike's Name's :")

# name_bike = bikes.split()
# print("The Bike's List: ",name_bike)



# Add Elements to a Python List---

# fruits = ['Apple', 'Orange', 'Jack']
# print('Original list:', fruits)

# fruits.append('Mango')
# print('Updated List: ',fruits)

# animals = ['Dog', 'Cat', 'Cow']

# wild_animals = ['Tiger', 'Fox']

# animals.append(wild_animals)
# print(animals)

# The insert() method adds an element at the specified index. For example,---

# fruits.insert(2, 'Straberry')   
# print('Another update List', fruits)

# name = ["D","a","m","o","d","r"]
# print(len(name))
# name.insert(5,"a")
# print(name)

# prime_numbers = [2,3,5,7,]

# # insert 11 at index 4
# prime_numbers.insert(4,11)
# print(prime_numbers)

# mixed_list = [{1,2},[5,6,7]]
# add_tuple = (3,4)

# mixed_list.insert(1,add_tuple)

# print(mixed_list)

# mixed_name = [{"Damo"},["Sahu"]]
# add_string = ("Dar")

# mixed_name.insert(1,add_string)

# print(mixed_name)


# Python List extend()---

# number1 = [1,2,3]
# number2 = [4,5,6]

# number1.extend(number2)

# print(f"number1 = {number1}")
# print(f"number2 = {number2}")


# first_name = ["Damodar"]
# last_name = ["Sahu"]


# first_name.extend(last_name)
# print(f"Full name = {first_name}")

# languages1 = ["Hindi","English"] 
# language2 = ["Odia","Telugu"]

# language2.extend(languages1)
# print('Speaking Languages: ',language2)

# brands = ["Tata","Mahindra"]
# print(brands)

# brands_tuple = ("Suzuki","Hyundai","kia")
# brands.extend(brands_tuple)
# print("\nUpdated List: ",brands)

# brands_set = {"Skoda","Volkwagen","BMW","Audi"}
# brands.extend(brands_set)
# print(brands)

# Python extend() Vs append()---

# a = [1,2,3]
# b = [1,2,3]
# c = (4,5)

# # add items of b to the a list
# a.extend(c)
# print(a)

# # add b itself to the a list
# a.append(c)
# print(a)

# Remove an Item From a List---

# num = [1,2,3,4,5]
# print(num)

# num.remove(4)
# print(num)

# var = ["Damo", "Dar", "Sahu"]
# print('Orginal List',var)

# var.remove('Dar')
# print('\nUpdated List: ',var) 

# output:
# [1, 2, 3, 4, 5]
# [1, 2, 3, 5]
# Orginal List ['Damo', 'Dar', 'Sahu']

# Updated List:  ['Damo', 'Sahu']  


# Iterating Through a List---

# students = ["Ahuti", "Damodar", "Silu", "Popun"]

# for student in students:
#     print(student)

# output:
# Ahuti
# Damodar
# Silu
# Popun
 
# gadgets = ["Mobile", "Laptop", "KeyBoard", "Mouse"]

# for gadget in gadgets:
#     print(gadget) 


# Python List pop()---

# num = [1,2,3,4,5]
# remove_num = num.pop(2)

# print('Removed Element',remove_num)
# print('Updated List',num)

# output---
# Removed Element 3
# Updated List [1, 2, 4, 5]


# name = ["Damodar", "Dar", "Sahu"]
# remove_name = name.pop(1)

# print('Remove Word: ',remove_name)
# print("Updated Name: ",name)

# output---
# Remove Word:  Dar
# Updated Name:  ['Damodar', 'Sahu']  

# languages = ["Python", "JavaScript", "C++", "Hindi","C"]
# remove_languages = languages.pop(3)

# print(remove_languages,languages)
# print(languages)

# output--
# Hindi ['Python', 'JavaScript', 'C++', 'C']
# ['Python', 'JavaScript', 'C++', 'C']

# data_types = ["String","Number","List","Tuple","Set","Dist","Telugu"]

# # remove and return the last item
# print('When index is not passed:')
# print('\nRemoved Element: ',data_types.pop())
# print('Updated List: ',data_types)

# # remove and return the last item
# print('\nWhen -1 is passed: ')
# print('\nRemoved Element: ',data_types.pop(-1))
# print('Updated List: ',data_types)

# # remove and return the third last item
# print('\nWhen -3 is passed: ')
# print('\nRemoved Element: ',data_types.pop(-3))
# print('Updated List: ',data_types)

# output---
# When index is not passed:

# Removed Element:  Telugu
# Updated List:  ['String', 'Number', 'List', 'Tuple', 'Set', 'Dist']

# When -1 is passed:

# Removed Element:  Dist
# Updated List:  ['String', 'Number', 'List', 'Tuple', 'Set']

# When -3 is passed:

# Removed Element:  List
# Updated List:  ['String', 'Number', 'Tuple', 'Set']


# Python List clear()---
# students = ['Damo','Dar','sahu']

# students.clear()
# print(students)

# lst = [{1,2},('w'),[1.1,2.4,4.1]]

# lst.clear()
# print(lst)


# lst = [{1,2},('w'),[1.1,2.4,4.1]]    #error

# lst.clear(2)
# print(lst)


# lst = [{1,2},('w'),[1.1,2.4,4.1]]    #error

# lst.clear(('w'))
# print(lst)

# Python List count()---

# duplicate_names = ['Damo','sai','alekha','loku','pintu','alekha','pintu','pintu','pintu']

# check = duplicate_names.count('pintu')

# print(duplicate_names)
# print('\nThe Duplicate Name is: ',check)



random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

count = random.count(('a', 'b'))
print("The count of ('a', 'b') is: ", count)

count = random.count([3, 4])
print("The Count of [3, 4] is: ", count)