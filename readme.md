Sense Home Energy Monitor - Power Quality Scraper

Overview
This script scrapes real-time L1 and L2 voltage data from the Sense Home Energy Monitor's Power Quality Labs and logs it to a CSV file.

Features
Scrapes real-time L1 and L2 voltage data.
Logs data to a CSV file.
Configurable options via config.ini.
Dockerized for easy deployment.
Installation
Requirements
Python 3.8+
selenium module
pandas module
python-dotenv module
chromedriver-binary module
Chrome web browser
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/diefalse/sense-voltage-scraper.git
Navigate to the project directory:

bash
Copy code
cd sense-voltage-scraper
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Make sure to edit the config.ini file and provide your Sense login credentials and other configuration options.

Run the script:

bash
Copy code
python sense.py
Configuration
Before running the script, make sure to configure the config.ini file:

makefile
Copy code
[Credentials]
email = sense@example.com
password = your_password

[Paths]
data_file = voltage_data.csv
chromedriver_path = /path/to/chromedriver

[Logging]
error_log_file = scraper_errors.log
error_log_path = /path/to/error/log
Usage
Once the script is running, it will continuously scrape real-time L1 and L2 voltage data from the Sense Home Energy Monitor's Power Quality Labs and log it to the specified CSV file.

Docker
To run the scraper using Docker, follow these steps:

Make sure you have Docker installed on your system.

Build the Docker image:

bash
Copy code
docker build -t sense-scraper .
Run the Docker container:

bash
Copy code
docker run -d --name sense-scraper sense-scraper
Troubleshooting
If you encounter any issues or errors while running the scraper, please check the error logs (scraper_errors.log) for more information.

Credits
This scraper was developed by Simon Lively. For questions or inquiries, you can reach out via email: livetru247@duck.com.