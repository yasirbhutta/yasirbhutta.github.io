---
layout: page
title: "String Manipulation Tool: Python Project for String Operations and Formatting"
description: Explore a Python-based String Manipulation Tool to reverse strings, change case, count vowels, replace substrings, and more. Learn essential string operations and formatting in Python with this interactive mini project.
keywords: Python string manipulation, Python project, string operations, reverse string, count vowels, string formatting, Python string methods, interactive Python tool, palindrome checker, string replace, word count, Python tutorial, string case conversion, remove extra spaces, title case formatting, Python beginner project
author: "Muhammad Yasir Bhutta"
toc: toc/python-toc.html
topic: "strings"
course: "python"
prev: "/python/docs/strings/practice-and-progress/exercises-strings.html"
next: "/python/docs/strings/practice-and-progress/review-questions-strings.html"
---

## **1. Project: String Manipulation Tool**

#### **Objective:**
Create an interactive console-based tool that allows users to input strings and perform various string operations, such as reversing, formatting, replacing substrings, counting occurrences of characters, and more.

#### **Features:**
1. **Reverse a String**  
   Allow the user to input a string and reverse it.

2. **Convert to Uppercase and Lowercase**  
   Provide options to convert the string to either all uppercase or all lowercase.

3. **Count Vowels and Consonants**  
   Count and display the number of vowels and consonants in the input string.

4. **Replace a Substring**  
   Allow the user to replace a specific substring within the string with another substring.

5. **Format Title Case**  
   Convert the input string into title case (capitalize the first letter of each word).

6. **Remove Extra Spaces**  
   Remove any extra spaces from the input string, ensuring only single spaces between words.

7. **Check for Palindrome**  
   Check if the string is a palindrome, ignoring spaces, punctuation, and case sensitivity.

8. **Word Count**  
   Count and display the number of words in the input string.

#### **How the Tool Works:**
1. **User Input:** The tool will prompt the user to enter a string of their choice.
2. **Select Operation:** The user can select from the listed string operations by choosing the corresponding number.
3. **Display Result:** The result of the selected operation will be displayed immediately, and the user can perform additional operations or exit the tool.
4. **Exit:** The tool will continue to run until the user decides to exit.

#### **Example Interaction:**
```
Welcome to the String Manipulation Tool!
Choose an operation:
1. Reverse a string
2. Convert to uppercase
3. Convert to lowercase
4. Count vowels and consonants
5. Replace a substring
6. Format title case
7. Remove extra spaces
8. Check if the string is a palindrome
9. Count words in a string
10. Exit
Enter the number of your choice: 1
Enter a string: Hello, World!
Reversed string: !dlroW ,olleH
```

Absolutely! Here's a beginner-friendly **Mini Project** based on string formatting that ties together the concepts of `find()`, `replace()`, `split()`, and `partition()`.

---

## 🎯 **2. Mini Project: String Formatter Toolkit**

### 📖 **Objective**

To build a **menu-driven Python program** that allows users to perform different string operations like:
- Finding a substring
- Replacing words
- Splitting into words
- Partitioning a string

This helps students:
- Practice string manipulation
- Write interactive programs
- Use conditionals and loops

---

### 🛠️ **Features to Implement**

1. **Input a sentence**
2. **Display a menu with options:**
   ```
   1. Find a word
   2. Replace a word
   3. Split into words
   4. Partition at a word
   5. Exit
   ```

3. **Perform the operation based on user choice**
4. **Repeat until the user chooses to exit**

---

### 🧑‍💻 **Sample Code Skeleton**

```python
print("Welcome to the String Formatter Toolkit!")
sentence = input("Enter a sentence: ")

while True:
    print("\nWhat would you like to do?")
    print("1. Find a word")
    print("2. Replace a word")
    print("3. Split into words")
    print("4. Partition at a word")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        word = input("Enter the word to find: ")
        pos = sentence.find(word)
        if pos != -1:
            print(f"'{word}' found at position {pos}")
        else:
            print(f"'{word}' not found.")

    elif choice == '2':
        old = input("Word to replace: ")
        new = input("New word: ")
        sentence = sentence.replace(old, new)
        print("Updated sentence:", sentence)

    elif choice == '3':
        words = sentence.split()
        print("Words in sentence:", words)

    elif choice == '4':
        sep = input("Enter the word to partition by: ")
        before, middle, after = sentence.partition(sep)
        print("Before:", before)
        print("Separator:", middle)
        print("After:", after)

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
```

---

### 📝 **Expected Output Example**

```
Welcome to the String Formatter Toolkit!
Enter a sentence: Python is easy and fun to learn

What would you like to do?
1. Find a word
2. Replace a word
3. Split into words
4. Partition at a word
5. Exit
Enter your choice (1-5): 1
Enter the word to find: fun
'fun' found at position 19
```

---

### 📚 **Learning Outcomes**

- Understand and apply string methods (`find`, `replace`, `split`, `partition`)
- Use loops and conditionals effectively
- Build confidence writing interactive programs

---

