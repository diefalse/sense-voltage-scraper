# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install ChromeDriver and other dependencies
RUN apt-get update && apt-get install -y chromium-driver
RUN pip install --no-cache-dir pandas selenium

# Set the working directory in the container
WORKDIR /app

# Copy the scraper script into the container
COPY scraper.py /app

# Run the scraper script when the container launches
CMD ["python", "scraper.py"]
