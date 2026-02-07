---
layout: page
title: Python 3.14's t-strings: A New Era in String Processing
description: Python 3.14's t-strings: A New Era in String Processing String formatting stands as a fundamental aspect of programming, enabling the dynamic creation...
keywords: strings, template, string, object, processing
---
Python 3.14's t-strings: A New Era in String Processing
String formatting stands as a fundamental aspect of programming, enabling the dynamic creation of textual output by embedding variables and expressions within predefined text. Python has historically provided various mechanisms for this purpose, starting with the % operator, evolving to the more versatile .format() method, and later introducing the highly readable and concise f-strings. Each subsequent method has generally offered increased readability and power, reflecting the language's commitment to developer experience. In this ongoing evolution, Python 3.14 introduces a new feature: template strings, often referred to as t-strings. This addition, formally proposed in PEP 750, is anticipated to ship with the release of Python 3.14 in late 2025. This report aims to provide a comprehensive understanding of t-strings, exploring their definition, purpose, advantages, distinctions from f-strings, and illustrative examples.
The introduction of t-strings indicates a continued emphasis on refining string manipulation capabilities within Python, likely motivated by the growing need for enhanced security and greater flexibility in handling textual data. Python's history of improving its string formatting tools demonstrates a clear trend towards more expressive and user-friendly syntax. The progression from older methods to f-strings highlights a focus on readability and power. Described as a generalization of f-strings, the arrival of t-strings suggests an effort to address specific limitations of existing approaches, particularly in scenarios demanding robust security measures and the ability to perform complex templating operations. Furthermore, the timing of this release provides the developer community with an opportunity to explore and understand this new feature early in its lifecycle. The availability of information and discussions around April 2025 about a feature expected to be released in late 2025 suggests a proactive approach to community engagement and feedback.
Delving into t-strings: Definition and Syntax
Template strings, or t-strings, are a new type of string literal introduced in Python 3.14. They are designed as a generalization of f-strings, aiming to provide a safer and more flexible approach to string processing. A key characteristic of t-strings is their use of the prefix t (or T) immediately before the opening quote of the string. Similar to f-strings, t-strings employ curly braces {} to denote placeholders where expressions or variable names can be embedded. For instance, one might define a t-string as t"Hello {name}" or t"The result is {2 + 2}".
However, a crucial distinction from f-strings lies in their evaluation. While f-strings are evaluated immediately to produce a standard string (str) object, t-strings evaluate to a new type: string.templatelib.Template. This Template object encapsulates the structure of the template string along with the interpolated values. Consequently, Template objects are not directly usable as strings and necessitate a further processing step, often referred to as rendering, to produce the final string output. This processing is typically performed by a separate function or library, allowing for the implementation of custom logic such as sanitization or transformation of the interpolated values before they are incorporated into the final string. Furthermore, the Template object provides access to its underlying components through properties like .strings, which returns a tuple of the static string parts, and .values, which returns a tuple of the interpolated values. For more detailed information about each interpolation, the .interpolations property can be used.
The choice of the t prefix for t-strings serves as a clear visual indicator, immediately distinguishing them from other types of string literals in Python code. This explicit prefix signals that the resulting object will be a Template instance, not a directly usable string, thereby setting the expectation that further processing will be required. The introduction of this intermediate Template object represents a fundamental aspect of t-string functionality. It is this intermediate representation that enables the deferred evaluation and the potential for custom processing, which are central to the advantages offered by t-strings.
The Rationale Behind t-strings: Purpose and Advantages
A primary motivation behind the introduction of t-strings is to enhance the security of Python applications, particularly when dealing with user-provided input. Directly interpolating untrusted data into strings, especially in contexts like constructing SQL queries or generating HTML content, can lead to security vulnerabilities such as SQL injection and cross-site scripting (XSS) attacks. The deferred evaluation inherent in t-strings addresses this concern by allowing for the sanitization of interpolated values before they are used in sensitive operations. For example, one can envision a function, perhaps named html(), that takes a Template object and returns a safely escaped HTML string, ensuring that any potentially malicious code within the interpolated values is rendered harmless.
Beyond security, t-strings offer increased flexibility in how string content can be processed. They enable more than just simple formatting; processing functions can be designed to return objects of different types based on the template content, such as a specialized HTMLElement object. They also facilitate more complex substitutions, such as directly embedding a dictionary of attributes into an HTML tag within the template. The ability to access the underlying structure of the Template object, including the raw string parts and the interpolated values via the .strings, .values, and .interpolations properties, provides a significant advantage. This access allows developers to implement custom processing logic tailored to the specific requirements of the template, as demonstrated by the example of a pig_latin() function that could operate on the interpolated words.
For developers familiar with JavaScript, the concept of t-strings might feel familiar as they bear a resemblance to JavaScript's tagged templates, which offer similar capabilities for custom string processing. This conceptual similarity can potentially ease the transition for developers working across both languages. Furthermore, t-strings inherently support deferred evaluation, meaning the final string is not produced until the Template object is explicitly processed. This lazy evaluation can be advantageous in various scenarios, such as internationalization (i18n) where the string might need to be processed based on the locale, or in logging where the final formatted string might only be necessary if a certain log level is reached.
The emphasis on security as a primary driver for t-strings highlights a crucial aspect of modern application development. The potential for misuse of f-strings with untrusted input has been recognized, and t-strings offer a mechanism to enforce a safer approach by separating template definition from value interpolation. This encourages developers to think more deliberately about how dynamic data is incorporated into strings, particularly in security-sensitive contexts. The flexibility afforded by t-strings positions them as a powerful tool for developers looking to build custom templating systems and even domain-specific languages within Python. The ability to manipulate the template structure and interpolated values before the final string is generated opens up a wide range of possibilities for creating more sophisticated and secure applications.
t-strings vs. f-strings: A Comparative Analysis
While both f-strings and t-strings offer convenient ways to embed expressions within string literals in Python, they differ significantly in their behavior and intended use cases. The most obvious difference lies in the prefix used to denote them: f-strings are prefixed with f or F, while t-strings use t or T.
A fundamental distinction between the two lies in their evaluation timing. F-strings are evaluated immediately when the line of code is executed, resulting in the direct creation of a str object. In contrast, t-strings undergo deferred evaluation, meaning they are not immediately converted to a string. Instead, they evaluate to a string.templatelib.Template object, which holds the template and the values to be interpolated. This difference in the resulting object type is critical and dictates their primary use cases. F-strings are generally employed for straightforward, readable string formatting tasks where immediate string creation is desired. T-strings, on the other hand, are designed for scenarios that demand enhanced security, custom processing of the interpolated values, or deferred evaluation, such as building templating engines or domain-specific languages.
Given their evaluation model, t-strings are inherently safer for handling user input compared to f-strings. The requirement for a separate processing step on the Template object allows for the implementation of sanitization or escaping logic before the final string is generated, mitigating the risks associated with directly injecting untrusted data. Furthermore, t-strings offer greater flexibility in string processing. The Template object can be manipulated in various ways, and the processing functions can be designed to return not just strings but other types of objects as well.
It is also useful to briefly consider how both f-strings and t-strings compare with older string formatting methods in Python, namely the % operator and the .format() method. For simple formatting tasks, f-strings are widely regarded as more readable and concise than these older approaches. T-strings, however, represent a different paradigm focused on processing rather than direct formatting. Their primary value lies in the control they offer over how string content is handled, making them not directly comparable to the older methods in terms of simplicity of basic formatting.
Feature
f-strings
t-strings (string.templatelib.Template)
Prefix
f or F
t or T
Evaluation
Eager (immediate)
Deferred (lazy)
Resulting Type
str
string.templatelib.Template
Primary Use Case
General string formatting, readability
Security, custom processing, templating
Security
Potential risks with untrusted input
Safer due to required processing
Flexibility
Primarily for string formatting
Higher flexibility for custom handling

