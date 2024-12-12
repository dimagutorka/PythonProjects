from celery import shared_task
import csv
from basic_site.models import Movies, Genres


@shared_task(bind=True)
def test_func(self):
	for i in range(20):
		print(i)
	return 'DONE'


@shared_task(bind=True)
def from_csvfile_to_bd(self, filename):
	file_path = f'../basic_project_for_deploy/media/{filename}'

	with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
		csv_reader = csv.DictReader(csv_file)

		for row in csv_reader:
			genre = row['genres']

			try:
				get_genre = Genres.objects.get(name=genre)

				movie = Movies.objects.create(
					title=row['title'],
					country=row['country'],
				)
				movie.genres.set([get_genre])
				movie.save()
			except Genres.DoesNotExist:
				print(f'Genre {genre} does not exist')