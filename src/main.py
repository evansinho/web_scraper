# src/main.py

from scraper import scrape_trade_map
from html_parser import extract_table_data
from exporter import save_to_csv
from un_comtrade import fetch_trade_data, process_data
from faostat_scraper import fetch_faostat_data, save_faostat_data

def main():
    """Run the full scraping process."""
    
    ## 1️⃣ Fetch Trade Map Data (Selenium Scraper)
    print("📡 Scraping Trade Map data...")
    html_content = scrape_trade_map()
    
    if not html_content:  
        print("❌ Error: No HTML content retrieved!")
        return
    
    print(html_content[:500])  # Debug: Print first 500 characters
    structured_data = extract_table_data(html_content)
    save_to_csv(structured_data, "data/trade_map_data.csv")
    print("✅ Trade Map data saved!")


    ## 2️⃣ Fetch UN Comtrade Data (API Scraper)
    print("\n📡 Fetching UN Comtrade export data...")
    
    cashew_data = fetch_trade_data("080132")  # Cashew Nuts
    cocoa_data = fetch_trade_data("180100")  # Cocoa Beans

    if cashew_data:
        df_cashew = process_data(cashew_data)
        df_cashew.to_csv("data/cashew_trade.csv", index=False)
        print("✅ Cashew trade data saved!")

    if cocoa_data:
        df_cocoa = process_data(cocoa_data)
        df_cocoa.to_csv("data/cocoa_trade.csv", index=False)
        print("✅ Cocoa trade data saved!")


    ## 3️⃣ Fetch FAOSTAT Export Data (API Scraper)
    print("\n📡 Fetching FAOSTAT export data...")

    for commodity in ["Cashew", "Cocoa"]:
        df_faostat = fetch_faostat_data(commodity)
        if df_faostat is not None:
            save_faostat_data(commodity, df_faostat)

if __name__ == "__main__":
    main()
