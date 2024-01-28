# Python: Language Basics

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/classes.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/ms-excel/docs/classes.html](https://yasirbhutta.github.io/ms-excel/docs/classes.html)

- [Python Playlist on Youtube](https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)
- [Download Example Code](https://github.com/yasirbhutta/python-examples)
- [Pyton Resources: Books, Websites, Tutorials](../resources.md)
- [Python Tools](../tools.md)
- [Python - Quick Guide for Ultimate Python Beginner's](quick-guide.md)

## Classes

- Classes act as blueprints for creating objects.

**What are instance attributes?:**

- Unique to each instance (object) of a class.
- Store data specific to that object.
- Defined within the __init__() constructor method, using the self parameter.

**Example #:**

```python
# Class Definition
class Student:
    # Constructor
    def __init__(self, name, age, grade): # self refers to the current object being created.
        self.name = name
        self.age = age
        self.grade = grade
    # Method
    def info(self):
        print(f"Name = {self.name} Age = {self.age} Grade = {self.grade}")

# Object Creation

student1 = Student("Hamza", 8, 3)
student2 = Student("Muhammad", 15, 10)

# Accessing Attributes and Methods

print(student1.name)
student1.info()
student2.info()
```

**Key Points:**

- Classes act as blueprints for creating objects.
- Objects are instances of classes, each with their own attributes (data) and methods (behaviors).
- The `__init__()` method initializes objects when they're created.
- Methods are functions defined within a class that operate on the object's data.
- `self` is used to access the object's attributes and methods within its methods.


**Example #:**

```python
class Student:
    """Represents a student with their name, age, and grade."""

    def __init__(self, name, age, grade):
        """Initializes a Student object with the given attributes."""
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        """Returns the student's name."""
        return self.name

    def get_age(self):
        """Returns the student's age."""
        return self.age

    def get_grade(self):
        """Returns the student's grade."""
        return self.grade

    def set_grade(self, new_grade):
        """Updates the student's grade."""
        self.grade = new_grade

    def introduce(self):
        """Prints a self-introduction message."""
        print("Hello, my name is", self.name, "and I'm in grade", self.grade)

# Example usage
student1 = Student("Hamza", 8, 3)
student2 = Student("Muhammad", 16, 10)

student1.introduce()  # Output: Hello, my name is Alice and I'm in grade 9
print(student2.get_name())  # Output: Bob
student2.set_grade(11)
print(student2.get_grade())  # Output: 11

```

## Key Terms

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

## Fill in the Blanks

## Exercises

## Review Questions

## References and Bibliography

- [Classes - Python documentation](https://docs.python.org/3/tutorial/classes.html)