The introduction of t-strings does not signify a replacement for f-strings. Instead, it provides an alternative tailored for specific scenarios where the benefits of deferred evaluation and custom processing are paramount. While t-strings build upon the syntax of f-strings, the fundamental difference in their evaluation and the resulting Template object necessitate a shift in how developers approach string manipulation in these contexts. Understanding the need for a separate rendering step and the capabilities offered by the Template object will be key to effectively utilizing this new feature.
Getting Started with t-strings: Beginner-Friendly Examples
For those new to t-strings, understanding their basic usage is the first step. Creating a t-string is straightforward and resembles the creation of an f-string, with the key difference being the t prefix. Consider the following example:
from string.templatelib import Template
name = "Beginner"
template: Template = t"Hello {name}!"
print(template)


Executing this code will not directly print "Hello Beginner!". Instead, it will output a representation of the Template object, similar to <string.templatelib.Template object at...>. This indicates that the template has been created but the actual substitution of the name variable has not yet occurred. To achieve the substitution and obtain the final string, a processing or rendering function is required. A simple rendering function can be defined as follows:
from string.templatelib import Template, Interpolation

def simple_render(template: Template) -> str:
    parts =
    for item in template:
        if isinstance(item, Interpolation):
            parts.append(str(item.value))
        else:
            parts.append(item)
        return "".join(parts)

name = "Beginner"
template: Template = t"Hello {name}!"
rendered_string = simple_render(template)
print(rendered_string)


In this simple_render function, the code iterates through the components of the Template object. If a component is an Interpolation object (representing a placeholder), its value is appended to a list. Otherwise, if it's a static part of the string, it's also appended. Finally, all the parts are joined together to form the rendered string. Running this code will now produce the output: Hello Beginner!.
T-strings can also accommodate multiple placeholders within a single template :
from string.templatelib import Template
city = "New York"
country = "USA"
template: Template = t"I live in {city}, {country}."
rendered = simple_render(template)
print(rendered)


