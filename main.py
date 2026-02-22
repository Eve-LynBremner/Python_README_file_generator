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
    "To use this read me generator, please follow the prompts below. A readme.md file will then be created in your current folder."
)

# Get input by asking questions
user_data = prompt(questions)

# generate markdown content for readme file using the input from the questions
content = Content(user_data)
markdown_content = content.generate_content()

# Generate readme file using the formatted markdown content
readme_file = Generator('test.md', markdown_content)
readme_file.generate_readme()

# Confirmation that readme.md has been created
test = open("test.md").read()
if test:
    console.print("[bold green]readme.md has been generated[/bold green] ✅")    
else:
    console.print("[bold red]readme.md failed to generate[/bold red] ❌")
