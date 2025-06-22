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

# 📚 Python Library System

This project consists of two Python scripts — `library_system.py` and `main.py` — designed to demonstrate the principles of **object-oriented programming** using **inheritance** and **composition**.

---

## 🔧 File Structure

.
├── library_system.py
└── main.py


---

## 🧱 `library_system.py`

This module defines all the classes used in the system.

### ✅ Base Class: `Book`

- **Attributes**:
  - `title` (str): The title of the book.
  - `author` (str): The author of the book.
- **Methods**:
  - `__init__(self, title, author)`: Initializes the title and author.

---

### ✅ Derived Classes

#### 📘 `EBook` (inherits from `Book`)
- **Additional Attribute**:
  - `file_size` (int): Size of the eBook in KB.
- **Methods**:
  - `__init__(self, title, author, file_size)`: Initializes inherited and unique attributes.

#### 📗 `PrintBook` (inherits from `Book`)
- **Additional Attribute**:
  - `page_count` (int): Total number of pages.
- **Methods**:
  - `__init__(self, title, author, page_count)`: Initializes inherited and unique attributes.

---

###
### 📚 Composition: `Library` Class

Manages a collection of books using **composition**.

- **Attributes**:
  - `books` (list): Stores instances of `Book`, `EBook`, or `PrintBook`.

- **Methods**:
  - `add_book(self, book)`: Adds a book to the library.
  - `list_books(self)`: Prints details of all books in the library.

---

## 🚀 main.py

- Creates instances of `Book`, `EBook`, and `PrintBook`.
- Adds them to the `Library`.
- Calls `list_books()` to display all books with class-specific details.

# 🔄 Polymorphism Demo in Python

This project demonstrates **polymorphism** in Python using a common interface (`area()`) in a base class and its implementation in multiple derived classes.

---

## 📁 File: `polymorphism_demo.py`

This script contains the following components:

---

## 🧱 Base Class: `Shape`

- **Purpose**: Acts as an abstract blueprint for geometric shapes.
- **Method**:
  - `area(self)`: Raises a `NotImplementedError`, requiring all derived classes to implement their own `area` method.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")

# 🧮 Class vs Static Methods Demo in Python

This project demonstrates the use of **`@staticmethod`** and **`@classmethod`** in Python within a simple calculator class. It highlights the differences between the two decorators and their appropriate use cases.

---

## 📁 File: `class_static_methods_demo.py`

This script contains a `Calculator` class with both a static method and a class method.

---

## 🧠 Key Concepts

| Concept        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `@staticmethod`| Method that doesn’t access instance (`self`) or class (`cls`) data.         |
| `@classmethod` | Method that accesses class-level data via `cls`.                            |
| Class attribute| Shared across all instances; used by class methods.                         |

---

## 🔧 Calculator Class Overview

### 🔢 Class Attribute

```python
calculation_type = "Arithmetic Operations"

