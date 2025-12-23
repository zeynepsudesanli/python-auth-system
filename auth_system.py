


import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_connection():
    return sqlite3.connect("users.db")

def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

create_users_table()


def register():
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    hashed_password = hash_password(password)

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, hashed_password)
    )

    connection.commit()
    connection.close()

    print("Registration successful.")

    
    
# register()   
    
def login():
    email = input("Email: ")
    password = input("Password: ")
    hashed_password = hash_password(password)

    
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    "SELECT * FROM users WHERE email = ? AND password = ?",
    (email, hashed_password)
)


    user = cursor.fetchone()
    conn.close()
    
    if user:
        print("Login successful.")
    else:
        print("Invalid email or password.")
        
        
# login()

def menu():
    while True:
        print("\n--- AUTH SYSTEM ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Bye 👋")
            break
        else:
            print("Invalid choice")

menu()



    
    
    
    
    
    
    
    
    

    
