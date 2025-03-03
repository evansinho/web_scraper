# src/scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import URLS, SELENIUM_OPTIONS

def fetch_html_selenium(url):
    """Fetch HTML content using Selenium for JavaScript-rendered pages."""
    
    # Configure headless mode for performance
    options = Options()
    for opt in SELENIUM_OPTIONS:
        options.add_argument(opt)

    # Set up Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    print(f"Fetching: {url} using Selenium...")
    driver.get(url)
    
    # Wait for JavaScript to load (adjust as needed)
    time.sleep(5)

    # Get the page source
    html_content = driver.page_source
    driver.quit()

    return html_content


def scrape_trade_map():
    """Fetch trade map page using Selenium."""
    url = URLS["trade_map"]  
    html_content = fetch_html_selenium(url)

    if not html_content:
        print(f"Error: Could not retrieve HTML from {url}")

    return html_content