This will output: I live in New York, USA. Furthermore, a single placeholder can be reused multiple times within the same template :
from string.templatelib import Template
item = "example"
template: Template = t"This is an {item}. Another {item}."
rendered = simple_render(template)
print(rendered)


The output will be: This is an example. Another example. Finally, as mentioned earlier, the static parts and interpolated values of a Template object can be accessed directly through its .strings and .values properties :
from string.templatelib import Template
name = "Beginner"
template: Template = t"Hello {name}!"
print(template.strings)
print(template.values)


This will output: ('Hello ', '!') and ('Beginner',), respectively, illustrating how the template is broken down into its constituent parts.
The initial syntax of t-strings, with its use of the t prefix and curly braces, will likely feel familiar to developers already acquainted with f-strings, which can facilitate a smoother learning process. However, the crucial concept of a separate rendering step and the introduction of the Template object represent a new way of working with strings for those whose primary experience is with f-strings. Understanding this distinction and how to interact with Template objects will be essential for effectively utilizing t-strings.
Real-World Applications: Unleashing the Power of t-strings
The unique characteristics of t-strings, particularly their deferred evaluation and the ability to process the Template object, open up several compelling real-world applications. In web development, t-strings can be employed to build safer HTML templates. By allowing for the automatic escaping of user-provided data during the rendering process, t-strings can help mitigate cross-site scripting (XSS) vulnerabilities. The hypothetical html() function, which takes a Template and sanitizes the input, exemplifies this use case. Furthermore, t-strings can facilitate the dynamic generation of HTML attributes, allowing for more flexible and programmatic construction of web elements. The pep750-examples repository provides more advanced illustrations of HTML templating with t-strings, including the creation of components and handling of nested elements.
In the realm of data handling, particularly with databases, t-strings offer a mechanism to prevent SQL injection vulnerabilities. By allowing database libraries to take a Template object and handle the secure binding of parameters, t-strings can encourage safer practices. Examples include using t-strings with libraries like sqlite3 or SQLAlchemy to construct parameterized queries. The Template object enables the database library to inspect the structure of the query and ensure that interpolated values are safely substituted, rather than directly embedded in a potentially unsafe manner.
Logging is another area where t-strings can provide significant benefits. They can be used for structured logging, allowing for a clear separation between the human-readable log message and structured data that can be easily parsed and analyzed. The pep750-examples repository showcases how a single log call utilizing a t-string can produce both a human-readable log message and a JSON-formatted output containing the structured data. This structured log data can be invaluable for monitoring application behavior and debugging issues.
Furthermore, there is a proposal (PEP 787) to introduce t-string support to the subprocess module. This would enable the safer and more readable construction of commands executed by subprocesses. T-strings could aid in correctly quoting and escaping arguments passed to these subprocesses, thereby reducing the risk of shell injection attacks. Beyond these core applications, t-strings hold potential for use in other areas such as internationalization (i18n), where the deferred evaluation might be advantageous , and in the creation of domain-specific languages (DSLs) where the ability to process the template structure can be particularly useful.
The potential of t-strings to enhance the security of Python applications interacting with databases or generating web content is substantial. By promoting safer practices for handling dynamic data, t-strings can contribute to more robust and secure software. Their flexibility also opens up new avenues for creating more sophisticated and maintainable code in areas like logging and templating, where custom handling of string content is often a necessity.
Navigating the Template Landscape: string.templatelib.Template vs. string.Template
It is important to note that Python's standard library already includes a Template class within the string module. This existing string.Template class, introduced by PEP 292, serves a different purpose compared to the new string.templatelib.Template introduced in Python 3.14. The primary goal of string.Template is to provide a simpler mechanism for string substitutions using $-based placeholders, making it particularly useful for tasks like internationalization (i18n) where a less complex syntax is often preferred. Basic syntax involves using $$ for a literal $, $identifier for substitution placeholders, and ${identifier} when identifier characters follow immediately. The class provides methods like substitute() and safe_substitute() to perform the replacements.
In contrast, PEP 750 introduces a new Template class located within the string.templatelib submodule. As previously discussed, t-strings, which use the t prefix and curly brace placeholders {}, evaluate to instances of this new string.templatelib.Template class. The key differences lie in the syntax used for placeholders ({} vs. $), the primary purpose (security and flexibility vs. simple substitution for i18n), and the requirement for separate processing of the string.templatelib.Template object.
The similarity in names between string.Template and string.templatelib.Template could potentially lead to confusion among developers. It is important to recognize that while both serve as template mechanisms, they operate with different syntax and are intended for distinct use cases. Typically, the context in which a Template object is being used – whether it arises from a t-string literal or from explicit instantiation of one of the Template classes – will indicate which class is being referred to. Clear documentation and examples will be crucial in differentiating their usage and helping developers choose the appropriate tool for their needs. The decision to place the new Template class within a submodule suggests a more structured approach to templating within the standard library, potentially paving the way for future enhancements and related functionalities within string.templatelib.
Conclusion: Embracing the Future of String Processing
Python 3.14's introduction of t-strings marks a significant step forward in th