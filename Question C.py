""" Write a Python program to get the third side of right angled triangle from two given sides """

from math import sqrt

a = float(input("enter the value for a: "))
b = float(input("enter the value for b: "))

c = int()
c = sqrt(a * a + b * b)
print('The length of side c is %g: ' %(c))