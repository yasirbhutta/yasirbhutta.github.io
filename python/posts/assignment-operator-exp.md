# Understanding Assignment in Python: Why = Can't Be Used in Expressions and How := Solves It


No, the assignment operator (=) cannot be used inside expressions in Python. Unlike some other languages like C or JavaScript, Python does not allow assignments within expressions.

Example (Invalid Code)

if (x = 10):  # ❌ SyntaxError
    print(x)

This will result in a SyntaxError because = is an assignment operator, not an expression.


---

How to Assign Values Inside Expressions?

To allow assignments within expressions, Python introduced the walrus operator (:=) in Python 3.8.

Example Using Walrus Operator (:=)

if (x := 10) > 5:
    print(f"x is {x}")  # ✅ This works

This assigns 10 to x and checks if it's greater than 5 in a single step.



