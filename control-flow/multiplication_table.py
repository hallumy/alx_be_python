#!/usr/bin/env python

# A script that prints a multiplication table based on users input

number = int(input("Enter a number to see its multiplication table: "))

for Y in range(1, 11):
    Z = number * Y
    print(f"{number} * {Y} = {Z}")