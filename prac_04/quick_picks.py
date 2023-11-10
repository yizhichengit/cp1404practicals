import random

NUM_QUICK_PICKS = 0
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_pick():
    # Generate a single quick pick without using random.sample()
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        # Use string formatting to align the numbers
        formatted_quick_pick = " ".join(["{:2}".format(number) for number in quick_pick])
        print(formatted_quick_pick)

if __name__ == "__main__":
    main()


