from flask import render_template

from app import app
from models.book import Book
from models.book_list import book_list, get_book_list

@app.route("/")
def index():
    book_list = get_book_list()
    return render_template("index.html", title="Home", book_list = book_list)


@app.route("/books/<index>")
def single_book_index(index):
    singe_book = book_list[int(index)]
    print(singe_book)
    return render_template('book.html', title="Book", book= singe_book)
