import os

course = "python"  
topic = "functions"
directory_path = os.path.join(os.getcwd(), course,"docs", topic,"practice-and-progress")
file_names = [
    f"fill-blank-python-{topic}.md",
    f"find-fix-mistakes-python-{topic}.md",
    f"mini-projects-python-{topic}.md",
    f"review-questions-python-{topic}.md",
    f"true-false-python-{topic}.md",
    f"mcqs-python-{topic}.md"
]

# Define the content for the markdown files
markdown_content = """---
layout: default
title: --.
description: --.
---
"""

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

# Create the markdown files with the specified content
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "w") as file:
        file.write(markdown_content)

print(f"Markdown files created successfully in {directory_path}")