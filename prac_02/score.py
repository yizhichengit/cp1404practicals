def main():
    score = float(input("your score: "))
    result = ask_score(score)
    print(f"your score is {result}")


def ask_score(score):
    if score < 0 or score > 100:
       return "Invalid score"
    elif score <= 50:
        return "Bad"
    elif score <= 90:
        return "passable"
    else:
        return "Excellent"


if __name__ == "__main__":
    main()