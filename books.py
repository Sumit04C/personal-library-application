class Book:
    def __init__(self, title, author, year, genre, medium, book_type):
        #self.id = str(uuid.uuid4()) # Generate a unique ID for each book
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.medium = medium
        self.type = book_type 


import csv
import os 
#import uuid for generating unique IDs for each book entry
from fileinput import filename

def main():
    print(f"Welcome to your Personal Library Manager!")
    book_file_path = "books.csv"
    books = get_user_books() 

    save_to_csv(books, book_file_path) #defined line 71
    display_books(book_file_path, books)


def get_user_books():
#print(f"Getting User Books!\n")
#need to display the csv here so the user can see what they've inputted.

#all the attributes of the book that the user will input. The user will be prompted to enter the book name, 
# author, year, genre, medium, and type. 
# The user will also be able to select the genre from a list of options.
    title = input("Enter book name: ")
    author = input("Enter book author: ")
    year = input("Enter book year: ")
    genre = input("Enter book genre: ")
    medium = input("Enter book medium (book/manga/magazine/etc): ")
    type = input("Enter book type (physical/ebook/audiobook/pdf): ")

#shows the medium of the book, the type of book, and the genre of the book. The user can select from a list of options for each category, and the selected options are used to create a new Book object with the specified attributes.
    book_mediums = [
        "Book",
        "Manga",
        "Comic",
        "Graphic Novel",
        "Magazine", "literary magazine",
        "Other"
    ]

    book_types = [
        "Physical",
        "Ebook",
        "Audiobook",
        "PDF"
    ]

    book_genres = [
        "Fiction",
        "Fantasy",
        "Science Fiction",
        "Mystery",
        "Misc"

    ]


def save_to_csv(book, filename="books.csv"):
    # Check if file exists: if not, create headers
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='',) as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'author', 'year', 'genre', 'medium', 'type'])
        #what does DictWriter do? 
        # DictWriter is a class in the csv module that allows you to write dictionaries to a CSV file.

        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            #'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'genre': book.genre,
            'medium': book.medium,
            'type': book.type
        })

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    medium = input("Enter medium (book/manga/magazine/etc): ")
    book_type = input("Enter type (physical/ebook/audiobook/pdf): ")

    return Book(title, author, year, genre, medium, book_type)

    book_mediums = ["Book", "Manga","Comic","Graphic Novel","Magazine","Other"]
    book_types = ["Physical","Ebook","Audiobook","PDF"]
    book_genres = ["Fiction","Fantasy","Science Fiction","Mystery","Misc"]

    while True: 
        for i, book_id in enumerate(book_id, start=1):
            print(f"{i}. {id}. {book_id[i]}")
    #each book entry is assigned an integer value starting from 1. 
    #done automatically by the enumerate function, which takes care of the indexing for you.
    #once the core functionality is done, I want the user to be able to search for books by index/id number. 

        value_range = f"{len(book_genres)}]"     
        selected_index = int(input(f"Enter a genre {value_range}: ")) 
        print(f"\nYou selected: {book_genres[selected_index]}")

        if selected_index in range(len(book_genres)):
            selected_genre = book_genres[selected_index]
            new_book = book(title="Sample Book", author="Author Name", year=int["book_year"], genre=selected_genre)


if __name__ == "__main__":
    book = add_book()
    save_to_csv(book, filename="books.csv")
    #print(f"Book added successfully with ID: {book.id}")

def display_books(filename="books.csv"):
    if not os.path.isfile(filename):
        print("No books found. Please add some books first.")
        return
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Title: {row['title']}, Author: {row['author']}, Year: {row['year']}, Genre: {row['genre']}, Medium: {row['medium']}, Type: {row['type']}")


