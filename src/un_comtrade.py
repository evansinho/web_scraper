# src/un_comtrade.py
import requests
import pandas as pd
from config import URLS

BASE_URL = URLS["un_comtrade_api"]

def fetch_trade_data(commodity_code, year="2023"):
    """Fetch export data from UN Comtrade API."""
    params = {
        "max": 500,  
        "type": "C",  
        "freq": "A",  
        "px": "HS",  
        "ps": year,  
        "r": "566",  
        "p": "all",  
        "cc": commodity_code,  
        "fmt": "json",
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("dataset", [])  
    else:
        print("Error:", response.status_code)
        return None

def process_data(data):
    """Convert API response to structured DataFrame."""
    records = []
    for entry in data:
        records.append({
            "Year": entry.get("yr"),
            "Reporter": entry.get("rtTitle"),
            "Partner": entry.get("ptTitle"),
            "Trade Value (USD)": entry.get("TradeValue"),
            "Commodity": entry.get("cmdDescE"),
        })
    
    return pd.DataFrame(records)

if __name__ == "__main__":
    cashew_data = fetch_trade_data("080132")  
    cocoa_data = fetch_trade_data("180100")  
    
    if cashew_data:
        df_cashew = process_data(cashew_data)
        df_cashew.to_csv("data/cashew_trade.csv", index=False)
        print("Cashew trade data saved!")

    if cocoa_data:
        df_cocoa = process_data(cocoa_data)
        df_cocoa.to_csv("data/cocoa_trade.csv", index=False)
        print("Cocoa trade data saved!")
