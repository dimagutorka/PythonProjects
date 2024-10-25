import sqlite3
import datetime


def all_data_from_movies_actors_tables(cursor):
	"""
	Prints all data from Movies and Actors tables, showing title, release year, genre, actor name, and birth year.
	"""
	cursor.execute(""" 
    SELECT m.title, m.release_year, m.genre, a.name, a.birth_year 
    FROM Movies m 
    LEFT JOIN Movie_cast ms ON m.id = ms.movie_id
    LEFT JOIN Actors a ON a.id = ms.actor_id 
    """)
	[print(row) for row in cursor.fetchall()]


def distinct_movies(cursor):
	"""
	Prints all distinct genres from the Movies table.
	"""
	cursor.execute("SELECT DISTINCT genre FROM Movies")
	print("All distinct genres:")
	[print(row[0]) for row in cursor.fetchall()]


def movie_by_key_word(cursor, keyword):
	"""
	Prints movies whose titles match the provided keyword.

	Args:
		keyword (str): The keyword to search for in movie titles.
	"""
	cursor.execute("SELECT title FROM Movies WHERE title LIKE ?", (f"%{keyword}%",))
	print("Movies containing the keyword:", keyword)
	print(*[row[0] for row in cursor.fetchall()])


def movies_per_genre(cursor):
	"""
	Prints the count of movies per genre.
	"""
	cursor.execute("SELECT genre, COUNT(title) FROM Movies GROUP BY genre")
	for row in cursor.fetchall():
		print(f"{row[0]}: {row[1]}")


def average_age_actor_per_genre(cursor, genre):
	"""
	Prints the average age of actors in a given genre.

	Args:
		genre (str): The genre to calculate the average actor age.
	"""
	current_year = datetime.date.today().year
	cursor.execute("""
    SELECT AVG(?) - (a.birth_year) AS average_age 
    FROM Movies m
    LEFT JOIN Movie_cast ms ON m.id = ms.movie_id
    LEFT JOIN Actors a ON a.id = ms.actor_id
    WHERE m.genre = ?
    """, (current_year, genre))
	avg_birth_year = cursor.fetchone()
	if avg_birth_year:
		print(f'Average age of actors in genre "{genre}" is {int(avg_birth_year[0])}')
	else:
		print(f'No actors found in genre "{genre}"')


def limited_amount_of_movies(cursor, limit, offset=0):
	"""
	Prints a limited number of movies with optional offset.

	Args:
		limit (int): The maximum number of movies to display.
		offset (int, optional): The number of records to skip. Defaults to 0.
	"""
	cursor.execute("""
    SELECT m.title, m.release_year, m.genre, a.name, a.birth_year 
    FROM Movies m 
    JOIN Movie_cast ms ON m.id = ms.movie_id
    JOIN Actors a ON a.id = ms.actor_id  
    LIMIT ? OFFSET ?
    """, (limit, offset))
	[print(row) for row in cursor.fetchall()]


def unite_movies_and_actors(cursor):
	"""
	Prints a unified list of movies and actors' names.
	"""
	cursor.execute("""
    SELECT title AS item FROM Movies
    UNION
    SELECT name AS item FROM Actors
    """)
	[print(row[0]) for row in cursor.fetchall()]


def movie_age(cursor):
	"""
	Prints the age of each movie based on its release year.
	"""
	current_year = datetime.date.today().year
	cursor.execute("SELECT title, release_year FROM Movies")
	for title, release_year in cursor.fetchall():
		age_of_movie = current_year - release_year
		print(f"The movie {title} is {age_of_movie} years old")


def main():
	try:
		with sqlite3.connect('movie_warehouse.db') as conn:
			cursor = conn.cursor()
			all_data_from_movies_actors_tables(cursor)
			distinct_movies(cursor)
			movie_by_key_word(cursor, "keyword")  # Replace "keyword" with the actual keyword
			movies_per_genre(cursor)
			average_age_actor_per_genre(cursor, 'Horror')
			limited_amount_of_movies(cursor, limit=10)
			unite_movies_and_actors(cursor)
			movie_age(cursor)
	except sqlite3.Error as e:
		print(f"SQLite error: {e}")
	finally:
		print("Connection closed.")


if __name__ == '__main__':
	main()
