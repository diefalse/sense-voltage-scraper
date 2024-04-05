<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sense Home Energy Monitor - Power Quality Scraper</title>
</head>

<body>

    <h1>Sense Home Energy Monitor - Power Quality Scraper</h1>

    <img src="sense_logo.png" alt="Sense Logo" width="200">

    <h2>Overview</h2>

    <p>This script scrapes real-time L1 and L2 voltage data from the Sense Home Energy Monitor's Power Quality Labs and logs
        it to a CSV file.</p>

    <h2>Features</h2>

    <ul>
        <li>Scrapes real-time L1 and L2 voltage data.</li>
        <li>Logs data to a CSV file.</li>
        <li>Configurable options via <code>config.ini</code>.</li>
        <li>Dockerized for easy deployment.</li>
    </ul>

    <h2>Installation</h2>

    <h3>Requirements</h3>

    <ul>
        <li>Python 3.8+</li>
        <li><code>selenium</code> module</li>
        <li><code>pandas</code> module</li>
        <li><code>python-dotenv</code> module</li>
        <li><code>chromedriver-binary</code> module</li>
        <li>Chrome web browser</li>
    </ul>

    <h3>Installation Steps</h3>

    <ol>
        <li>Clone the repository:</li>
        <code>git clone https://github.com/diefalse/sense-voltage-scraper.git</code>
        <li>Navigate to the project directory:</li>
        <code>cd sense-voltage-scraper</code>
        <li>Install the required Python packages:</li>
        <code>pip install -r requirements.txt</code>
        <li>Make sure to edit the <code>config.ini</code> file and provide your Sense login credentials and other configuration options.</li>
        <li>Run the script:</li>
        <code>python sense.py</code>
    </ol>

    <h2>Configuration</h2>

    <p>Before running the script, make sure to configure the <code>config.ini</code> file:</p>

    <pre>
[Credentials]
email = sense@example.com
password = your_password

[Paths]
data_file = voltage_data.csv
chromedriver_path = /path/to/chromedriver

[Logging]
error_log_file = scraper_errors.log
error_log_path = /path/to/error/log
    </pre>

    <h2>Usage</h2>

    <p>Once the script is running, it will continuously scrape real-time L1 and L2 voltage data from the Sense Home
        Energy Monitor's Power Quality Labs and log it to the specified CSV file.</p>

    <h2>Docker</h2>

    <p>To run the scraper using Docker, follow these steps:</p>

    <ol>
        <li>Make sure you have Docker installed on your system.</li>
        <li>Build the Docker image:</li>
        <code>docker build -t sense-scraper .</code>
        <li>Run the Docker container:</li>
        <code>docker run -d --name sense-scraper sense-scraper</code>
    </ol>

    <h2>Troubleshooting</h2>

    <p>If you encounter any issues or errors while running the scraper, please check the error logs
        (<code>scraper_errors.log</code>) for more information.</p>

    <h2>Credits</h2>

    <p>This scraper was developed by Simon Lively. For questions or inquiries, you can reach out via email:
        livetru247@duck.com.</p>

</body>

</html>
