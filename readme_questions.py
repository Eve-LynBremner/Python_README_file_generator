questions = [
    {
        "type": "input", 
        "name": "title", 
        "message": "What is your project title?",
        "validate": lambda result: len(result.strip()) > 0,
        "invalid_message": "This cannot be left empty."
     },
    {
        "type": "input", 
        "name": "description", 
        "message": "Describe your project.",
        "validate": lambda result: len(result.strip()) > 0,
        "invalid_message": "This cannot be left empty."
     },
    {
        "type": "input", 
        "name": "installation", 
        "message": "Provide installation instructions.",
        "validate": lambda result: len(result.strip()) > 0,
        "invalid_message": "This cannot be left empty."
     },
    {
        "type": "input", 
        "name": "usage", 
        "message": "Provide usage information.",
        "validate": lambda result: len(result.strip()) > 0,
        "invalid_message": "This cannot be left empty."
     },
    {
        "type": "list", 
        "name": "license", 
        "message": "Select a license from the list:", 
        "choices" : ["MIT License", "Apache License 2.0", "GPLv3", "BSD 3-Clause", "No License"]
        },
    {
        "type": "input", 
        "name": "author", 
        "message": "What is the author's name?",
        "validate": lambda result: len(result.strip()) > 0,
        "invalid_message": "This cannot be left empty."
        },
    {
        "type": "input", 
        "name": "contact", 
        "message": "Provide contact information",
        "validate": lambda result: len(result.strip()) > 0,
        "invalid_message": "This cannot be left empty."
        },
]