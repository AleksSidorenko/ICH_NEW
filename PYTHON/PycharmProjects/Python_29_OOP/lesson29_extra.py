class MyClass:
    class_field = "Class Field"

my_object1 = MyClass()
my_object2 = MyClass()
my_object1.instance_field = "Instance Field"

print(MyClass.class_field)
print(my_object1.class_field)
print(my_object1.instance_field)
print()

print(my_object2.class_field)
# print(my_object2.instance_field)
print()

my_object1.class_field = "New"
print(my_object1.class_field)
print(my_object2.class_field)
print(MyClass.class_field)
print()

MyClass.class_field = "New Class Field"
print(MyClass.class_field)
print(my_object1.class_field)
print(my_object2.class_field)

