from flask import render_template, request, redirect

from app import app
from models.book import Book
from models.book_list import book_list, get_book_list, add_new_book, delete_book

@app.route('/')
def index():
    book_list = get_book_list()
    return render_template('index.html', title='Home', book_list = book_list)


@app.route('/books/<index>')
def single_book_index(index):
    singe_book = book_list[int(index)]
    print(singe_book)
    return render_template('book.html', title='Book', book= singe_book)

@app.route('/books', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return redirect('/')

@app.route('/books/<index>/delete', methods=['POST'])
def delete(index):
    delete_book(int(index))
    return redirect('/')