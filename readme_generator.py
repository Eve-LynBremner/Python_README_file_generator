class Generator:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def generate_readme(self):
        with open(self.filename, "w") as file:
            file.write(self.content)