Sense Home Energy Monitor Scraper

This script scrapes L1 and L2 voltages from the Sense Home Energy Monitor in real-time and logs them to a CSV file. It uses Selenium for web scraping.

Requirements

Python 3.9
Docker
ChromeDriver

Usage

Local Installation

Clone this repository:

git clone https://github.com/yourusername/sense-scraper.git
cd sense-scraper

Install the dependencies:

pip install -r requirements.txt

Set up ChromeDriver:
Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
Extract the executable and place it in a directory included in your system's PATH.

Edit the scraper.py file to add your Sense login credentials.

Run the scraper:

python scraper.py

Docker Installation

Clone this repository:

git clone https://github.com/yourusername/sense-scraper.git
cd sense-scraper

Build the Docker image:

docker build -t sense-scraper .

Run the Docker container, passing your Sense login credentials as environment variables:

docker run -e SENSE_USERNAME=your_username -e SENSE_PASSWORD=your_password sense-scraper
Replace your_username and your_password with your Sense login credentials.

Docker-compose

Alternatively, you can use docker-compose to manage the Docker container. Edit the docker-compose.yml file to include your environment variables and run:

docker-compose up -d

Environment Variables

SENSE_USERNAME: Your Sense Home Energy Monitor login username.
SENSE_PASSWORD: Your Sense Home Energy Monitor login password.

License

This project is licensed under the MIT License - see the LICENSE file for details.
