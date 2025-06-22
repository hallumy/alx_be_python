# 📘 Book Class in Python

This project contains a simple Python script named `book_class.py` that defines a `Book` class using Python's **magic methods** to enhance its behavior and provide meaningful representations.

## 📝 Description

The `Book` class models a book with attributes for its title, author, and publication year. It implements several special methods to control how instances of the class are created, displayed, and deleted.

## 📁 File Structure


## 🔧 Book Class Features

### Attributes

- `title` (`str`): The title of the book
- `author` (`str`): The name of the author
- `year` (`int`): The year the book was published

### Magic Methods

- `__init__(self, title, author, year)`  
  Initializes a `Book` instance with title, author, and publication year.

- `__del__(self)`  
  Prints a message in the format:  
when the object is deleted.

- `__str__(self)`  
Returns a readable string representation:  


- `__repr__(self)`  
Returns an official string representation that can be used to recreate the object:  
```python
Book('<title>', '<author>', <year>)

