FROM diefalse/sense-voltage-scraper:latest
LABEL org.opencontainers.image.authors = "DieFalse"
LABEL org.opencontainers.image.source = "https://github.com/dieflase/sense-voltage-scraper"

# Use a base image suitable for running Python scripts
FROM python:3.9-slim

# Set up environment variables
ENV TZ=America/New_York
ENV SENSE_USERNAME=""
ENV SENSE_PASSWORD=""

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the Python script and any additional files
COPY scraper.py /app/

# Install Python dependencies
RUN pip install selenium pandas

# Expose volume for data and logs
VOLUME /appdata

# Set the command to run the scraper script
CMD ["python", "scraper.py"]
