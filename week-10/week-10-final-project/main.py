

import requests
import json



def fetch_books(title_query):

    url = "https://openlibrary.org/search.json"
    params = {"title": title_query}  # Example query; you can change this to any search term


    try:
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            return None

        result = response.json()

    # Extract the list of books from the response
        books = result.get("docs", [])

        cleaned_books = []

        for item in books:
            title = item.get("title", "N/A")
            #EXTRACT AUTHOR
            author_name = item.get("author_name", ["N/A"])[0]  # Get the first author if available
            first_publish_year = item.get("first_publish_year", "N/A")

            cleaned_books.append({
                "title": title,
                "author": author_name,
                "first_publish_year": first_publish_year
        })
        return cleaned_books

    except requests.exceptions.RequestException as e:
     print(f"Error: Could not reach the server ({e}). Check your connection and try again.")
     return None

def search_by_title():
    user_input = input("Enter a title to search for: ").strip().lower()
    if not user_input:
        print("Error: Title cannot be empty. Please enter a valid title.")
        return
    print(f"Searching for books with title: '{user_input}'...")
    books = fetch_books(user_input)

    if books is None:
        print("No books found or an error occurred during the search.")
        return

    print(f"Found {len(books)} books:")

    for book in books[:5]:  # Display only the first 5 results
        print(f"Title: {book['title']}, Author: {book['author']}, First Published: {book['first_publish_year']}")


if __name__ == "__main__":

    while True:
        print("\nBook Search Menu:")
        print("1. Search for books by title")
        print("2. Exit")    
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_by_title()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

