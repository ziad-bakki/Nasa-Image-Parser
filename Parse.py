import requests
from bs4 import BeautifulSoup

URL = 'https://www.nasa.gov/image-of-the-day/page/'

first_page = 1
last_page = 100


image_urls = []
for page_number in range(first_page, last_page + 1):
    new_url = URL + str(page_number) + '/'
    request = requests.get(new_url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html5lib')
        images = soup.find_all("div", class_="hds-gallery-item-single hds-gallery-image")
        image_urls = [img.find('img')['src'] for img in images if img.find('img')]
        print(image_urls)
            