Sense Home Energy Monitor Realtime Mains Voltage Scraper
=================================

This Docker container scrapes L1 and L2 voltages from the Sense Home Energy Monitor in real-time and logs them to a CSV file.  I have been experiencing voltage sag / drop and needed a way to log the mains voltages in real time.  
This Docker satisfies my needs and was written primarily for UnRaid as that is my primary Docker Container host.   You can simply use the scraper.py script standalone with the requirements for your OS if you do not want the Docker version.
This Docker utilizes a headless selenium instance to open and login to https://home.sense.com/ which when successful redirects to https://home.sense.com/now/ which is detected and then navigates to https://home.sense.com/labs/power-quality.

When utilizing the Sense Home - Labs - Power Quality webpage, the python script scrapes in realtime the L1 and L2 voltages for changes.  Depending on your power mains stability, this can change in miliseconds or minutes, these changes are logged in
the voltage_data.csv file for your consumption.   

There is a scraper.log file that will capture any errors with the scraper python script for troubleshooting assistance.

Environment Variables
---------------------
*   `SENSE_USERNAME`: Your Sense Home Energy Monitor login username.
*   `SENSE_PASSWORD`: Your Sense Home Energy Monitor login password.
*   Data file mapping: /appdata/ needs to be pointed to the location you wish to have the scraper.log and voltage_data.csv files placed.   This will need to be a R/W permission.

Data / File Mapping
-------------------
/appdata/:/user/home/appdata/


Port Mappings
-------
NONE

License
-------

This project is licensed - see the [LICENSE](LICENSE) file for details.
