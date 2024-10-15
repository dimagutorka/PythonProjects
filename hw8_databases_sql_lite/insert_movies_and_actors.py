import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('movie_warehouse.db')
cursor = conn.cursor()

def add_movie(amounts_of_actors=0, is_there_actors=True):
	title = input("Enter movie title: ")
	release_year = input("Enter release year: ")
	genre = input("Enter genre: ")

	cursor.execute('''
	INSERT INTO Movies (title, release_year, genre) 
	VALUES (?, ?, ?)''', (title, release_year, genre))

	if is_there_actors and amounts_of_actors > 0:
		movie_id = cursor.lastrowid
		add_actor(movie_id, amounts_of_actors)


def add_actor(movie_id, amounts_of_actors):

	for i in range(amounts_of_actors):
		name = input("Enter actor's name: ")
		birth_year = input("Enter actor's birth year: ")
		cursor.execute('''
		INSERT INTO Actors (name, birth_year) 
		VALUES (?, ?)''', (name, birth_year))

		actor_id = cursor.lastrowid
		add_actors_to_movie(movie_id, actor_id)


def add_actors_to_movie(movie_id, actor_id):
		cursor.execute('''
		INSERT OR IGNORE INTO movie_cast (movie_id, actor_id) 
		VALUES (?, ?)''', (movie_id, actor_id))


def main():
	add_movie(5)

	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()




