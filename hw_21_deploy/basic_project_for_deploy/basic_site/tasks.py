import time
from celery import shared_task
import csv
from basic_site.models import Movies, Genres
from celery_progress.backend import ProgressRecorder


@shared_task(bind=True)
def from_csvfile_to_bd(self, filename):
	progress_recorder = ProgressRecorder(self)

	file_path = f'../basic_project_for_deploy/media/{filename}'

	with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
		lines = len(csv_file.readlines())
		csv_file.seek(0)

		csv_reader = csv.DictReader(csv_file)

		for i, row in enumerate(csv_reader):
			time.sleep(1) #just to prolong progress bar "animations" on a web page
			genre = row['genres']

			try:
				get_genre = Genres.objects.get(name=genre)

				movie = Movies.objects.create(
					title=row['title'],
					country=row['country'],
				)
				movie.genres.set([get_genre])
				movie.save()

				progress_recorder.set_progress(i + 1, lines)
			except Genres.DoesNotExist:
				print(f'Genre {genre} does not exist')