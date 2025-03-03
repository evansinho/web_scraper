# src/faostat.py

import requests
import pandas as pd
from config import FAOSTAT_URL, COMMODITIES, DATA_DIR
import os


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.fao.org/faostat/en/#data",
}

def fetch_faostat_data(commodity):
    """Fetch FAOSTAT data for a given commodity."""
    print(f"📡 Fetching FAOSTAT export data for {commodity}...")
    
    params = {
        "area": "all",
        "item": COMMODITIES.get(commodity.lower(), None),
        "element": "export_quantity",
        "format": "json",
    }

    response = requests.get(FAOSTAT_URL, headers=HEADERS, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"⚠️ Error fetching {commodity} data: {response.status_code}")
        return None


def parse_faostat_data(data):
    """Convert FAOSTAT JSON response into a structured DataFrame."""
    structured_data = []
    
    for entry in data:
        structured_data.append({
            "Country": entry.get("area"),
            "Commodity": entry.get("item"),
            "Year": entry.get("year"),
            "Export Quantity (tons)": entry.get("value")
        })

    return pd.DataFrame(structured_data)


def save_faostat_data(commodity, df):
    """Save FAOSTAT export data to CSV."""
    if df is None or df.empty:
        print(f"⚠️ No data to save for {commodity}.")
        return

    os.makedirs(DATA_DIR, exist_ok=True)
    file_path = os.path.join(DATA_DIR, f"faostat_{commodity.lower()}.csv")
    
    df.to_csv(file_path, index=False)
    print(f"✅ FAOSTAT export data saved: {file_path}")
