# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # For a new line

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # For a new line

# c. Print n stars
n = int(input("Number of stars: "))
for _ in range(n):
    print('*', end='')
print()  # For a new line

# d. Print n lines of increasing stars
for i in range(1, n + 1):
    print('*' * i)
print()  # For a new line

# End of loops.py content
