import requests
import csv
from typing import List, Dict, Any

BASE_URL: str = "https://openlibrary.org/search.json"
OUTPUT_FILE: str = "books_after_2000.csv"


def fetch_books(query: str = "the", limit: int = 200) -> List[Dict[str, Any]]:
    params: Dict[str, str | int] = {
        "q": query,
        "limit": limit,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
        return data.get("docs", [])
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []


def extract_and_filter_books(
    raw_books: List[Dict[str, Any]]
) -> List[Dict[str, str | int]]:
    filtered_books: List[Dict[str, str | int]] = []

    for book in raw_books:
        title: str = book.get("title", "N/A")

        author_list: List[str] = book.get("author_name", [])
        author: str = author_list[0] if author_list else "N/A"

        publish_year = book.get("first_publish_year")

        publisher_list: List[str] = book.get("publisher", [])
        publisher: str = publisher_list[0] if publisher_list else "N/A"

        if isinstance(publish_year, int) and publish_year > 2000:
            filtered_books.append(
                {
                    "Title": title,
                    "Author": author,
                    "First Publish Year": publish_year,
                    "Publisher": publisher,
                }
            )

    return filtered_books


def save_to_csv(
    books: List[Dict[str, str | int]], filename: str
) -> None:
    if not books:
        print("No books to save.")
        return

    books_sorted: List[Dict[str, str | int]] = sorted(
        books, key=lambda x: x["First Publish Year"]  # type: ignore
    )

    fieldnames: List[str] = [
        "Title",
        "Author",
        "First Publish Year",
        "Publisher",
    ]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books_sorted)

        print(
            f"Data successfully saved to {filename}, total {len(books_sorted)} books."
        )

    except Exception as e:
        print("Error saving CSV:", e)


def main() -> None:
    print("Fetching books from Open Library...")
    raw_books = fetch_books(query="the", limit=200)
    print(f"Total books fetched: {len(raw_books)}")

    filtered_books = extract_and_filter_books(raw_books)
    print(
        f"Number of books after filtering (after 2000): {len(filtered_books)}"
    )

    save_to_csv(filtered_books, OUTPUT_FILE)


if __name__ == "__main__":
    main()
