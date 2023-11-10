data = []

def list_exercises():
    for i in range(5):
        number = int(input("Enter a number: "))  # Convert the input to an integer
        print(f"Number: {number}")
        data.append(number)  # Append the integer to the list

def check_access(username):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

list_exercises()

print(f"The first number is: {data[0]}")
print(f"The last number is: {data[-1]}")  # You can use negative indexing to get the last element
max_n = max(data)
min_n = min(data)
sum_n = sum(data)
average_n = sum_n / len(data)  # Use len(data) to get the number of elements in the list
print(f"The smallest number is: {min_n}")
print(f"The largest number is: {max_n}")
print(f"The average of the numbers is: {average_n}")

# Get the username from the user
username = input("Enter your username: ")
check_access(username)

