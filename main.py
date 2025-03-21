# class student :
#     def __init__(self,name,id):
#       self.name = name
#       self.usman = id

# class student2(student) : 
#    def __init__(self, name, id):
#       super().__init__(name, id)      
#       print(f"name :{self.name} and id: {self.usman} ") 

# s1 = student2("jerry",21)

# inheritance
# class anmial :
#     def color(self) :
#         self.name = "jerry"
#         print("this is a animal class")
# class dog(anmial) :
#     def bark(self) :
#         print(f"{self.name} bhaooo bhaooo  ")

# ai = dog()
# ai.color()
# ai.bark()        

# polumorphism

# class anmial :
#     def color(self) :
#         self.name = "jerry"
#         print("this is a animal class")
# class dog(anmial) :
#     def color(self) :
#         self.catName = "tom"
#         print(f"{self.name} bhaooo bhaooo  ")
# class cat(dog) :
#     def color(self) :
#         print(" meow meow  ")

# def func(obj):
#     obj.color()

# s1 = cat()
# func(s1)

# i = 1
# while i <= 20 :
#     print(i)
#     i += 1

# word = "Python"
# for letter in word:
#     print(letter)

# n = int(input("Enter a number to get its mutiplication table: "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")


# n = int(input("Enter a number: "))

# # for i in range (1, n+1):
# #     if i % 2 != 0:
# #      print(i)

# sum_of_numbers = sum(range(1, n+1))

# print(f"The sum of all numbers from 1 to {n} is {sum_of_numbers}")

# name = "Arsalan"
# surName = "Muhammad"

# if name == "Arsalan" and surName == "Muhamm" : 
#     print(f"{name}'s roll no is 21")
# else :
#  print("you are not the student of this class")


# class Vehicle:
#     def __init__(self,name,model):
#         self.name = name
#         self.model=model
# class Car(Vehicle) :
#     def __init__(self,name,model,price):
#         super().__init__(name,model)
#         self.price = price
#     def show(self):

#         print(f"My car is {self.name} and its model is {self.model} and its price is {self.price}")        

# car = Car("corolla","Toyota", "75,00,000")
# car.show()


my_list = [1,2,2,2,2,3,4,5]
my_list2 = [6,4,7,9,2,8]
tuple = (1,2,3)
# my_list.append(6)
# my_list.extend([6,7,8,9])
# my_list.insert(1,7)
# my_list2.sort()
# my_list.reverse()
# print(sum(my_list))
# print(len(my_list))
# print(max(my_list))
# print(min(my_list))
# my_list3 = list(tuple)
# print(my_list3)
# copyList = my_list2.copy()
# print(copyList)
# countList = my_list.count(2)
# popList = my_list2.pop(2)
# my_list.remove(5)
# indexList = my_list2.index(9)
# my_list.clear()
# # print(indexList)

# print(my_list)
# my_list2[1] = 5
# my_list2[0:2]= [5,5]
# print(my_list2)

import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter")
root.geometry("400x400")

label = tk.Label(root, text="Basic Tkinter App" , font=("arial",16))
label.pack(pady=8)

def on_click():
    label.config(text="Clicked")


button = tk.Button(root, text="Click me", command=on_click)
button.pack(pady=8)

entry = tk.Entry(root, font=("arial",12))
entry.pack(pady=8)

def show_input():
    text = entry.get()
    label.config(text=f"you entered {text}")

button = tk.Button(root, text="Show input", command=show_input)
button.pack(pady=8)    
root.mainloop()