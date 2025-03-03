# src/config.py
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
}

# Website URLs
URLS = {
    "trade_map": "https://www.trademap.org/Country_SelProductCountry.aspx",
    "un_comtrade_api": "https://comtrade.un.org/api/get?",
}

# Selenium Configuration
SELENIUM_OPTIONS = [
    "--headless",  
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]

# FAOSTAT API URL
FAOSTAT_URL = "https://fenixservices.fao.org/faostat/api/v1/en/data/TM"

# Commodity Codes
COMMODITIES = {
    "cashew": "080132",
    "cocoa": "180100"
}

# Directory to save data
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
