from bs4 import BeautifulSoup
import requests
import csv


url_website = 'https://www.aljazeera.com'


def get_page():
	req = requests.get('https://www.aljazeera.com/news/').text
	soup = BeautifulSoup(req, 'html.parser')

	return soup


def parse_news():
	list_news = []
	news_headers = get_page().find_all('div', class_='gc__content')

	for ind, art in enumerate(news_headers):
		if art.a.span is not None:
			list_news.append({f'Article_{ind}':
				                  {'link': url_website + art.a.attrs['href'],
				                   'title': art.a.span.text,
				                   'summary': art.p.text,
				                   'date': art.find('span', class_='screen-reader-text').text}})
	return list_news


def save_to_csv():
	data_from_scrapper = parse_news()
	fields_for_csv = []
	data_for_csv = []

	for row in data_from_scrapper:

		for val in row.values():
			data_for_csv.append(val)

			if not fields_for_csv:
				fields_for_csv = [field for field in val.keys()]

	with open('news.csv', 'w', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fields_for_csv)
		writer.writeheader()
		writer.writerows(data_for_csv)


def main():
	get_page()
	parse_news()
	save_to_csv()


if __name__ == '__main__':
	main()
