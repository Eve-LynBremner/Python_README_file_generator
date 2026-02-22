class Content:
    def __init__(self, inputs):
        self.title = inputs['title']
        self.description = inputs['description']
        self.installation = inputs['installation']
        self.usage = inputs['usage']
        self.license = inputs['license']
        self.author = inputs['author']
        self.contact = inputs['contact']


    def generate_content(self):
        return f"""# {self.title}
        
## Description
{self.description}

## Installation
{self.installation}

## Usage
{self.usage}

## License
{self.license}

## Author
{self.author}

## Contact
{self.contact}
"""
