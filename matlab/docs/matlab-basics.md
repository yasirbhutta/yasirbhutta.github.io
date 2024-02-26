# Introduction to MATLAB

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)


## Introduction

- MATLAB stands for Matrix Laboratory. 
- It's a proprietary (paid) programming platform specifically designed for engineers and scientists. 
- It allows users to analyze data, create data visualizations, develop algorithms, and create models.
  
## Command Window

- In MATLAB, the Command Window is your interactive workspace. It's like a command center where you can directly interact with the software. 
- The Command Window displys the command prompt `>>` and a cursor where commands are entered and are excutated instantaneously on pressing the `Enter` key of the keyboard.

**What is the ans variable?** 

- Think of ans as a temporary "holding area" that MATLAB automatically creates under specific conditions.
- Whenever you execute a command or function without assigning the output to a named variable, the result gets stored in ans.

```matlab
result = sin(pi/2); % `result` stores the output (1) explicitly
2 + 3 * 4;          % `ans` holds the implicit output (14)
```
In the second line, since we didn't assign the calculation (14) to a specific variable, it goes into the ans variable.

**Start with a clean slate:**

```matlab
clc
```
the `clc` command clears any previous commands or outputs from the window, giving you a fresh start.

**Example 1.1** from book [1].

## Command History Window

- The Command History Window consists of a list of all the commands that are entered in the Command Window.

## Workspace

- A workspace is a collection of all the variables that have been generated so far in the current MATLAB session and shows their data type and size.
- 

**Check the current workspace:**

```matlab
who
```

The who command shows you a list of all the currently defined variables and their values in the workspace.

## Key Terms

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

## Fill in the Blanks

## Exercises

## Review Questions

## References and Bibliography

[1] Raj Kumar Bansal, A. K. Goel, and Manoj Kumar Sharma, MATLAB and its applications in engineering : [based iôn MATLAB 7.5 (R2007b)]. Delhi: Pearson, 2012.
‌
‌