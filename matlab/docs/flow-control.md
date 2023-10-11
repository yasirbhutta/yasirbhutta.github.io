# Control Statements

- [Download PDF](https://yasirbhutta.github.io/matlab/docs/flow-control.pdf)

- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/matlab/docs/flow-control.html](https://yasirbhutta.github.io/matlab/docs/flow-control.html)

## Introduction

## Loops

## For Loop

- A for loop in MATLAB is a programming statement that repeats a block of code a certain number of times.
- They are used in a wide variety of applications, such as mathematical computations, data processing, and graphical plotting.

### Syntax - for loop

```matlab
for variable = expression
    statements
end
```

- **variable** is a loop counter variable that is initialized to the value of expression at the start of the loop.
- **expression** is a mathematical expression that evaluates to a scalar value.
- **statements** are the statements that are executed within the loop body.

The loop counter variable is incremented by 1 after each iteration of the loop. The loop continues to iterate until the loop counter variable is greater than the value of expression.

#### MATLAB Example: Printing "Hello, World!" Ten Times Using a for Loop

```matlab
for i = 1:10
    disp('Hello, world!');
end
```

#### MATLAB Example: Print Numbers from 1 to 5

```matlab
   for i = 1:5
       disp(i);
end
```

#### MATLAB Example: Print the numbers from 1 to 10

```matlab
% Print the numbers from 1 to 10 to the console.
for i = 1:10
  fprintf('The number is %d\n', i);
end

```

#### MATLAB Example: Sum of Numbers from 1 to N

 ```matlab
   N = 10;
   sum = 0;
   for i = 1:N
       sum = sum + i;
   end
   disp(sum);
```

#### MATLAB Example: Calculate the sum of the numbers from 1 to 100

```matlab
sum = 0;
for i = 1:100
    sum = sum + i;
end
disp(sum);
```

#### MATLAB Example: Print Even Numbers from 1 to 10

 ```matlab
   for i = 2:2:10
       disp(i);
   end
```

#### MATLAB Example: Print Sum of Even Numbers from 0 to 20

```matlab
sum = 0;
for k = 0:2:20,
    sum = sum + k;
end;
fprintf('sum %d', sum);
```

#### MATLAB Example: Calculating the Sum of Elements in an Array

```matlab
sum = 0;
for arr1 = [1 5 7 6],
    sum = sum + arr1;
end;
fprintf('sum = %d',sum)
```

#### MATLAB Example: Displaying Elements of an Array Using a for Loop

```matlab
   A = [10, 20, 30, 40, 50];
   for i = 1:length(A)
       disp(A(i));
end
```

#### MATLAB Example: Infinite loop

```matlab
for k=1:inf
    disp(k)
end
```

- A **nested loop** is a loop inside another loop. It is a powerful programming technique that can be used to solve a wide variety of problems.
- We use nested loops when we need to iterate over multiple dimensions of data. For example, we might use a nested loop to print a two-dimensional array, or to search through a list of lists.

#### Example: Nested Loops - Multiplication Table

```matlab
for i = 1:5
    for j = 1:5
           fprintf('%d x %d = %d\n', i, j, i * j);
    end
end
```

## Conditional Statements / Branches

## Review Questions

1. What is the purpose of a for loop in MATLAB?
2. What is the syntax for creating a for loop in MATLAB?
3. What is the exit condition for a for loop in MATLAB, and how is it specified?
4. How can you create nested for loops in MATLAB, and what is their purpose?
5. How can you use the break statement in a for loop to prematurely exit the loop?
6. What is the purpose of the continue statement in a for loop?
7. How can you calculate the cumulative sum of elements in an array using a for loop?
8. What happens if you forget to increment the loop variable in a for loop?

### Coding Questions

1. Write a MATLAB for loop that prints the numbers from 1 to 10 to the command window.
2. Write a MATLAB for loop that calculates the sum of the numbers from 1 to 10.
3. Write a MATLAB program to get input from the user to display a table of a given number. The program should prompt the user to enter the number and then print a table showing the multiplication table for that number from 1 to 10.

**Example output:**

```matlab
Enter a number: 5

Multiplication table for 5


1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
```

2. Write a MATLAB program that uses a for loop to print the numbers from 1 to 10.
3. Create a MATLAB program that calculates the sum of all even numbers from 1 to 50 using a for loop.
4. Write a for loop to print the even numbers from 1 to 100.
5. Write a for loop to find the factorial of a given number.
6. Write a for loop to find the prime numbers from 1 to 100.

## Multiple Choice

True/False

1. A for loop can be used to execute a block of code multiple times. (True)
2. The increment expression in a for loop is evaluated before each iteration of the loop. (True)
3. A MATLAB for loop can only iterate over a range of numeric values. (False)
4. A for loop can be used to execute a block of code once. (False)
5. A MATLAB for loop can be nested inside of another for loop. (True)
6. The break statement can be used to exit a for loop early. (True)
The continue statement can be used to skip the remaining code in the current iteration of a for loop and proceed to the next iteration. (True)

A for loop can be nested inside another for loop. (True)

### For loop

#### What is the default increment value for a MATLAB for loop?

A. 1
B. 2
C. 10
D. None of the above

#### Which of the following is the correct syntax for a for loop in MATLAB?

A. for i = 1:10 % code block end
B. for i = 1:10 % code block endfor
C. for i = 1:10 do
D. for i = 1:10

#### What is the purpose of the increment expression in a for loop?

A. To set the initial value of the loop counter
B. To specify the number of times the loop will iterate
C. To determine the step size between iterations
D. All of the above

#### In MATLAB, what is the primary purpose of a for loop?

a. To create a sequence of numbers
b. To execute a block of code repeatedly a specified number of times
c. To check if a condition is true
d. To perform mathematical calculations

#### What is the structure of a for loop in MATLAB?

a. for i = 1:10
b. repeat 10 times
c. while i < 10
d. if i = 1 to 10

#### How is the loop variable updated in a for loop?

a. Automatically by MATLAB
b. It is not updated
c. Manually within the loop
d. The loop variable cannot be changed

#### What is the output of the following for loop?

```matlab
for i = 1:5
    disp(i);
end
```

a. 1 2 3 4 5
b. 5 4 3 2 1
c. 1 1 1 1 1
d. No output is generated.

#### What is the expected output of the following MATLAB code?

```matlab
for i = 2:2:10
    disp(i);
end
```

a. 2 4 6 8 10
b. 1 3 5 7 9
c. 2 4 8
d. 2 4 6 10

#### What is the expected output of the following MATLAB code?

```matlab
sum = 0;
for i = 1:5
    sum = sum + i;
end
disp(sum);
```

a. 0
b. 1
c. 15
d. 10

#### What is the expected output of the following MATLAB code?

```matlab
for i = 1:4
    if i == 3
        continue;
    end
    disp(i);
end

```

a. 1 2
b. 1 2 3 4
c. 1 2 4
d. 4

#### What is the expected output of the following MATLAB code?

```matlab
for i = 1:5
    if i == 3
        break;
    end
    disp(i);
end

```

a. 1 2 3 4 5
b. 1 2
c. 1 2 4 5
d. 3

#### While loop

- What is the difference between a for loop and a while loop?
- 

## Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
