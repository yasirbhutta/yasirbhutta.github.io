# [MATLAB for Beginners](https://yasirbhutta.github.io/matlab/)

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

## Input Output Statements

- [Download PDF](https://yasirbhutta.github.io/matlab/docs/ios.pdf)

- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/matlab/docs/ios.html](https://yasirbhutta.github.io/matlab/docs/ios.html)

## Introduction

## Comments

- Comments in MATLAB are used to explain the code and make it more readable.
- Comments are ignored by the MATLAB interpreter, so they do not affect the execution of the code.

There are two ways to add comments in MATLAB:

- **Single-line comments:** Start a single-line comment with a percent sign (%). Everything on the line after the percent sign is ignored by the MATLAB interpreter. For example:

```matlab

% This is a comment.

```

- **Block comments:** Start a block comment with a pair of curly braces (%{ and %}). Everything between the curly braces is ignored by the MATLAB interpreter. Block comments can be used to comment out multiple lines of code. For example:

```matlab
%{
This is a block comment.
It can be used to comment out multiple lines of code.
%}

```

## Data Input

### What is variable

- A variable in programming language is a named storage location in computer memory.
- It is used to store data that can be changed during the course of program execution.
- Variables can be used to store any type of data, such as numbers, text, dates, and objects.

### Assignment Statement and Variable Declaration

## Interactive Inputs

### Input Functions

**MATLAB Tutorial in urdu: How to Create a New Script File Using MATLAB Mobile App**

{% assign video_type = "short" %}
{% assign video_id = "_494zaRAIGo" %}

{% include youtube-video.html video_type=video_type video_id=video_id %}

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

- The fprintf command is used to format and display data on the command window or write data to a file.[^1]
- It takes a variable number of arguments, the first of which is a format string that specifies how the data should be formatted. The remaining arguments are the data values that should be printed.
- The format string is a sequence of characters that tells MATLAB how to format the data. It can include characters such as "%d" for integers, "%f" for floats, and "%s" for strings. The format string can also include other characters, such as spaces and commas, to control the appearance of the output.

**Syntax:**

```matlab
fprintf(text)

fprintf(formatspec,var)

fprintf(text) command displays formatted text centered on the command window .

fprintf(formatspec,var) formats var as specified in formatSpec.
```

- **formatSpec** is a string that specifies the format of the output data.

Here are some common format specifiers used with the fprintf command:

| Format specifier | Description |
|---|---|---|
| %d | Integer |
| %f | Floating-point number |
| %c | Character |
| %s | String |
| \n | Newline character |

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

> What is the purpose of the input function in MATLAB?

1. [ ] To display text on the console
2. [ ] To wait for a key press
3. [x] To take user input from the console
4. [ ] To pause script execution

> Which command is used in MATLAB for interactive debugging by pausing script execution and entering the debug mode?

1. [ ] stop
2. [x] keyboard
3. [ ] break
4. [ ] pause

#### Input Command (MCQs)

> What does the pause function in MATLAB do?

1. [ ] Stops the execution of the script
2. [x] Adds a delay in script execution
3. [ ] Accepts keyboard input from the user
4. [ ] Prints a message to the console

> Which of the following is true about the input function in MATLAB?**

1. [ ] It only accepts numerical input
2. [ ] It always displays a message to the user
3. [x] It can accept both numerical and string input
4. [ ] It cannot be used in MATLAB scripts

> Which of the following is a correct usage of the input function in MATLAB?

1. [x] input('Enter a number: ')
2. [ ] keyboard('Please enter a number: ')
3. [ ] pause('Enter a value: ')
4. [ ] None

> Which of the following is true about the input function's behavior if the user enters non-numeric input when expecting a number?

1. [ ] It displays an error message and terminates the program.
2. [ ] [ ] It converts the input to a numeric value.
3. [ ] It throws an error and crashes MATLAB.
4. [ ] It loops until valid numeric input is provided.

> When using the input function to collect user input, how can you display a prompt message?

1. [ ] There is no way to display a prompt message with input.
2. [ ] By specifying the prompt message as an argument to the input function.
3. [ ] By using the display function before calling input.
4. [ ] By defining the prompt message as a variable.

#### Pause and keyboard Commands (MCQs)

> What does the pause command do in MATLAB?

1. [ ] Ends the program
2. [ ] Pauses the program's execution for a specified duration
3. [ ] Prompts the user for input
4. [ ] Clears the command window

> How is the duration of the pause specified in the pause command?

1. [x] In seconds
2. [ ] In milliseconds
3. [ ] In minutes
4. [ ] It is not possible to specify a duration

> What is the primary purpose of the keyboard command in MATLAB?

1. [ ] To insert a physical keyboard into the program
2. [ ] To pause program execution and enter the debug mode
3. [x] To display a virtual keyboard on the screen
4. [ ] To display the program's source code

> In what scenarios might you use the keyboard command in MATLAB?

1. [ ] To create interactive user interfaces
2. [ ] To simulate keyboard input
3. [x] For debugging and inspecting variables during program execution
4. [ ] To change the color of the command window

> How can you specify the duration of a pause in seconds when using the pause function in MATLAB?

1. [ ] The pause function does not allow you to specify a duration.
2. [x] By passing the number of seconds as an argument: pause(2)
3. [ ]  By pressing a key on the keyboard
4. [ ]  By using a loop within the script

#### fprintf Command

> What is the purpose of the fprintf function in MATLAB?

1. [ ] To read data from a file
2. [x] To format and display output to the console or a file
3. [ ] To accept input from the user
4. [ ] To calculate mathematical expressions

> Which function is used to display formatted output in MATLAB?

1. [ ] output
2. [ ] printf
3. [ ] print
4. [x] fprintf

> Which character is commonly used as a placeholder for inserting variable values within a formatted string when using fprintf?

1. [ ] #
2. [ ] $
3. [x] %
4. [ ] @

> In fprintf formatting, the %d specifier is used for:

1. [x] Decimal (integer) values
2. [ ] Floating-point values
3. [ ] Characters
4. [ ] Strings

> When using fprintf, the escape sequence \n is used for:

1. [ ] Printing a backslash
2. [x] Printing a newline character
3. [ ] Printing a tab character
4. [ ] Printing a space

> In the fprintf function, what does the %f specifier typically represent?

1. [ ] An integer
2. [x] A floating-point number
3. [ ] A character
4. [ ] A string

> When using fprintf, what does the format specifier %s represent?

1. [ ] An integer
2. [ ] A floating-point number
3. [ ] A character
4. [x] A string

> Which of the following is the correct way to format a number using the fprintf command?

1. [ ] fprintf('%.2f\n', number);
2. [ ] fprintf('%s\n', number);
3. [ ] fprintf('%c\n', number);
4. [x] fprintf('%d\n', number);

> Which of the following is the correct way to format the output of the fprintf command?

1. [x] fprintf('%s', 'Hello, world!')
2. [ ] fprintf('%s', 'Hello, world!\n')
3. [ ] fprintf('%s', Hello, world!')
4. [ ] None of the above

> Which of the following is the correct way to print a number using the fprintf command?

1. [x] fprintf('%d', 123)
2. [ ] fprintf('%s', 123.456)
3. [ ] fprintf(123.456e-10)
4. [ ] All of the above

> Which of the following is the correct way to print a string using the fprintf command?

1. [ ] fprintf('%s', 'Hello, world!')
2. [ ] fprintf('%c', 'Hello, world!')
3. [ ] fprintf('%d', 'Hello, world!')
4. [ ] None of the above

> Which of the following is a valid format specifier for the fprintf command?

1. [ ] %d
2. [ ] %f
3. [ ] %s
4. [x] All of the above

## Review Questions

1. Write note on Common Ways to Input Data in MATLAB?
2. What is the difference between the input and disp commands?
3. How do you prompt the user for input?
4. How do you use the input function to prompt the user for a string input?
5. What is the purpose of the keyboard keyword in MATLAB, and how is it used in a script or function?
6. What are some common use cases for using the pause keyword in MATLAB scripts or functions?
7. Can you provide an example of using the pause function to create a timed delay in a MATLAB script?
8. What is the difference between the input and fprintf commands?
9. What is the purpose of the fprintf command in MATLAB?
10. What is the syntax for using the fprintf command in MATLAB?
11. Explain the role of format specifiers in fprintf. Provide examples of commonly used format specifiers.
12. How can you print numerical values with a specific number of decimal places using fprintf?
13. What is the difference between %s and %d format specifiers in fprintf? When and how would you use each?
14. Explain how to create a newline character in the output file when using fprintf.
15. What is the fprintf command used for?
16. Give two examples of how to use the fprintf command.
17. How do you print a string of text to the command window using the fprintf command?
18. How do you print a numeric value to the command window using the fprintf command?
19. Write a MATLAB script that uses the fprintf command to print the value of the variable x to the command window, formatted to display two decimal places.

### What are some of the common mistakes people make when using the fprintf command?

>**Answer:** Some of the common mistakes people make when using the fprintf command include:

- Forgetting to specify the format specifier.
- Using the wrong format specifier for the data type to be displayed.
- Forgetting to enclose the format specifier in single quotes.
- Forgetting to use the \n escape sequence to display a new line character.
- Forgetting to close the file when writing data to a file using the fprintf command.

### Write a MATLAB script that uses the fprintf command to print the following text to the command window:

Hello, world

### How can I display a new line character?

>**Answer:** To display a new line character, you can use the \n escape sequence. For example, to print the following message to the command window:

```matlab
Hello,
world!
```

You would use the following fprintf command:

```matlab
fprintf('Hello,\nworld!\n')
```

### What are some tips for using the fprintf command effectively?

>**Answer:** Here are some tips for using the fprintf command effectively:

> - Use the correct format specifier for the type of data you want to display or write to a file.
> - Use newline characters (\n) to separate lines of output.
> - Use comments to make your code more readable and maintainable.
  
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

### Explain the difference between the = operator and the == operator in MATLAB

>**Answer:** The = operator is used for assignment, setting the value of a variable. The == operator is used for comparison and checks if two values are equal.

### What is the purpose of the clear command in MATLAB, and how does it relate to variable declaration?

>**Answer:** The clear command in MATLAB is used to remove variables from the workspace. It's related to variable declaration because it allows you to clean up the workspace and remove unused variables, which can help manage memory effectively.

## Excercises

1. Write a MATLAB script that prompts the user for their name and age, and then displays a greeting message that includes their name and age.
2. Write a MATLAB script that prompts the user for two numbers, and then displays the sum, difference, product, and quotient of the two numbers.
3. Write a MATLAB script that prompts the user for a vector of numbers, and then displays the maximum, minimum, mean, and median of the vector.

## References

[^1:] [MATLAB fprintf - MathWorks](https://www.mathworks.com/help/simulink/slref/fprintf.html)


What is the difference between input and fprintf? Explain the difference with an example."
