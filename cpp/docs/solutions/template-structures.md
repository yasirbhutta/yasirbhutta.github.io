Let me explain the `TOPIC-TYPE-NUMBER` system with examples from your C++ Programming Fundamentals course.

The main idea is to give every coding exercise a unique, permanent identification number so that you can add new exercises anytime without renumbering existing exercises.

## 1. Understanding TOPIC-TYPE-NUMBER

Consider this exercise ID:

# LOOP-COD-001

LOOP

Topic

Loops

COD

Activity type

Coding Exercise

001

Unique number

First assigned ID

Each part has a specific purpose:

| Part   | Meaning | Explanation                                       |
| ------ | ------- | ------------------------------------------------- |
| `LOOP` | Topic   | Exercise belongs to Loops                         |
| `COD`  | Type    | It is a coding exercise                           |
| `001`  | Number  | Unique exercise number within this topic and type |

## 2. Define Topic Codes

Use consistent short codes for all C++ topics.

| Topic                  | Code     |
| ---------------------- | -------- |
| Introduction to C++    | `INTRO`  |
| Basics                 | `BAS`    |
| Input and Output       | `IO`     |
| Conditional Structures | `COND`   |
| Loops                  | `LOOP`   |
| Arrays                 | `ARR`    |
| Functions              | `FUNC`   |
| Structures             | `STRUCT` |

## 3. Define Activity Types

The second part identifies what students need to do.

| Code  | Activity          | Example                  |
| ----- | ----------------- | ------------------------ |
| `COD` | Coding Exercise   | Write a program          |
| `OUT` | Output Prediction | Predict program output   |
| `DBG` | Debugging         | Find and fix errors      |
| `MOD` | Code Modification | Modify existing code     |
| `PRA` | General Practice  | Solve practice questions |
| `PRO` | Problem Solving   | Solve real-life problems |

For example:

LOOP-COD-001
LOOP-OUT-001
LOOP-DBG-001
LOOP-MOD-001


## 4. How Numbering Works When Adding New Exercises

This is the most important part.

Suppose you initially create three exercises:

| Display order | Exercise ID    | Title                      |
| ------------- | -------------- | -------------------------- |
| 1             | `LOOP-COD-001` | Print numbers 1 to 10      |
| 2             | `LOOP-COD-002` | Print even numbers         |
| 3             | `LOOP-COD-003` | Print multiplication table |

Now you want to add an exercise between the first and second exercises.

Do not renumber existing exercises. Assign the next available number.

| Display order | Exercise ID    | Title                      |
| ------------- | -------------- | -------------------------- |
| 1             | `LOOP-COD-001` | Print numbers 1 to 10      |
| 2             | `LOOP-COD-004` | Print odd numbers          |
| 3             | `LOOP-COD-002` | Print even numbers         |
| 4             | `LOOP-COD-003` | Print multiplication table |

Important rule

The exercise ID represents identity, not display order.

You can change the display order anytime without changing exercise IDs.

## 5. How to Name Markdown Files

I recommend keeping filenames descriptive and avoiding sequential numbering.

Your existing folder structure could be:

```
docs/
├── loops/
│   ├── index.md
│   ├── for-loop.md
│   ├── while-loop.md
│   ├── do-while-loop.md
│   └── practice-and-progress/
│       ├── output-practice.md
│       ├── find-fix-mistakes.md
│       └── coding-exercises.md
│
└── solutions/
    └── loops/
        ├── output-solutions.md
        ├── debugging-solutions.md
        └── coding-exercise-solutions.md
```

Notice:

- `coding-exercises.md` contains student exercises.
- `coding-exercise-solutions.md` contains their solutions.
- Exercise IDs connect the two files.

## 6. Example: Exercise and Its Solution

Student exercise file: `loops/practice-and-progress/coding-exercises.md`

```
# C++ Loops: Coding Exercises

## Beginner Level

### LOOP-COD-001: Print Numbers from 1 to 10

Write a C++ program to print numbers from 1 to 10.

### LOOP-COD-002: Print Even Numbers

Write a C++ program to print even numbers from 1 to 20.

### LOOP-COD-003: Multiplication Table

Write a C++ program to display the multiplication table of a number.
```

Solution file: `solutions/loops/coding-exercise-solutions.md`

````
# C++ Loops: Coding Exercise Solutions

## LOOP-COD-001: Print Numbers from 1 to 10

### Solution

​```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        cout << i << endl;
    }
    return 0;
}
​```

## LOOP-COD-002: Print Even Numbers

### Solution

​```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 2; i <= 20; i += 2) {
        cout << i << endl;
    }
    return 0;
}
​```
````

Both files use exactly the same exercise IDs.

## 7. Rules to Follow in Your Repository

I recommend adopting these rules as your permanent course documentation standard.

| Rule                | Standard                                   |
| ------------------- | ------------------------------------------ |
| Exercise ID format  | `TOPIC-TYPE-NUMBER`                        |
| Number format       | Three digits (`001`, `002`, `003`)         |
| Numbering sequence  | Separate for each topic and activity type  |
| New exercise        | Assign next unused number                  |
| Exercise deletion   | Never reuse deleted IDs                    |
| Exercise reordering | Change display position only               |
| Solution reference  | Use the same exercise ID                   |
| Markdown filenames  | Descriptive names, no sequential numbering |

## 8. Final Example Across Your Course

| Exercise ID    | Description                   |
| -------------- | ----------------------------- |
| `BAS-COD-001`  | Declare and display variables |
| `IO-COD-001`   | Calculate sum of two numbers  |
| `COND-COD-001` | Check even or odd             |
| `COND-OUT-001` | Predict if-else output        |
| `LOOP-COD-001` | Print numbers 1 to 10         |
| `LOOP-OUT-001` | Predict while-loop output     |
| `LOOP-DBG-001` | Fix errors in a for loop      |
| `ARR-COD-001`  | Calculate array sum           |
| `FUNC-COD-001` | Create an addition function   |

My suggestion: Adopt `TOPIC-TYPE-NUMBER` as the official identification standard for all your CS-303 Programming Fundamentals learning materials.

One more benefit: later, you can use these IDs to connect exercises with quizzes, lab tasks, assignments, solutions, and student progress tracking without changing the original IDs.