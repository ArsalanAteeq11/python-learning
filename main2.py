# name = "Arsalan"
# print(name)

# age = 20

# if age >=20:
#     print("you are adult")
# else:
#     print("you are not adult")     


# for i in range(1,11):
#     print(i)


# LIST
my_list = ["apple","mango","banana","orange","kiwi"]
# my_list.append("grapes") {list k sb se last me elemet add krta hai}
# my_list.insert(2,"grapes") {list k andr kisi bhi index pr element add krta hai}
# my_list.remove("mango") {list k andr kisi bhi element ko remove krta hai}
# my_list.pop(1) {list k andr se kisi bhi elemet ko remove krta hai usk index se aur by default last wala remove krta hai }
# print(my_list.count("apple"))
# print(my_list.index("apple"))

# print(my_list)

# TUPLES
# numbers = (10,20,30,40,10)
# print(numbers)
# # print(numbers.index(10))
# print(numbers.count(10))


# temp_list = list(numbers)
# temp_list.append(50)
# print(temp_list)
# tup = tuple(temp_list)
# print(tup)


# DICTIONARY
# student = {"name":"ali","age": 22, "marks": 90}

# print(student.get("name")) {Key ki value return karta hai}
# print(student.keys()) {Sare keys return karta hai}
# print(student.values()) {Sare values return karta hai}
# print(student.items()) {(key, value) pairs return karta hai}
# student.update({"age":23}) {Dictionary me data update karta hai}
# student.update({"number":23}) {Dictionary me new data add karta hai}
# student.pop("age") {Given key ka element delete karta hai}
# student.popitem() {Last key-value pair delete karta hai}
# student.clear() {	Dictionary empty kar deta hai}
# student2 = student.copy() {Dictionary ki copy banata hai}
# print(student)


# SETS

# set1 = {1,2,3,4,5,9}
# set2 = {1,2,3,4,5,6,7,8}
# set1.add(6) {Set me naya element add karta hai}
# set1.remove(2) {Given element remove karta hai (Error agar element nahi mila)}
# set1.discard(7) {Given element remove karta hai (No error agar nahi mila)}
# set1.pop() {Random element remove karta hai}
# set1.clear() {Sab elements hata deta hai}
# set3 = set1.union(set2) {Do sets ko mila kar naya set banata hai}
# set3 = set1.intersection(set2) {Common elements ka set return karta hai}
# set3 = set1.difference(set2)

# print(set1)
# print(set3)



# List Comprehension (Short Way to Write Loops in Lists)
# even_number = [x*2 for x in range (1,11)]
# print(even_number)


# LAMDA FUNCTIONS

# square = lambda x : x**2
# print(square(5))

# add = lambda a,b:a+b
# print(add(5,8))

# even_or_add = lambda x : "Even" if x % 2 == 0  else "Odd"
# print(even_or_add(8))
# print(even_or_add(7))


#  {***/ MAP Function /***}
# Map function ek function ko ek puri list ke har element pe apply karta hai.
# Yeh list ka har element process karne ke liye use hota hai.


# numbers = [1,2,3,4,5]

# squared = list(map(lambda x : x**2 , numbers))
# print(squared)

# upper_case = list(map(lambda x : x.upper(), my_list))
# print(upper_case)


#{***/ FILTER Function /***}
# Yeh sirf unhi elements ko return karta hai jo condition satisfy karein.
# True wale elements ko rakh lega, false wale hata dega.

# evens = list(filter(lambda x : x%2==0,numbers))
# print(evens)

# long_words = list(filter(lambda x : len(x) > 5 , my_list))
# print(long_words)


# ZIP Function
# Zip function multiple lists ko ek sath merge karke tuples banata hai.
# Same index wale elements ko pair bana deta hai.

names = ["arsalan", "sameer","shariq"]
ages = [20,22,24]

dictionary = dict(zip(names,ages))
print(dictionary)

list = list(zip(names,ages))
print(list)

