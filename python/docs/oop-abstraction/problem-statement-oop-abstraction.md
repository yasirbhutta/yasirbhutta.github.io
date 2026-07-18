# Problem Statement: OOP Abstraction in Python

Design a Python program to demonstrate the concept of **Abstraction** using abstract classes and methods.

Create an abstract class named `Shape` using the `ABC` module. The class should contain:

* An abstract method named `area()`
* An abstract method named `perimeter()`

Then create the following child classes:

1. `Rectangle`

   * Attributes: `length`, `width`
2. `Circle`

   * Attribute: `radius`

Each child class must implement the abstract methods `area()` and `perimeter()` according to its own formula.

## Tasks

1. Import the required module for abstraction.
2. Create the abstract class `Shape`.
3. Implement abstract methods in the child classes.
4. Create objects of both `Rectangle` and `Circle`.
5. Display:

   * Shape type
   * Area
   * Perimeter
6. Demonstrate that an object of the abstract class cannot be created directly.

## Sample Output

```python
Shape: Rectangle
Area: 50
Perimeter: 30

Shape: Circle
Area: 78.5
Perimeter: 31.4
```

## Instructions

* Use proper class structure and indentation.
* Use constructors (`__init__`) to initialize attributes.
* Use meaningful variable names.
* Add comments where necessary.

## Learning Objectives

After completing this practical exam, students will be able to:

* Understand the concept of abstraction in OOP
* Use abstract classes and abstract methods in Python
* Implement inheritance with abstraction
* Write reusable and organized code

Abstraction helps in hiding implementation details and showing only essential features to the user. ([gyata.ai][1])

[1]: https://yasirbhutta.github.io/python/docs/oop-abstraction/ "OOP Abstraction | Learn with Yasir"
