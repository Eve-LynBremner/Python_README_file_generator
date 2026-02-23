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
        "choices" : ["MIT License", "Apache License 2.0", "GNU General Public License (GPL v3)", "GNU Lesser General Public License (LGPL v3)", "Mozilla Public License 2.0 (MPL 2.0)", "Creative Commons Licenses (CC0, CC BY, etc.)", "Unlicense"]
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