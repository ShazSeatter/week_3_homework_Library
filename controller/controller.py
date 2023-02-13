from flask import render_template, request, redirect

from app import app
from models.book import Book
from models.book_list import book_list, get_book_list, add_new_book, delete_book, update_book_status

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
    checked_out = True if 'check_out' in request.form else False
    new_book = Book(book_title, book_author, book_genre, checked_out)
    add_new_book(new_book)
    return redirect('/')

@app.route('/books/<index>/update', methods=['POST'])
def update(index):
    chosen_book = update_book_status(int(index))
    print(chosen_book)
    checked_out_book = True if 'check_out' in request.form else False
    chosen_book.update({'checked_out' : checked_out_book})
    print(checked_out_book)
    print(chosen_book)
    return redirect('/')

# basically sending back the information but the only thing updated is the boolena proepty
# You want to update the main page (/) to display checked out if person clicks the checkout to check the book out
# maybe need to update at specific index position

# currently the checked box when submitted is not returning true 
# current dictionary being displayed {'title': 'A Court of Torns of Roses', 'author': 'Sarah J Maas', 'genre': 'Fantasy', 'checked_out': False}
# need to updated checked-in key to True

# it returns true in the add new book form, so this means the checkbox is not working 

@app.route('/books/<index>/delete', methods=['POST'])
def delete(index):
    delete_book(int(index))
    return redirect('/')