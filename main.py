from InquirerPy import prompt
from rich.console import Console

# input required to create content for readme
from readme_questions import questions

# class to format input from questions into content for the readme file
from readme_content import Content

# class to create readme and populate with formatted content
from readme_generator import Generator

console = Console()

# Instructions for user
console.print(
    "Hi. To use this read me generator, please answer the questions below. A readme markdown file will then be created in your current folder. Thank you."
)

# Get input by asking questions
user_data = prompt(questions)

# generate markdown content for readme file using the input from the questions
content = Content(user_data)
markdown_content = content.generate_content()

# Generate readme file using the formatted markdown content
readme_file = Generator('test.md', markdown_content)
readme_file.generate_readme()
