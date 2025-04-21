from collections import defaultdict, Counter


# list
#
a = [1, 2]
a.append(3)

#
#
#
# # class MyClass:
# #     pass
#
#
# class Person:
#     pass
#
# bob = Person()
# tom = Person()
# print(bob)
# print(tom)
#
#
#
# class MyClass:
#     name = "John"
#     age = 30
#
# print(dir(MyClass))
# # MyClass.


# class MyClass:
#     class_field = "Class Field"
#
#
# print(MyClass.class_field)
# my_object = MyClass()
# print(my_object.class_field)
#
#
# my_object.instance_field = "Instance Field"
# print(my_object.instance_field)
# # MyClass.instance_field
#
#

# class Person:
#
#     def __init__(self, person_name="Bob"):
#         print(self)
#         print(person_name)
#         self.name = person_name
#
#
#     def say_hello(self):
#         print(f"Hello, {self.name}!")
#
#     # def print_color(self, color):
#     #     print(color)
#
#
# my_object = Person("John")
# print(my_object.name)
#
# my_object2 = Person()
# print(my_object2.name)
#
# my_object.say_hello()
# my_object2.say_hello()
#
# print()
# Person.say_hello(my_object)



class Person:

    field7 = "value7"

    def __init__(self, person_name, field2):
        self.field5 = None
        self.name = person_name
        self.field2 = field2
        self.field3 = "default_value3"

    def say_hello(self):
        print(f"Hello, {self.name}!")

    def set_field6(self, field6):
        self.field5 = "default_value5"
        self.field6 = field6

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name


Person.field1 = "value1"
print(Person.field1)
p1 = Person("Bob", "value2")
p1.field4 = "value4"
p1.set_field6("value6")
print(p1.field6)

print(p1.get_name())

p1.field2 = "New value2"
Person.field1 = "New value1"
p1.change_name("New name")
p1.say_hello()

Person.change_name(p1, "New name2")
p1.say_hello()

a = 5
a = None
del a
del p1.field3
del p1
