---
layout: page
title: "Mini Project: String Manipulation Tool"
description: Learn how to use the SUM function and AutoSum in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
author: Muhammad Yasir Bhutta
course: python
topic: mini-projects
show_toc: false
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Mini Projects
    url: /python/mini-projects/
---

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

