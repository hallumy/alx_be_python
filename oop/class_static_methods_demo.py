#!/usr/bin/env python

class Calculator:
    """
    A python script that includes a static method and a class method
    to perform operation
    """ 
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod

    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
