#!/usr/bin/env python

# A script that prints a square pattern using '*'

rows = int(input("Enter the size of the pattern: "))

index = 1;

while index <= rows:
    side = 1;
    while side <= rows:
        print("*", end="")
        side += 1
    print()
    index += 1