from models.book import *


book_1 = Book("The Lord of the Rings", "T R R Tolkien", "Fantasy", True)
book_2 = Book("A Court of Torns of Roses", "Sarah J Maas", "Fantasy", False)
book_3 = Book("Pen Pal", "J.T Geissinger", "Thriller", True)

book_list = [book_1, book_2, book_3]

def get_book_list():
    return book_list

def add_new_book(book):
    book_list.append(book)


def delete_book(index):
    book_list.pop(index)

def update_book_status(index):
    book = book_list[index].__dict__
    return book
