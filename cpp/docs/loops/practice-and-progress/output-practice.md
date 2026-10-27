---
layout: page
title: "C++ Loops: Output Practice Questions"
description: "Practice C++ output basics with beginner-friendly questions on cout, variables, arithmetic expressions, and predicting console output in simple programs."
keywords: C++ output basics, cout in C++, C++ console output, predicting output in C++, print variable values in C++, arithmetic output in C++, beginner C++ exercises, C++ programming practice, output practice questions, C++ tutorial for beginners
---

## Instructions for Students

1. Read the program carefully.
2. Predict the output without running the code.
3. Write your predicted output.
4. Run the program to verify your answer.
5. Understand why the output appears.
6. Modify the code and predict the new output.

---

# Contents

- [While Loop](#section-1-while-loop)
- [Nested Loop](#section-2-nested-loops)

# Section 1: While Loop

<!-- ## Beginner Level -->

## Question 1:

**Task:** Predict the output.

### Code

```cpp
int i = 2;

while (i <= 6)
{
    cout << i * i << " ";
    i++;
}
```

## Question 2:

**Task:** Predict the output.

### Code

```cpp
int n = 20;

while (n >= 5)
{
    cout << n << " ";
    n -= 5;
}
```

## Question 3:

**Task:** Predict the output.

### Code

```cpp
int i = 1;

while (i <= 4)
{
    cout << i << " ";
    i += 2;
}
```

## Question 4:

**Task:** Predict the output.

### Code

```cpp
int i = 1;

while (i <= 3)
{
    cout << "CS" << i << " ";
    i++;
}
```

## Question 5:

**Task:** Predict the output.

### Code

```cpp
int x = 2;

while (x <= 8)
{
    cout << x - 1 << " ";
    x += 3;
}
```

## Question 6:

**Task:** Predict the output.

### Code

```cpp
int i = 4;

while (i >= 1)
{
    cout << i % 2 << " ";
    i--;
}
```

## Question 7:

**Task:** Predict the output.

### Code

```cpp
int x = 1;

while (x <= 4)
{
    cout << x + 3 << " ";
    x++;
}
```

## Question 8:

**Task:** Predict the output.

### Code

```cpp
int n = 3;

while (n > 0)
{
    cout << n * 2 << " ";
    n--;
}

cout << "Done";
```

<!-- ## Intermediate Level -->

## Question 9:

**Task:** Predict the output.

### Code

```cpp
int x = 2;
int sum = 0;

while (x <= 8)
{
    sum += x;
    x += 2;
}

cout << sum;
```

## Question 10:

**Task:** Predict the output.

### Code

```cpp
int n = 1;
int result = 1;

while (n <= 4)
{
    result += n * 3;
    n++;
}

cout << result;
```

## Question 11:

**Task:** Predict the output.

### Code

```cpp
int x = 1;

while (x <= 8)
{
    if (x % 3 == 0)
        cout << x << " ";

    x++;
}
```

## Question 12:

**Task:** Predict the output.

### Code

```cpp
int x = 10;

while (x > 0)
{
    x -= 3;
    cout << x << " ";
}
```

## Question 13:

**Task:** Predict the output.

### Code

```cpp
int n = 2;
int count = 0;

while (n <= 12)
{
    if (n % 4 == 0)
        count++;

    n += 2;
}

cout << count;
```

## Question 14:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int y = 8;

while (x <= 4)
{
    cout << x + y << " ";
    x++;
    y -= 2;
}
```

## Question 15:

**Task:** Predict the output.

### Code

```cpp
int n = 1;

while (n <= 5)
{
    if (n == 3)
        cout << "Three ";
    else
        cout << n << " ";

    n++;
}
```

## Question 16:

**Task:** Predict the output.

### Code

```cpp
int x = 2;
int product = 1;

while (x <= 6)
{
    product *= x;
    x += 2;
}

cout << product;
```

## Question 17:

**Task:** Predict the output.

### Code

```cpp
int n = 5;

while (n >= 1)
{
    if (n % 2 == 1)
        cout << n * 2 << " ";

    n--;
}
```

## Question 18:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int total = 0;

while (x <= 4)
{
    total += x * x;
    x++;
}

cout << total;
```

<!-- ## Upper-Intermediate Level -->

## Question 19:

**Task:** Predict the output.

### Code

```cpp
int x = 1;

while (x <= 5)
{
    cout << x << " ";

    if (x % 2 == 0)
        cout << "Even ";

    x++;
}
```

## Question 20:

**Task:** Predict the output.

### Code

```cpp
int n = 1;
int value = 2;

while (n <= 4)
{
    value += n;
    cout << value << " ";
    n++;
}
```

## Question 21:

**Task:** Predict the output.

### Code

```cpp
int n = 246;
int sum = 0;

while (n > 0)
{
    sum += n % 10;
    n /= 10;
}

cout << sum;
```

## Question 22:

**Task:** Predict the output.

### Code

```cpp
int n = 1357;

while (n > 0)
{
    cout << n % 10 << " ";
    n /= 100;
}
```

## Question 23:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int y = 2;

while (x <= 4)
{
    y += x;
    x++;

    if (y > 5)
        cout << y << " ";
}
```

## Question 24:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int count = 0;

while (x <= 10)
{
    if (x % 2 == 0 && x % 3 != 0)
        count++;

    x++;
}

cout << count;
```

## Question 25:

**Task:** Predict the output.

### Code

```cpp
int x = 1;

while (x <= 4)
{
    int y = x;

    while (y > 0)
    {
        cout << y << " ";
        y--;
    }

    x++;
}
```

<!-- ## Advanced Level -->

## Question 26:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int y = 10;

while (x < y)
{
    cout << x * y << " ";
    x += 2;
    y -= 3;
}
```


## Question 27:

**Task:** Predict the output.

### Code

```cpp
int n = 12345;
int result = 0;

while (n > 0)
{
    int digit = n % 10;

    if (digit % 2 == 1)
        result += digit;

    n /= 10;
}

cout << result;
```



## Question 28:

**Task:** Predict the output.

### Code

```cpp
int x = 2;
int total = 0;

while (x <= 10)
{
    if (x % 4 == 0)
        total += x;
    else
        total -= 1;

    x += 2;
}

cout << total;
```

## Question 29:

**Task:** Predict the output.

### Code

```cpp
int n = 5;
int result = 0;

while (n > 0)
{
    result = result * 2 + n;
    n -= 2;
}

cout << result;
```


## Question 30:

**Task:** Predict the output.

### Code

```cpp
int n = 9876;
int reversed = 0;

while (n > 0)
{
    reversed = reversed * 10 + n % 10;
    n /= 10;
}

cout << reversed;
```

## Question 31:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int result = 0;

while (x <= 6)
{
    if (x % 2 == 0)
        result += x * 2;
    else
        result += x;

    x++;
}

cout << result;
```

## Question 32:

**Task:** Predict the output.

### Code

```cpp
int n = 1;
int sum = 0;

while (n <= 20)
{
    if (n % 4 == 0 || n % 6 == 0)
        sum += n;

    n++;
}

cout << sum;
```


## Question 33:

**Task:** Predict the output.

### Code

```cpp
int n = 2;
int count = 0;

while (n <= 50)
{
    if (n % 7 == 0 && n % 2 == 0)
        count++;

    n += 2;
}

cout << count;
```

# Section 2: Nested Loops

## Question 1:

**Task:** Predict the output.

### Code

```cpp
int x = 1;

while (x <= 3)
{
    int y = 3;

    while (y >= 1)
    {
        cout << x * y << " ";
        y--;
    }

    x++;
}
```

<!-- ## Advanced Level -->

## Question 2:

**Task:** Predict the output.

### Code

```cpp
int n = 1;
int sum = 0;

while (n <= 3)
{
    int j = 1;

    while (j <= 3)
    {
        sum += n * j;
        j++;
    }

    n++;
}

cout << sum;
```

## Question 3:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int count = 0;

while (x <= 5)
{
    int y = x;

    while (y <= 5)
    {
        count++;
        y += 2;
    }

    x++;
}

cout << count;
```


## Question 4:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int y = 1;

while (x <= 4)
{
    y = 1;

    while (y <= x)
    {
        cout << x + y << " ";
        y++;
    }

    cout << endl;
    x++;
}
```

## Question 5:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int count = 0;

while (x <= 4)
{
    int y = 1;

    while (y <= 4)
    {
        if (x + y > 4)
            count++;

        y++;
    }

    x++;
}

cout << count;
```

## Question 6:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int result = 0;

while (x <= 4)
{
    int y = 1;

    while (y <= x)
    {
        result += x - y;
        y++;
    }

    x++;
}

cout << result;
```

## Question 7:

**Task:** Predict the output.

### Code

```cpp
int x = 1;
int y = 5;

while (x <= 3)
{
    int z = y;

    while (z >= x)
    {
        cout << z << " ";
        z--;
    }

    cout << endl;
    x++;
    y--;
}
```


**Practice tip:** Trace each loop iteration in a small table with columns for the variables, condition, and output. Pay special attention to when variables change and when the condition is checked again.