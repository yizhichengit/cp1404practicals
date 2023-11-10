score = float(input("Enter score: "))

if score < 0 or score > 100:
    print(f"Invalid score")
elif score <= 50:
    print(f"Bad")
elif score <= 90:
    print(f"Passable")
else:
    print(f"Excellent")
print("hello")