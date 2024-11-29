from bs4 import BeautifulSoup  # For parsing HTML content
import requests  # For making HTTP requests
import csv  # For writing data to a CSV file

# Base URL for Al Jazeera website
url_website = 'https://www.aljazeera.com'


def get_page() -> BeautifulSoup:
    """
    Sends a GET request to the news page and returns a BeautifulSoup object of the page content.

    Returns:
    BeautifulSoup: Parsed HTML content of the news page.
    """
    try:
        # Fetch the content of the news page
        req = requests.get('https://www.aljazeera.com/news/').text
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(req, 'html.parser')
        return soup
    except requests.exceptions.HTTPError:
        print('Request failed')
    except requests.exceptions.ReadTimeout:
        print('Request timed out')
    except requests.exceptions.ConnectionError:
        print('Connection error')
    except Exception as e:
        print(e)


def parse_news() -> list:
    """
    Parses the news page to extract article details and stores them in a list of dictionaries.

    Returns:
    list: A list of dictionaries, each containing the link, title, summary, and date of an article.
    """
    list_news = []  # List to hold parsed news articles
    # Find all relevant article divs
    news_headers = get_page().find_all('div', class_='gc__content')

    # Iterate over the articles and extract relevant information
    for ind, art in enumerate(news_headers):
        if art.a.span is not None:
            list_news.append({
                f'Article_{ind}': {
                    'link': url_website + art.a.attrs['href'],  # Construct the full URL
                    'title': art.a.span.text,  # Extract the title
                    'summary': art.p.text,  # Extract the summary
                    'date': art.find('span', class_='screen-reader-text').text  # Extract the date
                }
            })
    return list_news


def format_data_for_csv() -> tuple:
    """
    Formats parsed news data for CSV writing.

    Returns:
    tuple: A tuple containing the CSV field names and data rows.
    """
    data_from_scrapper = parse_news()

    fields_for_csv = []  # List for field names
    data_for_csv = []  # List for data rows

    # Extract field names and data from the parsed news
    for row in data_from_scrapper:
        for val in row.values():
            data_for_csv.append(val)  # Append article details as rows

            if not fields_for_csv:  # Only set field names once
                fields_for_csv = [field for field in val.keys()]

    return fields_for_csv, data_for_csv


def save_to_csv() -> None:
    """
    Saves the parsed news data to a CSV file.
    """
    # Get field names and data rows
    fields = format_data_for_csv()[0]
    data = format_data_for_csv()[1]

    # Write data to a CSV file
    with open('news.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()  # Write the header row
        writer.writerows(data)  # Write the data rows


def main() -> None:
    """
    Main function to run all steps of the scraper.
    """
    get_page()  # Fetch and parse the page
    parse_news()  # Parse news articles
    format_data_for_csv()  # Format data for CSV writing
    save_to_csv()  # Save data to a CSV file


if __name__ == '__main__':
    main()  # Run the main function
