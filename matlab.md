Sure, here are some examples of arithmetic operators in MATLAB:

1. Addition (+):

```
x = 5;
y = 10;
z = x + y;
disp(z); % Output: 15
```

2. Subtraction (-):

```
x = 10;
y = 5;
z = x - y;
disp(z); % Output: 5
```

3. Multiplication (*):

```
x = 2;
y = 3;
z = x * y;
disp(z); % Output: 6
```

4. Division (/):

```
x = 6;
y = 3;
z = x / y;
disp(z); % Output: 2
```

5. Exponentiation (^):

```
x = 2;
y = 3;
z = x ^ y;
disp(z); % Output: 8
```

6. Modulo (%):

```
x = 7;
y = 3;
z = mod(x,y);
disp(z); % Output: 1
```

These are just a few examples, but there are many more arithmetic operators available in MATLAB.Sure, here are some examples of arithmetic operators in MATLAB:

1. Addition (+):

```
x = 5;
y = 10;
z = x + y;
disp(z); % Output: 15
```

2. Subtraction (-):

```
x = 10;
y = 5;
z = x - y;
disp(z); % Output: 5
```

3. Multiplication (*):

```
x = 2;
y = 3;
z = x * y;
disp(z); % Output: 6
```

4. Division (/):

```
x = 6;
y = 3;
z = x / y;
disp(z); % Output: 2
```

5. Exponentiation (^):

```
x = 2;
y = 3;
z = x ^ y;
disp(z); % Output: 8
```

6. Modulo (%):

```
x = 7;
y = 3;
z = mod(x,y);
disp(z); % Output: 1
```

Sure, here are some examples of how to use relational operators in MATLAB:

1. Greater Than (`>`) and Less Than (`<`) operators:

```
a = 5;
b = 7;

if a < b
    disp('a is less than b');
    end

    if b > a
        disp('b is greater than a');
        end
        ```

        Output:
        ```
        a is less than b
        b is greater than a
        ```

        2. Greater Than or Equal To (`>=`) and Less Than or Equal To (`<=`) operators:

        ```
        a = 5;
        b = 7;

        if a <= b
            disp('a is less than or equal to b');
            end

            if b >= a
                disp('b is greater than or equal to a');
                end
                ```

                Output:
                ```
                a is less than or equal to b
                b is greater than or equal to a
                ```

                3. Equality (`==`) and Inequality (`~=`) operators:

                ```
                a = 5;
                b = 7;

                if a == b
                    disp('a is equal to b');
                    else
                        disp('a is not equal to b');
                        end

                        if a ~= b
                            disp('a is not equal to b');
                            else
                                disp('a is equal to b');
                                end
                                ```

                                Output:
                                ```
                                a is not equal to b
                                a is not equal to b
                      ```
                    ## example  
calculate the area and circumference of a circle with a radius of 5 cm.

% Define the radius
r = 5;

% Calculate the area and circumference
area = pi * r^2;
circumference = 2 * pi * r;

% Display the results
disp('Area of the circle: ');
disp(area);
disp('Circumference of the circle: ');
disp(circumference);

Example: Calculating the Mean and Standard Deviation of a Data Set

% Define the data set
data = [4, 8, 15, 16, 23, 42, 5, 9, 17, 29];

% Calculate the mean
mean_val = mean(data);
disp(mean_val); % Output: 17.9

% Calculate the standard deviation
std_val = std(data);
disp(std_val); % Output: 11.1423



