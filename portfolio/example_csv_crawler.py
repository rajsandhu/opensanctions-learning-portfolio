import csv
import requests
from io import StringIO

def fetch_csv(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_csv(raw_text):
    reader = csv.DictReader(StringIO(raw_text))
    return list(reader)

def main():
    url = "https://www.berlin.de/sen/finanzen/service/daten/beteiligungsbericht_2022.csv"
    raw = fetch_csv(url)
    rows = parse_csv(raw)
    print(f"Fetched {len(rows)} rows")
    for row in rows[:5]:
        print(row)

if __name__ == "__main__":
    main()
