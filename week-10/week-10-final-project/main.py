import json
import matplotlib.pyplot as plt
import requests


def publish_year_distribution(books, query):
  # Extract first publish years
  years = []
  for book in books:
    year_value = book.get("first_publish_year")
    if year_value and year_value != "N/A":
      try:
        years.append(int(year_value))
      except ValueError:
        continue

  if not years:
    print("No valid first publish years found in the data.")
    return

  # Create a simple bar chart
  plt.figure(figsize=(10, 6))
  plt.hist(years, bins=20, edgecolor="black")
  plt.xlabel("First Publish Year")
  plt.ylabel("Number of Books")
  plt.title(f"Distribution of Books by First Publish Year ({query})")

  # Save chart as PNG file
  safe_query = query.replace(" ", "_").lower()
  filename = f"publish_year_distribution_{safe_query}.png"
  plt.savefig(filename)
  print(f"Chart saved as {filename}")
  plt.show()


def fetch_books(title_query):
  url = "https://openlibrary.org/search.json"
  params = {"title": title_query}

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
      # EXTRACT AUTHOR
      author_name = item.get("author_name", ["N/A"])[
          0
      ]  # Get the first author if available
      first_publish_year = item.get("first_publish_year", "N/A")

      cleaned_books.append({
          "title": title,
          "author": author_name,
          "first_publish_year": first_publish_year,
      })
    return cleaned_books

  except requests.exceptions.RequestException as e:
    print(
        f"Error: Could not reach the server ({e}). Check your connection and"
        " try again."
    )
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
    print(
        f"Title: {book['title']}, Author: {book['author']}, First Published:"
        f" {book['first_publish_year']}"
    )

  # This correctly calls the chart function using the fetched books and user input
  publish_year_distribution(books, user_input)


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