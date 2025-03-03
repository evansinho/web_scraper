# src/parser.py
from bs4 import BeautifulSoup

def extract_table_data(html_content):
    """Extracts tabular data from HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")  # Modify for specific tables
    rows = table.find_all("tr")

    extracted_data = []
    for row in rows:
        cols = row.find_all("td")
        extracted_data.append([col.text.strip() for col in cols])

    return extracted_data
