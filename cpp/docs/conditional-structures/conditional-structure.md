---
layout: page
title: "C++ Conditional Statements Explained: if, if-else, else-if, and Comparison Operators"
description: "Learn how C++ conditional statements work with if, if-else, else-if, and comparison operators through beginner-friendly examples and decision-making logic."
keywords: C++ conditional statements, C++ if statement, C++ if else statement, else if in C++, comparison operators in C++, nested if in C++, decision making in C++, C++ beginner programming, C++ tutorial, control flow in C++
---

## 1. What Is a Conditional Structure?

A conditional structure allows a program to make decisions. It checks a condition and executes the appropriate statement or block of code.

In real life, we make decisions every day.

[Ethics in Action – How to Decode Vignette-Based Ethics Questions on the National Psychology Exam](https://images.openai.com/static-rsc-4/nWpl84Uk-J1QXFtC_h4osTN_G7b6LjkrJbBorMqqfS-cQMW7UY7dlMDEaOTtZDtyDmkvgqjOK4n2PXELJ32ORTisecPMXs2QQLSn50oaOopn8KPwRtxv7Y8ku0jJuINs8IGOQ2Z0Jo492MQJLzsREIQ_3S4UCkQAYK7HtCROiJk?purpose=inline)

Example 1: Exam preparation

If a student prepares for an exam, the student may perform well.

[A girl with an umbrella is standing outside the window looking at me - SeaArt AI](https://images.openai.com/static-rsc-4/M98NkywChlTV_kiNCBTsRH1Nv_mywwKQEuBLca0NEd19Rp3lgvL9G660NpzOvz7RIWhF4oxy4MpDz5RXaLo2wFa3WUJY-D8m3SNRcvkhfJF8HE_Q0BsufjVSKDRzT8t2gc6QPCX1XM7TN5rGLT68yzGcifO_PwwWGb9DRDjTjG0?purpose=inline)

Example 2: Weather

If it is raining, take an umbrella.

[Retail employee counting cash at a register in a small business shop.](https://images.openai.com/static-rsc-4/V7VDuoHtxtYxOkJGF1jlrlfvCzvIHh1lLXIH8-ll_W41NBI1VJGQ8fg91Ea-Z256PNSDA65DYxdtpDpyLjj8FVV3JAXhhEIQkZEAuCcMtstcEnIyupWAJsjlEMRdtAuLDT6jTUFfqAlfqBVb1mAuI4bs3gtVx5rr4BwncaOuRCM?purpose=inline)

Example 3: Shopping

If you have enough money, you can buy the item.

Similarly, a C++ program can check a condition and decide which statements to execute.

## 3. What Is a Condition?

A condition is an expression that evaluates to either:

- `true` — the condition is satisfied.
- `false` — the condition is not satisfied.

For example:

```
age >= 18
```

If `age` is 20, the condition is true. If `age` is 15, it is false.

## 4. Comparison Operators

Comparison operators compare two values.

| Operator | Meaning                  | Example       |
| -------- | ------------------------ | ------------- |
| `==`     | Equal to                 | `age == 18`   |
| `!=`     | Not equal to             | `age != 18`   |
| `>`      | Greater than             | `marks > 50`  |
| `<`      | Less than                | `marks < 50`  |
| `>=`     | Greater than or equal to | `marks >= 50` |
| `<=`     | Less than or equal to    | `marks <= 50` |

Important: In C++, `=` assigns a value, while `==` compares two values.

```
age = 18;       // Assigns 18 to age
age == 18;      // Checks whether age equals 18
```
