# Task 1: Write the user's name to "name.txt"
user_name = input("Enter your name: ")

# Open "name.txt" in write mode and write the user's name to it
with open("name.txt", "w") as file:
    file.write(user_name)

# The file will be automatically closed when the "with" block exits
# Task 2: Read and print the name from "name.txt"
with open("name.txt", "r") as file:
    stored_name = file.read()
    print(f"Your name is {stored_name}")
# Task 4: Read the first two numbers from "numbers.txt" and add them
with open("numbers.txt", "r") as file:
    lines = file.readlines()

# Check if there are at least two lines
if len(lines) >= 2:
    num1 = int(lines[0].strip())  # Convert the first line to an integer
    num2 = int(lines[1].strip())  # Convert the second line to an integer

    result = num1 + num2
    print(f"The result of adding the first two numbers is: {result}")
else:
    print("There are not enough numbers in the file.")
# Task 5: Calculate the total of all numbers in "numbers.txt"
with open("numbers.txt", "r") as file:
    lines = file.readlines()

total = 0

for line in lines:
    try:
        number = int(line.strip())
        total += number
    except ValueError:
        print(f"Skipping non-integer value: {line.strip()}")

print(f"The total of all numbers in the file is: {total}")
