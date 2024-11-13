# Python: String Methods

- [Find Occurrences in Strings Effortlessly with Python's Count Method](https://www.youtube.com/watch?v=jWl8oWwEnzA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=75)
- [How to Replace the Second Occurrence of a Character in a String](https://www.youtube.com/watch?v=N7r1L5qpVKw&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=38)
- [String swapcase() Method](https://www.youtube.com/watch?v=Lj-LxOx3HBI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=26)

**Python str examples:**
- [How to Reverse a String in Python](https://www.youtube.com/watch?v=oD9Sfa-9uHU&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=44)
- [Generate Random 4-Digit PIN Code in Python](https://www.youtube.com/watch?v=93S_k3QIOAw)

# Fix the error

**Problem Statement:** [Python Quiz #66]

You are given a Python program that extracts and prints the last letter of a given name, "Ahmad". However, the program contains a potential issue related to how string indexing is handled. Analyze the code and correct any possible errors related to the string indexing.

The code provided is:

```python
name = "ahmad"
last_letter = name[5]
print(last_letter)
```

**Task:**
- Identify and describe the problem with the above code.
- Modify the code so that it prints the last letter of the name correctly.
## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()

What is the output of the following Python code? [Python Quiz #9]

def is_palindrome(s):
  return s == s[::-1]

is_palindrome("racecar")?

**A)** True
**B)** False
**C)** SyntaxError
**D)** None of these

**Watch this video for the answer:** [https://youtube.com/shorts/fYpVM6Tqf50?si=yyjM17NMUt5al1Bb](https://youtube.com/shorts/fYpVM6Tqf50?si=yyjM17NMUt5al1Bb)
  
What is the output of the following Python code? [Python Quiz #17]
```python
a = "Python is awesome"
print(a.find("is"))
```
- A) -1
- B) 0
- C) 7
- D) 2

**Watch this video for the answer:** [https://youtube.com/shorts/6rZpvEfzWf4](https://youtube.com/shorts/6rZpvEfzWf4)

**What is the output of the following code? [Python Quiz #27]**
```python
a = "hello world"
print(a[-5:-2])
```

- A)orl
- B)wor
- C)rld
- D)ld

**Watch this video for the answer:** [https://youtube.com/shorts/kLrdURzJ1Uk?si=N6LKU3v2ikrmgaFu](https://youtube.com/shorts/kLrdURzJ1Uk?si=N6LKU3v2ikrmgaFu)

**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

3. **Problem Statement:** Write a Python function `find_length` that takes a string input `word` and returns the length of the word by counting the number of characters in it. You are not allowed to use the built-in `len()` function.

**Function Signature:**
```python
def find_length(word: str) -> int:
```
**Input:**
- A string `word` which can contain letters, spaces, or special characters.
**Output:**
- The function returns an integer representing the total number of characters in the input string.
**Sample Input and Output:**
**Input:**
```python
find_length("python language")
```
**Output:**
```
15
```

- [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=wKuKX8-at5E&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=22)


Coding Challenge #1
You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length of all the words you use. It is up to you to figure out how long each word is and to average it out.

Task: 
Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number.

Input Format: 
A string containing multiple words.

Output Format: 
A number representing the average length of each word, rounded up to the nearest whole number.

Sample Input: 
this phrase has multiple words

Sample Output: 
6

Explanation:
The string in question has five words with a total of 26 letters (spaces do not count). The average word length is 5.20 letters, rounding it up to the nearest whole numbers results in 6.


import math
str1 = "this phrase has multiple words"

str_len = 0

words = str1.split()

for w in words:
    str_len += len(w)

result = math.ceil(str_len/len(words))

print(result)

## Review Questions

## References and Bibliography

30. **Replace vowels in a string with an asterisk**: Use a `for` loop to replace all vowels in the string "Replace all vowels" with '*'.

3. **Print each character in a string**: Write a `for` loop to iterate through the string "Hello, World!" and print each character.
7. **Reverse a string**: Use a `for` loop to reverse the string "Python".
8. 17. **Count vowels in a string**: Use a `for` loop to count the number of vowels in the string "Hello, World!".
25. **Count occurrences of a character in a string**: Use a `for` loop to count the number of times the letter 'l' appears in "Hello, World!".
27. **Find the length of each word in a sentence**: Use a `for` loop to find and print the length of each word in the sentence "The quick brown fox".
9.  **Print the reverse of each word in a string**: Use a `for` loop to reverse each word in the string "Hello World" and print it as "olleH dlroW".
10. **Count occurrences of a character in a string**: Use a `for` loop to count the number of times the letter 'l' appears in "Hello, World!".
11. **Find the length of each word in a sentence**: Use a `for` loop to find and print the length of each word in the sentence "The quick brown fox".
12. **Replace vowels in a string with an asterisk**: Use a `for` loop to replace all vowels in the string "Replace all vowels" with '*'.
13. **Calculate the average length of words in a sentence**: Use a `for` loop to calculate the average length of words in the sentence "Calculate the average length of words in this sentence".
14. **Count the number of consonants in a string**: Use a `for` loop to count the number of consonants in the string "Count the number of consonants".

### Question 4
**What will the output be for the following code?**
```python
for letter in "Python":
    print(letter)
```
A) P\ny\nt\nh\no\nn

B) Python

C) P y t h o n

D) P\ny\nt\nh\no\n

*Explanation:* The `for` loop iterates over each character in the string "Python", printing them one by one.

**Answer:** A

---
