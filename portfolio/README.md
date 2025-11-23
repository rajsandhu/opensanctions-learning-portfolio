# Portfolio: Working Crawlers

This folder contains working examples of web crawlers and data extraction scripts built using [Zavod](https://github.com/openownership/zavod) and OpenSanctions frameworks.

## Crawlers

### 1. `example_csv_crawler.py`
- Fetches structured CSV data from public sources.
- Demonstrates basic usage of Zavod's `Context` and `Entity` APIs.

### 2. `ihk_gewerbe_crawler.py`
- Extracts publicly available business registration data from IHK sources.
- Uses Zavod for structured data modeling and output in standard formats.

### 3. `test_crawler.py`
- Sandbox/testing crawler for experimenting with parsing logic and new sources.

## How to Run

1. Ensure Zavod is installed:

```bash
pip install zavod
```

2. Run a crawler:

```bash
python example_csv_crawler.py
```

3. Output is structured JSON data ready for OpenSanctions ingestion.

## Notes

- Crawlers are built around Zavod, no modifications to Zavod itself are needed.
- Designed for learning and demonstration purposes.