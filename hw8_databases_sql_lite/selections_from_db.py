import sqlite3
import datetime


try:
	conn = sqlite3.connect('movie_warehouse.db')
	cursor = conn.cursor()


	def all_data_from_movies_actors_tables():
		cursor.execute(""" 
		SELECT m.title, m.release_year, m.genre, a.name, a.birth_year FROM Movies m 
		LEFT JOIN Movie_cast ms on m.id = ms.movie_id
		LEFT JOIN Actors a on a.id = ms.actor_id """, )

		[print(i) for i in cursor.fetchall()]

	def distinct_movies():
		cursor.execute("""SELECT DISTINCT genre FROM movies""")
		print('All distinct genres:', )
		[print(i[0]) for i in cursor.fetchall()]


	def movie_by_key_word(key_words):
		cursor.execute("""
		SELECT title FROM movies 
		WHERE title LIKE ? """, (key_words,))
		print(*cursor.fetchall())


	def movies_per_genre():
		cursor.execute("""SELECT DISTINCT genre FROM movies""")

		for i in cursor.fetchall():
			cursor.execute("""
			SELECT count(title) 
			FROM movies 
			WHERE genre = ? """, (i[0],))

			print(f'{i[0]} {cursor.fetchone()[0]}')


	def average_age_actor_per_genre():
		cursor.execute("""
		SELECT m.genre, avg(a.birth_year) FROM Movies m
		LEFT JOIN Movie_cast ms on m.id = ms.movie_id
		LEFT JOIN Actors a on a.id = ms.actor_id
		WHERE m.genre = 'Horror' GROUP BY m.genre""")
		avg_br_of_actors = cursor.fetchall()

		print(f'Average age of actors per genre "{avg_br_of_actors[0][0]}" is {2024 - avg_br_of_actors[0][1]}')


	def limited_amount_of_movies(limit, offset=0):
		cursor.execute(""" 
		SELECT m.title, m.release_year, m.genre, a.name, a.birth_year 
		FROM Movies m 
		JOIN Movie_cast ms on m.id = ms.movie_id
		JOIN Actors a on a.id = ms.actor_id  LIMIT ? OFFSET ?""", (limit, offset))

		[print(i) for i in cursor.fetchall()]


	def unite_movies_and_actors():
		cursor.execute("""
		SELECT title AS item FROM Movies
		UNION
		SELECT name AS item FROM Actors;""")

		[print(i[0]) for i in cursor.fetchall()]


	def movie_age():
		cursor.execute("""SELECT title, release_year FROM Movies""")
		for i in cursor.fetchall():
			age_of_movie = datetime.date.today().year - int(i[1])
			print(f"The movie {i[0]} is {age_of_movie} old")

	def main():
		all_data_from_movies_actors_tables()
		average_age_actor_per_genre()
		limited_amount_of_movies(10)
		distinct_movies()
		# movie_by_key_word()
		unite_movies_and_actors()
		movie_age()
		movies_per_genre()


	if __name__ == '__main__':
		main()


except sqlite3.Error as e:
	print('Error %d: %s' % (e.args[0], e.args[1]))

finally:
	if conn:
		conn.close()
		print('Connection closed.')



