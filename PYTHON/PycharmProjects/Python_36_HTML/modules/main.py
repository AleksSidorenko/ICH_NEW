import math
import requests
# math.acos(5)
# print("Hi")
# import test_script
# from test_script import test_function as tf
#
# test_script.test_function()
# test_script.test_function()
# test_script.test_function()
# # test_function()
# tf()

# import test_script
import collections

# # Папка
# import folder
# folder.folder_script.folder_function()  # Не работает с папкой
# # Но можно так
# from folder.folder_script import folder_function
# folder_function()

# # Пакет
# import package
# package.package_script.package_function()  # Работает с пакетом благодаря from .package_script import package_function

# from package import package_function  # А также можно импортировать прямо из пакета
from package import *
package_function()
another_package_function()