import sqlite3

conn = sqlite3.connect('movie_warehouse.db')
cursor = conn.cursor()


def all_data_from_movies_actors_tables():
	cursor.execute(""" 
	SELECT m.title, m.release_year, m.genre, a.name, a.birth_year FROM Movies m 
	JOIN Movie_cast ms on m.id = ms.movie_id
	JOIN Actors a on a.id = ms.actor_id """, )

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


def need_rename():
	cursor.execute("""SELECT DISTINCT genre FROM movies""")

	for i in cursor.fetchall():
		cursor.execute("""
		SELECT count(title) 
		FROM movies 
		WHERE genre = ? """, (i[0],))

		print(f'{i[0]} {cursor.fetchone()[0]}')


def limited_amount_of_movies(limit=0, offset=0):
	cursor.execute(""" 
	SELECT m.title, m.release_year, m.genre, a.name, a.birth_year 
	FROM Movies m 
	JOIN Movie_cast ms on m.id = ms.movie_id
	JOIN Actors a on a.id = ms.actor_id  LIMIT ? OFFSET ?""", (limit, offset))

	[print(i) for i in cursor.fetchall()]


def main():
	all_data_from_movies_actors_tables()
	conn.commit()
	conn.close()


if __name__ == '__main__':
	main()