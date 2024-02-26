# Introduction to MATLAB

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/matlab/docs/matlab-basics.pdf)

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

**Example #1:** Find the value of z for the expression z = 2x+y, if x=5 and y=7.


```matlab
% Given values
x = 5;
y = 7;

% Expression for z
z = 2*x + y;
```

**Example #2:** Find the value of z for the expression z = (3x + 2y) / 4, if x=10 and y=5.


```matlab
% Given values
x = 10;
y = 5;

% Expression: z = (3x + 2y) / 4
z = (3*x + 2*y) / 4;
```

**Example #3:** Find the value of q for the expression q = x^2 + 2xy + y^2, if x=2 and y=3.

```matlab
% Given values
x = 2;
y = 3;

% Expression: q = x^2 + 2xy + y^2
q = x^2 + 2*x*y + y^2;
```

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

## Some Useful MATLAB Commands

### General Commands

**date:**
**ver:**

### Directory Commands

ls:

### Workspace Commands

who
whos
clear all
clc
clf

### Help commands

help
helpwin
help topic
doc
lookfor


## Key Terms

## True/False (Mark T for True and F for False)

- The clc command clears the command history. **True or False**
- The workspace stores all variables and their values during a session. **True or False**

## Multiple Choice (Select the best answer)

> Which of the following statements is TRUE about MATLAB?
1. [ ] It's an open-source programming language.
2. [ ] It's specifically designed for engineers and scientists
3. [ ] It cannot be used for data visualization.

> What does the ans variable represent in MATLAB?
1. [ ] A user-defined variable.
2. [ ] A temporary storage for implicit output.
3. [ ] A specific function for mathematical calculations.
4. [ ] A keyword for accessing the command history.

 > What does MATLAB stand for?

1. [ ] Mathematical Analysis Tool Box
2. [ ] Matrix Laboratory
3. [ ] Machine Learning Application Tool
4. [ ] Multi-function Analysis Language

> What is the purpose of the clc command in MATLAB?

1. [ ] Clear the command history
2. [ ] Close the current figure window
3. [ ] Clear all variables in the workspace
4. [ ] Clear the screen and display a new prompt

> What is the difference between the who and whos commands in MATLAB?
1. [ ] who displays all variables, while whos shows detailed information like size and class.
2. [ ] who shows only numeric variables, while whos displays all variable types.
3. [ ] who is used for clearing the workspace, and whos displays the command history.
4. [ ] There is no difference; both commands do the same thing.

> What is the primary function of the help command in MATLAB?
1. [ ] To display the current working directory.
2. [ ] To provide information and documentation about MATLAB functions, commands, and syntax.
3. [ ] To save the current state of the workspace.
4. [ ] To clear the command window and history.

> What does the "doc" command do in MATLAB?
1. [ ] Displays a list of available functions.
2. [ ] Opens the MATLAB documentation browser.
3. [ ] Prints the source code of a function.
4. [ ] Provides examples of MATLAB code.

> How is the helpwin command different from the help command in MATLAB?
1. [ ] helpwin displays help text in a separate window, while help displays help text in the Command Window
2. [ ] helpwin is used for accessing documentation of built-in functions, while help is used for custom functions
3. [ ] There is no difference; both commands provide the same functionality
4. [ ] helpwin is used for accessing toolbox documentation, while help is used for accessing function documentation

> What does the "ver" command in MATLAB do?
1. [ ] Verifies the syntax of a MATLAB script
2. [ ] Verifies the version of MATLAB currently installed
3. [ ] Verifies the integrity of MATLAB's installation files
4. [ ] Verifies the licensing information of MATLAB

> Which command in MATLAB clears only the command window and doesn't affect the workspace?
1. [ ] clc
2. [ ] clear
3. [ ] close all
4. [ ] delete

> What does the "clear all" command do in MATLAB?
1. [ ] Clears the command window
2. [ ] Removes all variables from the workspace
3. [ ] Deletes all files in the current directory
4. [ ] Exits MATLAB session

> What does the "doc" command do in MATLAB?
1. [ ] Displays the content of a variable
2. [ ] Opens the MATLAB documentation browser with the specified topic
3. [ ] Clears the current command window
4. [ ] Executes a predefined MATLAB script

## Fill in the Blanks

- The keyword ________ displays all currently defined variables in the workspace. (who)

## Exercises

## Review Questions

- What is MATLAB and what is its primary area of application?
- List the major components of the MATLAB enivornmnet?
- What is the difference between who and whos commands?
- What is a script file?
- What is the workspace in MATLAB, and what is its purpose?
- What is the primary function of the command window in MATLAB
- What is the purpose of the command history?
- What is the purpose of the semicolon (;) and the comment symbol (%) in MATLAB code?

**Answer:**

**Semicolon (;):**

- Separates statements: Primarily, the semicolon separates multiple statements on a single line. Each statement after the semicolon is executed independently. For example:

```matlab
a = 5; b = a^2;
```
Suppresses output: When placed at the end of a line, the semicolon suppresses the output of that specific line in the command window. This is useful if you want to perform calculations but don't need to see the intermediate results. 

**Comment symbol (%):**

Marks non-executable text: Anything following the percent sign (%) on the same line is considered a comment and is ignored by MATLAB during execution. This allows you to add notes, explanations, or reminders within your code, improving readability and maintainability.

## References and Bibliography

[1] Raj Kumar Bansal, A. K. Goel, and Manoj Kumar Sharma, MATLAB and its applications in engineering : [based iôn MATLAB 7.5 (R2007b)]. Delhi: Pearson, 2012.
‌
‌