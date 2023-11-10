class ProgrammingLanguage:
    # Constructor
    def __init__(self, name, typing, reflection, year):
        self.name = name           # Name of the programming language, e.g., Python, Ruby, etc.
        self.typing = typing       # Typing: Static/Dynamic
        self.reflection = reflection # Reflection: True/False
        self.year = year           # Year: Year of first appearance

    # is_dynamic method, returns True if this programming language is dynamically typed, otherwise returns False
    def is_dynamic(self):
        return self.typing == "Dynamic"

    # __str__ method, returns a description of the programming language
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
