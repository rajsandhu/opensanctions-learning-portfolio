# OpenSanctions Learning Portfolio

This repository documents my learning and experimentation with web scraping, data processing, and building small crawlers in Python. It is designed to show my process, progress, and approach to problem-solving in a way that can be reviewed by others, including the OpenSanctions team.

## Current Projects

The main portfolio folder contains my working scripts:

- **example_csv_crawler.py** – Fetches CSV data from a public Berlin dataset, parses it, and prints the first few rows. Demonstrates basic crawler functionality with Python and HTTP requests.
- **ihk_gewerbe_crawler.py** – Fetches CSV data from a GitHub repository of IHK Berlin business data. Shows CSV parsing and data inspection.
- **test_crawler.py** – Simple script to demonstrate Zavod-based crawler structure.

## Why I'm Doing This

This portfolio is meant to demonstrate my practical skills in Python, data handling, web scraping, and building simple crawlers. The goal is to create a traceable, iterative learning path showing my thought process and ability to tackle real-world datasets, including those relevant to OpenSanctions.

## How I Work

I use AI-assisted tools such as GitHub Copilot, ChatGPT, and Phind to explore solutions quickly. These tools help me test ideas and write maintainable code, but all work is manually reviewed to ensure correctness.

## How to Run

From the root of this repo:

```bash
python portfolio/example_csv_crawler.py
python portfolio/ihk_gewerbe_crawler.py
python portfolio/test_crawler.py
```
Expected output:

- example_csv_crawler.py prints a few rows of the Berlin Beteiligungsbericht CSV.
- ihk_gewerbe_crawler.py prints the first row of the IHK CSV.
- test_crawler.py prints "Hello Zavod! This is my test crawler script."

## Notes

This is a learning-focused repository, primarily aimed at showing my approach and progress. It is intended for review by the OpenSanctions team and others interested in my practical skills.

## Next Steps

- Extend existing crawlers into full Zavod-style scrapers for structured data ingestion.
- Experiment with more complex datasets (JSON, APIs).
- Document lessons learned and improvements iteratively to show growth over time.