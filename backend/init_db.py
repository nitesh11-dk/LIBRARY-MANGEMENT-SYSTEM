import sqlite3

def init_db():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        
        # Create books table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id TEXT PRIMARY KEY,
                title TEXT,
                subtitle TEXT,
                authors TEXT,
                image TEXT,
                url TEXT,
                status TEXT DEFAULT 'available'
            )
        ''')
        
        # Create users table with a primary key
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,  -- Add an ID column as primary key
                username TEXT UNIQUE NOT NULL, 
                password BLOB NOT NULL          
            )
        ''')
        
        # Create borrowed_books table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                user_id TEXT,
                book_id TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id),  -- Reference users table
                FOREIGN KEY(book_id) REFERENCES books(id)    -- Reference books table
            )
        ''')
        
        conn.commit()

if __name__ == "__main__":
    init_db()
