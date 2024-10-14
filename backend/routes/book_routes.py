# routes/book_routes.py
from flask import Blueprint, request, jsonify
import sqlite3

book_bp = Blueprint('book', __name__)

@book_bp.route('/all_books', methods=['GET'])
def all_books():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        return jsonify([dict(zip([key[0] for key in cursor.description], row)) for row in books])

@book_bp.route('/borrow_book', methods=['POST'])
def borrow_book():
    data = request.json
    user_id = data['user_id']
    book_id = data['book_id']
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "User ID does not exist."}), 400

        # Check if the book exists and get its status
        cursor.execute('SELECT status FROM books WHERE id = ?', (book_id,))
        book = cursor.fetchone()
        if not book:
            return jsonify({"error": "Book ID does not exist."}), 400
        
        # Check if the book is available
        if book[0] != 'available':  # Assuming status is the first column
            return jsonify({"error": "Book is not available."}), 400
        
        # Proceed to borrow the book
        cursor.execute('INSERT INTO borrowed_books (user_id, book_id) VALUES (?, ?)', (user_id, book_id))
        cursor.execute('UPDATE books SET status = ? WHERE id = ?', ('borrowed', book_id))
        conn.commit()
        return jsonify({"message": f"Book {book_id} borrowed successfully!"}), 200

@book_bp.route('/return_book', methods=['POST'])
def return_book():
    data = request.json
    user_id = data['user_id']
    book_id = data['book_id']
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "User ID does not exist."}), 400

        # Check if the book exists
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        book = cursor.fetchone()
        if not book:
            return jsonify({"error": "Book ID does not exist."}), 400

        # Check if the book is currently borrowed by the user
        cursor.execute('SELECT * FROM borrowed_books WHERE user_id = ? AND book_id = ?', (user_id, book_id))
        borrowed_book = cursor.fetchone()
        
        if borrowed_book:
            # Remove the entry from borrowed_books
            cursor.execute('DELETE FROM borrowed_books WHERE user_id = ? AND book_id = ?', (user_id, book_id))
            # Update the book status to available
            cursor.execute('UPDATE books SET status = ? WHERE id = ?', ('available', book_id))
            conn.commit()
            return jsonify({"message": f"Book {book_id} returned successfully!"}), 200
        else:
            return jsonify({"error": "This book was not borrowed by the user."}), 400

@book_bp.route('/my_borrowed_books', methods=['GET'])
def my_borrowed_books():
    user_id = request.args.get('user_id')
    
    if not user_id:
        return jsonify({"error": "User ID is required."}), 400

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "User ID does not exist."}), 400

        # Fetch all borrowed books for the user with additional details
        cursor.execute('''
            SELECT 
                b.id, b.title, b.subtitle, b.authors, b.image, b.url 
            FROM 
                borrowed_books bb 
            JOIN 
                books b ON bb.book_id = b.id 
            WHERE 
                bb.user_id = ?
        ''', (user_id,))
        borrowed_books = cursor.fetchall()

        # Return the full list of borrowed books with detailed information
        return jsonify([
            {
                "id": row[0],
                "title": row[1],
                "subtitle": row[2],
                "authors": row[3],
                "image": row[4],
                "url": row[5]
            }
            for row in borrowed_books
        ])
