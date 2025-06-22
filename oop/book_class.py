#!/usr/bin/env python

class Book:
    """
    A class that has a constructor __init__  that initializes a Book instance
    with the title, author and year. It has a destructor __del__ that prints
    a message upon an object deletion
    """ 

    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print (f"Deleting {self.title}") 
