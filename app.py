from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 데이터를 저장할 딕셔너리 초기화
members = {}
books = {}

@app.route('/')
def home():
    return render_template('index.html', members=members, books=books)

@app.route('/add_member', methods=['POST'])
def add_member():
    member_id = request.form['member_id']
    member_name = request.form['member_name']
    members[member_id] = member_name
    return redirect(url_for('home'))

@app.route('/remove_member', methods=['POST'])
def remove_member():
    member_id = request.form['member_id']
    if member_id in members:
        del members[member_id]
    return redirect(url_for('home'))

@app.route('/add_book', methods=['POST'])
def add_book():
    book_id = request.form['book_id']
    book_title = request.form['book_title']
    books[book_id] = {'title': book_title, 'status': 'Available'}
    return redirect(url_for('home'))

@app.route('/remove_book', methods=['POST'])
def remove_book():
    book_id = request.form['book_id']
    if book_id in books:
        del books[book_id]
    return redirect(url_for('home'))

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    book_id = request.form['book_id']
    if book_id in books and books[book_id]['status'] == 'Available':
        books[book_id]['status'] = 'Borrowed'
    return redirect(url_for('home'))

@app.route('/return_book', methods=['POST'])
def return_book():
    book_id = request.form['book_id']
    if book_id in books and books[book_id]['status'] == 'Borrowed':
        books[book_id]['status'] = 'Available'
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


