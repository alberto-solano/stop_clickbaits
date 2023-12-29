import requests
from bs4 import BeautifulSoup


def web_page_extractor(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    cleaned_text = soup.get_text()

    return cleaned_text
