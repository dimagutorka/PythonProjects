import sqlite3

try:
    # Establish a connection to the SQLite database
    with sqlite3.connect('movie_warehouse.db') as conn:
        cursor = conn.cursor()

        # Create Movies table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_year INTEGER,
            genre TEXT
        )
        ''')

        # Create Actors table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_year INTEGER
        )
        ''')

        # Create Movie_cast table with foreign key constraints
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movie_cast (
            movie_id INTEGER,
            actor_id INTEGER,
            PRIMARY KEY (movie_id, actor_id),
            FOREIGN KEY (movie_id) REFERENCES Movies(id) ON DELETE CASCADE,
            FOREIGN KEY (actor_id) REFERENCES Actors(id) ON DELETE CASCADE
        )
        ''')

        print("Tables created successfully.")

except sqlite3.Error as e:
    # Handle database errors with more robust exception handling
    print(f"SQLite error: {e}")

# Connection automatically closes here due to the context manager
