  Sense Home Energy Monitor Scraper

Sense Home Energy Monitor Scraper
=================================

This Docker container scrapes L1 and L2 voltages from the Sense Home Energy Monitor in real-time and logs them to a CSV file.

Usage
-----

1.  Install Docker on your system if you haven't already.
2.  Clone this repository:

    git clone https://github.com/yourusername/sense-scraper.git
    cd sense-scraper
    

3.  Set up environment variables for your Sense login credentials:

    export SENSE_USERNAME=your_username
    export SENSE_PASSWORD=your_password
    

4.  Edit the `docker-compose.yml` file to set your timezone if necessary.
5.  Build and run the Docker container:

    docker-compose up -d
    

The scraper will start running inside the Docker container, logging voltage data to a CSV file.

Environment Variables
---------------------

*   `SENSE_USERNAME`: Your Sense Home Energy Monitor login username.
*   `SENSE_PASSWORD`: Your Sense Home Energy Monitor login password.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
