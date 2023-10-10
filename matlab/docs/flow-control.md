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

#### Example: Printing "Hello, World!" Ten Times Using a for Loop

```matlab
for i = 1:10
    disp('Hello, world!');
end
```

#### Example: Print Numbers from 1 to 5

```matlab
   for i = 1:5
       disp(i);
end
```

#### Example: Print the numbers from 1 to 10

```matlab
% Print the numbers from 1 to 10 to the console.
for i = 1:10
  fprintf('The number is %d\n', i);
end

```

#### Example: Sum of Numbers from 1 to N

 ```matlab
   N = 10;
   sum = 0;
   for i = 1:N
       sum = sum + i;
   end
   disp(sum);
```

#### Example: Calculate the sum of the numbers from 1 to 100

```matlab
sum = 0;
for i = 1:100
    sum = sum + i;
end
disp(sum);
```

#### Example: Print Even Numbers from 1 to 10

 ```matlab
   for i = 2:2:10
       disp(i);
   end
```

#### Example: Print Even Numbers from 0 to 20

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

## Exercises

1. Write a MATLAB program to get input from the user to display a table of a given number. The program should prompt the user to enter the number and then print a table showing the multiplication table for that number from 1 to 10.

**Example output:**

```
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

## Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
