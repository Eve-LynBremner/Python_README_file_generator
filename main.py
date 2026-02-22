from InquirerPy import prompt
from rich.console import Console

# input required to populate readme
from questions import questions

# class to create readme
# from generate_readme import generate_readme

console = Console()

# Instructions for user
console.print(
    "Hi. To use this read me generator, please answer the questions below. A readme markdown file will then be created in your current folder. Thank you."
)

user_data = prompt(questions)

# def read_file(filename):
#     with open(filename, "r") as file:
#         return file.read()

# def write_file(filename, content):
#     with open(filename, "w") as file:
#         file.write(content)


# if __name__ == "__main__":
#     write_file("sample.txt", "Hello, world!")
#     print("File content:", read_file("sample.txt"))

