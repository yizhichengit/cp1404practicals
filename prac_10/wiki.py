
import wikipedia
def main():
    # Start an infinite loop until the user chooses to exit
    while True:
        # Prompt the user to enter a page title or search phrase
        title = input("Enter a page title or search phrase: ")
        # If the input is empty, it means the user wants to exit the program
        if not title:
            break
        try:
            # Attempt to get the Wikipedia page for the specified title
            # auto_suggest is set to False, which means no automatic redirection suggestions
            page = wikipedia.page(title, auto_suggest=False)
            # Print the title of the page
            print("Title:", page.title)
            # Print the summary of the page
            print("Summary:", wikipedia.summary(title))
            # Print the URL of the page
            print("URL:", page.url)
        # Catch disambiguation errors, prompting the user for a more specific query
        except wikipedia.DisambiguationError as e:
            print("Disambiguation error:", e.options)
        # If the page is not found, inform the user that the page doesn't exist
        except wikipedia.PageError:
            print("Page not found.")
        # Catch any other exceptions and print the error message
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()

