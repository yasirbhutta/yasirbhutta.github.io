import os

course = "python"  # Replace with the desired course name
topic = "lists"  # Replace with the desired topic
# Define the directory path where the markdown files will be created
directory_path = os.path.join(os.getcwd(), course,"docs", topic,"practice-and-progress")
print(directory_path)
file_names = [
    f"fill-blanks-{topic}.md",
    f"find-fix-mistakes-{topic}.md",
    f"mini-projects-{topic}.md",
    f"review-questions-{topic}.md",
    f"true-false-{topic}.md",
    f"mcqs-{topic}.md",
    f"exercises-{topic}.md",
    f"quiz-{topic}.md"
]

# Define the content for the markdown files
markdown_content = """---
layout: page
title: "How to Use the SUM Function and AutoSum in Excel  Complete Guide"
description: Learn how to use the SUM function and AutoSum in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
show_toc: false
toc: toc/ms-excel-toc.html
show_practice_progress: false
show_mini_project: false
prev: /ms-excel/docs/functions/what-is-functions.html
next: /ms-excel/docs/functions/sumif.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---"""

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

# Create the markdown files with the specified content
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "w") as file:
        file.write(markdown_content)

print(f"Markdown files created successfully in {directory_path}")