import sqlite3


def add_movie(cursor, conn, amounts_of_actors=0, is_there_actors=True):
	"""
	Adds a new movie to the Movies table and optionally adds associated actors.

	Args:
		cursor (sqlite3.Cursor): The cursor object for executing SQL commands.
		conn (sqlite3.Connection): The connection to the SQLite database.
		amounts_of_actors (int): Number of actors to associate with the movie.
		is_there_actors (bool): Whether to add actors for the movie.
	"""
	title = input("Enter movie title: ")
	release_year = input("Enter release year: ")
	genre = input("Enter genre: ")

	cursor.execute('''
    INSERT INTO Movies (title, release_year, genre) 
    VALUES (?, ?, ?)
    ''', (title, release_year, genre))

	# Commit after adding movie to save to database
	conn.commit()

	if is_there_actors and amounts_of_actors > 0:
		movie_id = cursor.lastrowid
		add_actor(cursor, conn, movie_id, amounts_of_actors)


def add_actor(cursor, conn, movie_id, amounts_of_actors):
	"""
	Adds actors to the Actors table and associates them with a given movie.

	Args:
		cursor (sqlite3.Cursor): The cursor object for executing SQL commands.
		conn (sqlite3.Connection): The connection to the SQLite database.
		movie_id (int): The ID of the movie to associate the actors with.
		amounts_of_actors (int): Number of actors to add.
	"""
	for _ in range(amounts_of_actors):
		name = input("Enter actor's name: ")
		birth_year = input("Enter actor's birth year: ")

		cursor.execute('''
        INSERT INTO Actors (name, birth_year) 
        VALUES (?, ?)
        ''', (name, birth_year))

		actor_id = cursor.lastrowid
		add_actors_to_movie(cursor, movie_id, actor_id)

	# Commit after adding actors to save to database
	conn.commit()


def add_actors_to_movie(cursor, movie_id, actor_id):
	"""
	Associates an actor with a movie in the Movie_cast table.

	Args:
		cursor (sqlite3.Cursor): The cursor object for executing SQL commands.
		movie_id (int): The ID of the movie.
		actor_id (int): The ID of the actor.
	"""
	cursor.execute('''
    INSERT OR IGNORE INTO Movie_cast (movie_id, actor_id) 
    VALUES (?, ?)
    ''', (movie_id, actor_id))


def main():
	try:
		# Establish a connection to the SQLite database
		with sqlite3.connect('movie_warehouse.db') as conn:
			cursor = conn.cursor()
			add_movie(cursor, conn, 2)
			print("Movie and actors added successfully.")

	except sqlite3.Error as e:
		print(f"SQLite error: {e}")

	finally:
		print("Connection closed.")


if __name__ == '__main__':
	main()
