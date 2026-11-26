# **7. Introduction to Two-Dimensional Arrays**

## **7.1 Problem**

Suppose we want to store marks of three students in two subjects:

- English
- Computer

A one-dimensional array stores values in a single row.

A two-dimensional array stores values in rows and columns.

## **7.2 Understand the Structure**

**Two-dimensional array**

| **Student** | **English** | **Computer** |
| ----------- | ----------- | ------------ |
| 1           | 75          | 80           |
| 2           | 85          | 90           |
| 3           | 65          | 70           |

Three rows and two columns

## **7.3 Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks[3][2] = {
        {75, 80},
        {85, 90},
        {65, 70}
    };

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout << marks[i][j] << " ";
        }

        cout << endl;
    }

    return 0;
}
```

## **7.4 Understand the Code**

**Step 1: Declare a two-dimensional array**

```
int marks[3][2];
```

- `3` represents the number of rows.
- `2` represents the number of columns.

**Step 2: Understand array indexes**

```
marks[0][0]
```

This accesses the first row and first column.

```
marks[1][0]
```

This accesses the second row and first column.

```
marks[2][1]
```

This accesses the third row and second column.

**Step 3: Use the outer loop**

```
for (int i = 0; i < 3; i++)
```

This loop controls the rows.

**Step 4: Use the inner loop**

```
for (int j = 0; j < 2; j++)
```

This loop controls the columns.

**Step 5: Display elements**

```
cout << marks[i][j] << " ";
```

This displays the element at the current row and column.

## **7.5 Dry Run**

| i (Row) | j (Column) | Value |
| ------- | ---------- | ----- |
| 0       | 0          | 75    |
| 0       | 1          | 80    |
| 1       | 0          | 85    |
| 1       | 1          | 90    |
| 2       | 0          | 65    |
| 2       | 1          | 70    |

## **7.6 Modify the Code**

1. Take marks from the user using `cin`.
2. Increase the number of students from 3 to 5.
3. Calculate the total marks of each student.
4. Calculate the average marks of each student.
5. Display the marks of a particular student.

