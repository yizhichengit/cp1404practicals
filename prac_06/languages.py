from programming_language import ProgrammingLanguage

# Create three ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the Python object
print(python)

# Create a list containing these three objects
languages = [python, ruby, visual_basic]

# Print descriptions of all programming languages
for language in languages:
    print(language)
