from models.book import *


book_1 = Book("The Lord of the Rings", "T R R Tolkien", "Fantasy")
book_2 = Book("A Court of Torns of Roses", "Sarah J Maas", "Fantasy")
book_3 = Book("Pen Pal", "J.T Geissinger", "Thriller")

book_list = [book_1, book_2, book_3]

def get_book_list():
    return book_list