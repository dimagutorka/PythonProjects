import sqlite3


try:
	conn = sqlite3.connect('movie_warehouse.db')
	cursor = conn.cursor()

	# Create tables
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Movies (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    title TEXT NOT NULL,
	    release_year INTEGER,
	    genre TEXT
	)
	''')

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Actors (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name TEXT NOT NULL,
	    birth_year INTEGER
	)
	''')

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Movie_cast (
	    movie_id INTEGER,
	    actor_id INTEGER,
	    PRIMARY KEY (movie_id, actor_id),
	    FOREIGN KEY (movie_id) REFERENCES Movies(id),
	    FOREIGN KEY (actor_id) REFERENCES Actors(id)
	)
	''')

except sqlite3.Error as e:
	print('Error %d: %s' % (e.args[0], e.args[1]))

finally:
	if conn:
		conn.close()
		print('Connection closed.')

