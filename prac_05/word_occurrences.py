def word_count(text):
    # Split the input text into words
    words = text.split()

    # Create a dictionary to store word counts
    word_counts = {}

    # Initialize the maximum word length for formatting
    max_word_length = 0

    # Count the occurrences of each word
    for word in words:
        # Remove punctuation and convert to lowercase
        cleaned_word = word.strip('.,!?').lower()

        # Update the maximum word length if needed
        max_word_length = max(max_word_length, len(cleaned_word))

        # Count the word
        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

    # Sort the word counts by word
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

    # Print the formatted word counts
    for word, count in sorted_word_counts:
        print(f"{word:{max_word_length}} : {count}")


# Get input text from the user
user_input = input("Enter a string: ")

# Call the word_count function with the input text
word_count(user_input)
