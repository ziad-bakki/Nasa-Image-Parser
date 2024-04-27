from flask import Flask, jsonify, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_images/')
def get_images():
    keyword = request.args.get('keyword', '')  # Use Flask's request to get query parameters
    URL = 'https://www.nasa.gov/image-of-the-day/page/'
    first_page = 1
    last_page = 10
    image_data = {}
    count = 0
    for page_number in range(first_page, last_page + 1):
        new_url = URL + str(page_number) + '/'
        response = requests.get(new_url)  # Rename variable to avoid confusion with Flask's request
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html5lib')
            images = soup.find_all("div", class_="hds-gallery-item-single hds-gallery-image")
            image_urls = {index: img.find('img')['src'] for index, img in enumerate(images, start=1) if img.find('img')}
            for src in image_urls.values():
                
                if keyword.lower() in src.lower():  # Ensure case insensitive comparison
                    image_data[count] = src
                    count += 1
            
    return jsonify(image_data)

if __name__ == '__main__':
    app.run(debug=True)
