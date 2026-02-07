---
layout: page
title: Custom function to escape HTML special characters
description: In Python 3.14, t-strings (template strings) are a newly introduced feature designed to enhance the safety and flexibility of string formatting, parti...
keywords: template, strings, string, str, name
---
In Python 3.14, t-strings (template strings) are a newly introduced feature designed to enhance the safety and flexibility of string formatting, particularly in contexts where security is paramount.  They are defined using the t prefix, similar to how f-strings use the f prefix.  Unlike f-strings, which interpolate expressions immediately, t-strings defer evaluation, allowing for safer handling of user input and integration with templating systems. 


---

🔍 What Are T-Strings?

T-strings are defined using the t prefix and evaluate to instances of the Template class from the string.templatelib module.  This design allows developers to process and sanitize interpolated values before rendering the final string, mitigating risks such as SQL injection and cross-site scripting (XSS) attacks. 

Example:

from string.templatelib import Template

name = "Alice"
template = t"Hello, {name}!"



In this example, template is a Template object that can be safely processed before rendering. 


---

🛡️ Why Use T-Strings?

T-strings are particularly useful in scenarios where interpolated values come from untrusted sources.  By deferring evaluation, developers can implement custom processing functions to sanitize or transform these values, enhancing security and flexibility. 

Example:

def html_escape(template: Template) -> str:
    # Custom function to escape HTML special characters
    ...

user_input = "<script>alert('XSS')</script>"
template = t"<p>{user_input}</p>"
safe_output = html_escape(template)



In this scenario, html_escape would process the Template object, escaping any potentially dangerous characters before rendering the final HTML. 


---

🔄 T-Strings vs. F-Strings


---

🧑‍💻 Beginner Examples

Basic Usage:

from string.templatelib import Template

name = "Bob"
template = t"Welcome, {name}!"



Processing the Template:

def render_template(template: Template) -> str:
    # Simple renderer that replaces placeholders with values
    return "".join(
        part if isinstance(part, str) else str(part.value)
        for part in template
    )

output = render_template(template)
print(output)  # Output: Welcome, Bob!




---

🌐 Real-World Examples

1. Generating HTML with Escaped User Input:

def html_escape(template: Template) -> str:
    # Function to escape HTML special characters
    ...

user_input = "<b>Important</b>"
template = t"<div>{user_input}</div>"
safe_html = html_escape(template)



2. Creating SQL Queries Safely:

def sql_escape(template: Template) -> str:
    # Function to safely construct SQL queries
    ...

user_input = "O'Reilly"
template = t"SELECT * FROM authors WHERE name = '{user_input}'"
safe_query = sql_escape(template)



3. Logging with Deferred Evaluation:

import logging

def log_template(template: Template):
    # Custom logging function
    ...

user_action = "deleted"
template = t"User {user} has {user_action} a record."
log_template(template)




---

T-strings in Python 3.14 provide a powerful tool for developers to handle string interpolation securely and flexibly.  By deferring evaluation and allowing custom processing, they address common security concerns associated with immediate string formatting methods like f-strings. 

For a more in-depth exploration of t-strings and their applications, you might find the following video insightful: 

