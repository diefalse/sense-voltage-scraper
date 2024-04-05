import os
import logging
import time
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set up logging
logging.basicConfig(filename='/app/scraper.log', level=logging.ERROR, format='%(asctime)s - %(message)s')

# Function to perform login using Selenium
def login(driver):
    username = os.getenv('SENSE_USERNAME')
    password = os.getenv('SENSE_PASSWORD')
    try:
        driver.get('https://home.sense.com/login')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
        driver.find_element(By.NAME, "email").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]").click()
        WebDriverWait(driver, 20).until(EC.url_contains("https://home.sense.com/now"))

        # Navigate to power-quality page
        driver.get('https://home.sense.com/labs/power-quality')
        WebDriverWait(driver, 20).until(EC.url_contains("https://home.sense.com/labs/power-quality"))

    except TimeoutException:
        logging.error("Timeout occurred while logging in")
        raise
    except Exception as e:
        logging.error(f"An error occurred during login: {e}")
        raise

# Function to scrape the voltage information using Selenium
def scrape_voltage(driver, prev_data):
    try:
        l1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='voltage__container-stats header now']//span[contains(@class, 'data')][1]")))
        l2_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='voltage__container-stats header now']//span[contains(@class, 'data')][2]")))
        
        l1_text = l1_element.text
        l2_text = l2_element.text
        
        if prev_data is None or l1_text != prev_data['L1 Voltage'] or l2_text != prev_data['L2 Voltage']:
            return l1_text, l2_text
        else:
            return None, None
    except TimeoutException:
        logging.error("Timeout occurred while scraping voltage information")
        raise
    except NoSuchElementException as e:
        logging.error(f"Element not found while scraping voltage information: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while scraping voltage information: {e}")
        raise

# Function to write data to CSV file with timestamps and headers
def write_to_csv_with_timestamp(data, file_path):
    try:
        if not os.path.exists(file_path):
            data.to_csv(file_path, index=False)
        else:
            data.to_csv(file_path, mode='a', index=False, header=False)
    except PermissionError:
        logging.error("Permission denied: Unable to write to CSV file")
    except Exception as e:
        logging.error(f"An error occurred while writing to CSV with timestamps: {e}")
        raise

# Main function
def main():
    print("="*48)
    print("           Sense Home Energy Monitor")
    print("        LABS - Power Quality - Scraper")
    print("="*48)
    print("\n   This script scrapes L1 and L2 voltages")
    print("   in realtime and logs them to a csv file.")
    print("\n  Make sure you set environment variables SENSE_USERNAME and SENSE_PASSWORD")
    print("   to your Sense login credentials.")
    print("\n             Version 1.1b")
    print("\n                  By: Simon Lively")
    print("              Email: livetru247@duck.com")
    print("="*48)

    # Set up Chrome options for headless mode
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    
    # Set up Chrome service and driver
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    
    # Perform login
    try:
        login(driver)
    except Exception as e:
        logging.error(f"Failed to log in: {e}")
        driver.quit()
        return

    # Initialize lists to store data
    timestamps = []
    l1_voltages = []
    l2_voltages = []

    # Initialize previous data
    prev_data = None

    # CSV file path
    file_path = '/app/voltage_data.csv'

    # Main loop to continuously scrape and update the data
    while True:
        try:
            l1_voltage, l2_voltage = scrape_voltage(driver, prev_data)
            if l1_voltage is not None and l2_voltage is not None:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"Timestamp: {timestamp}, L1 Voltage: {l1_voltage}, L2 Voltage: {l2_voltage}")
                timestamps.append(timestamp)
                l1_voltages.append(l1_voltage)
                l2_voltages.append(l2_voltage)
                prev_data = {'L1 Voltage': l1_voltage, 'L2 Voltage': l2_voltage}
                
                # Combine lists into DataFrame
                data = pd.DataFrame({'Timestamp': timestamps, 'L1 Voltage': l1_voltages, 'L2 Voltage': l2_voltages})
                
                # Write data to CSV file with a header if it's the first entry
                write_to_csv_with_timestamp(data, file_path)
                    
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Keyboard Interrupt: Exiting...")
            break
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
