import csv
import requests
from io import StringIO

def fetch_csv(url):
    """Download a CSV file and return rows."""
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.text
    reader = csv.DictReader(StringIO(data))
    return list(reader)

def main():
    url = "<PUT A SIMPLE CSV URL HERE>"
    print("Fetching CSV...")
    rows = fetch_csv(url)
    print(f"Got {len(rows)} rows")
    for row in rows[:5]:
        print(row)

if __name__ == "__main__":
    main()
