import sqlite3 as sl

DB_NAME = 'users.db'

def create_db():
    conn = sl.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE,
            username_hash TEXT UNIQUE,
            password_hash TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(username, username_hash, password_hash):
    conn = sl.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO users (username, username_hash, password_hash) VALUES (?, ?, ?)',
              (username, username_hash, password_hash))
    conn.commit()
    conn.close()

def get_user_by_hash(username_hash):
    conn = sl.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT username, password_hash FROM users WHERE username_hash = ?', (username_hash,))
    result = c.fetchone()
    conn.close()
    return result
