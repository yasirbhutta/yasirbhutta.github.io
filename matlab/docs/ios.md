# Input Output Statements

- [Download PDF](https://yasirbhutta.github.io/matlab/docs/ios.pdf)

- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/matlab/docs/ios.html](https://yasirbhutta.github.io/matlab/docs/ios.html)

## Introduction

## Data Input

### What is variable

- A variable in programming language is a named storage location in computer memory.
- It is used to store data that can be changed during the course of program execution.
- Variables can be used to store any type of data, such as numbers, text, dates, and objects.

### Assignment Statement and Variable Declaration

## Interactive Inputs

### Input Functions

[Video Tutorial: How to Create a New Script File Using MATLAB Mobile App](https://www.youtube.com/watch?v=_494zaRAIGo)

#### Example 1

Write a MATLAB script to take input two numbers from users and output the sum of those numbers.

```matlab
% Prompt the user for two numbers
num1 = input('Enter the first number: ');
num2 = input('Enter the second number: ');

% Calculate the sum of the two numbers
sum = num1 + num2;

% Output the sum to the user
disp(sum)
```

#### Example 2

Write a MATLAB script to take input name and age from users and display the name and age.

```matlab
% Prompt the user for their name and age
name = input('Enter your name: ', 's');
age = input('Enter your age: ');

% Display the name and age to the user
disp('Output of the code')
disp(name)
disp(age)
```

### Keyboard Command

#### Syntax

```matlab
keyboard
```

- keyboard pauses execution of a running program and gives control to the keyboard.
- Place the keyboard function in a program at the location where you want MATLAB® to pause.
- When the program pauses, the prompt in the Command Window changes to K>>, indicating that MATLAB is in debug mode.
- You then can view or change the values of variables to see if the new values produce expected results.

>**Tips**

- To terminate debug mode and continue execution, use the dbcont command.
- To terminate debug mode and exit the file without completing execution, use the dbquit command.

#### Example 3

```matlab
% Perform some calculations
a = 5;
b = 10;
c = a + b;
    
% Pause execution and enter debugging mode
keyboard

% Continue with more calculations
d = c * 2;
    
% Return the result
result = d;

disp(result)
```

### Pause Command

#### Syntax 

```matlab
pause(n)
```

- In MATLAB, the `pause` keyword is used to pause the execution of a script or function for a specified amount of time. 
- It can be useful in various situations, such as creating delays in animations, giving users time to read messages, or controlling the timing of certain operations.

#### Example 4

```matlab
a = 5;
b = 10;

c = a+b;
disp('Sum');
disp(c);

pause(2)

disp('Product');
result = a * b;
disp(result);

pause(2)

result = b/a;
disp('Divide');
disp(result);

```

### menu Command

### fprintf command

- fprintf() is a built-in function in MATLAB that is used to format and print data to the console.
- It takes a variable number of arguments, the first of which is a format string that specifies how the data should be formatted. The remaining arguments are the data values that should be printed.
- The format string is a sequence of characters that tells MATLAB how to format the data. It can include characters such as "%d" for integers, "%f" for floats, and "%s" for strings. The format string can also include other characters, such as spaces and commas, to control the appearance of the output.

#### Syntax

fprintf(text)
fprintf(formatspec,var)

fprintf(text) command displays formatted text centered on the icon .

fprintf(formatspec,var) formats var as specified in formatSpec.

#### Example: Display the text Hello

```matlab
fprintf('Hello');
```

#### Example: Display name

```matlab
name = 'Ali';
fprintf('Your name is %s', name);

```

#### Example

Convert the character a to an integer 97 and display it on the block icon.

```matlab
myvar = 'a'
fprintf('hello = %d',myvar);
```

#### Example : Printing a number

```matlab
x = 10;
fprintf('The value of x is %d\n', x);
```

This will print the following output to the command window:

```
The value of x is 10
```

#### Example: Printing multiple values

```matlab
x = 10;
y = 20;
fprintf('The values of x and y are %d and %d, respectively.\n', x, y);
```

This will print the following output to the command window:

```
The values of x and y are 10 and 20, respectively.
```

#### Example: Printing formatted values

The `fprintf` function also supports a variety of formatting options that allow you to control how values are printed. For example, you can specify the precision of floating-point numbers, the width of fields, and the alignment of text.

The following example shows how to print a floating-point number with two decimal places:

```matlab
x = 1.2345678;
fprintf('The value of x is %.2f\n', x);
```

This will print the following output to the command window:

```
The value of x is 1.23
```

#### Example: Printing formatted string

The following example shows how to print a string centered in a field of 20 characters:

```matlab
s = 'This is a string.';
fprintf('%20s\n', s);
```

This will print the following output to the command window:

```
     This is a string.
```

#### Example: Sum of two numbers

```matlab
num1 = input('Enter first value');
num2 = input('Enter second value');

total = num1 + num2;

fprintf('Sum of %d and %d is %d', num1, num2, total);
```

#### Example: use of line break in fprintf

```matlab
% Data Input
name = input('Enter your name','s');
city = input('Enter your city','s');
age  = input('Enter your age');

% Disply variables
% \n is used for line bread
fprintf('====== Student Details =====\n');
fprintf('Name = %s \n', name);
fprintf('City = %s \n', city);
fprintf('Age = %d \n', age);
```

## Reading/Storing File Data

## Resources


### MCQS

1. **Which of the following is the correct extension of the Python file?**

>**a.** .python
>**b.**  .pl
>**c.**  .p
>**d.**  .py

1. **What is the purpose of the input function in MATLAB?**

>**a.** To display text on the console
>**b.** To wait for a key press
>**c.** To take user input from the console
>**d.** To pause script execution

2. **Which keyword is used in MATLAB for interactive debugging by pausing script execution and entering the debug mode?**

>**a.** stop
>**b.** keyboard
>**c.** break
>**d.** pause

#### What does the pause function in MATLAB do?

- a. Stops the execution of the script
- b. Adds a delay in script execution
- c. Accepts keyboard input from the user
- d. Prints a message to the console

#### Which of the following is true about the input function in MATLAB?

a. It only accepts numerical input
b. It always displays a message to the user
c. It can accept both numerical and string input
d. It cannot be used in MATLAB scripts

1. **Which of the following is a correct usage of the input function in MATLAB?**

a. input('Enter a number: ')
b. keyboard('Please enter a number: ')
c. pause('Enter a value: ')
d. None

6. **How can you specify the duration of a pause in seconds when using the pause function in MATLAB?**

a. The pause function does not allow you to specify a duration.
b. By passing the number of seconds as an argument: pause(2)
c. By pressing a key on the keyboard
d. By using a loop within the script

## **Review Questions**

### Write note on Common Ways to Input Data in MATLAB?

### What is a variable in computer programming?

>**Answer:** A variable is a named storage location in a computer's memory that is used to hold data or values. It allows programmers to store and manipulate data within a program.

### What is the purpose of using variables in programming?

>**Answer:** Variables provide a way to store and manage data that can be used and manipulated throughout a program. They make programs more flexible and allow for dynamic data storage.

#### What is the difference between declaring and initializing a variable?

>**Answer:** Declaring a variable involves specifying its name and data type, while initializing a variable means giving it an initial value. Initialization usually follows declaration but is not always required.

### In MATLAB, what happens if you try to access a variable that has not been declared or initialized?

>**Answer:** In MATLAB, trying to access an undeclared or uninitialized variable typically results in an error. MATLAB will display a message indicating that the variable is undefined.

### What is a data type in MATLAB, and why is it important?

>**Answer:** A data type in MATLAB defines the kind of values a variable can hold and how those values are stored and manipulated. It's important because it affects memory usage, performance, and the operations that can be performed on the data.

### How do you assign a new value to an existing variable in MATLAB?

>**Answer:** In MATLAB, you can assign a new value to an existing variable simply by using the variable name followed by the new value. For example, x = 10; assigns the value 10 to the variable x.

### What is an assignment statement in MATLAB, and what is its primary purpose?

>**Answer:** An assignment statement in MATLAB is used to assign a value to a variable. Its primary purpose is to store and manage data within a program.

### Explain the difference between the = operator and the == operator in MATLAB.

>**Answer:** The = operator is used for assignment, setting the value of a variable. The == operator is used for comparison and checks if two values are equal.

### What is the purpose of the clear command in MATLAB, and how does it relate to variable declaration?

>**Answer:** The clear command in MATLAB is used to remove variables from the workspace. It's related to variable declaration because it allows you to clean up the workspace and remove unused variables, which can help manage memory effectively.

#### What is the purpose of the keyboard keyword in MATLAB, and how is it used in a script or function?

#### What are some common use cases for using the pause keyword in MATLAB scripts or functions?

#### Can you provide an example of using the pause function to create a timed delay in a MATLAB script?

Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
