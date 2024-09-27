# 📊 Apple Stock Data Scraper

This Python project scrapes historical stock data for Apple Inc. (AAPL) from Yahoo Finance and saves it in a CSV file. It’s a great way to learn **web scraping** and **data handling** with Python.

## Project Overview

The script automatically retrieves Apple’s historical stock data, which includes:

- **Date**: The trading date.
- **Open, High, Low, Close Prices**: Stock prices for each trading day.
- **Adjusted Close**: Adjusted prices considering corporate actions (e.g., splits).
- **Volume**: The number of shares traded on that day.

All this data is saved in a CSV file that can be used for further analysis in tools like Excel, Python (e.g., Pandas), or any data visualization tool.

## Key Features

- **Automated Web Scraping**: Gathers the latest stock data automatically from Yahoo Finance.
- **Data Export**: Saves the data in CSV format, making it easy to analyze.
- **Clean Code**: The project is structured in a way that’s easy to understand and modify.

## Requirements

You will need the following libraries to run the script:

- `requests`: For fetching web content.
- `BeautifulSoup`: For parsing HTML and extracting data.
- `csv`: Built-in Python module for writing to CSV files.

## Learning Goals

This project will help you:

- Get hands-on experience with **web scraping**.
- Practice organizing and storing data into **CSV files**.
- Understand how to interact with **HTML** using Python libraries.

## How It Works

1. **Web Scraping**: The script fetches the web page containing Apple’s historical stock data using `requests`.
2. **HTML Parsing**: `BeautifulSoup` parses the page, extracting useful data from HTML tags.
3. **Data Storage**: The extracted data (Date, Prices, Volume) is written to a CSV file, making it easy to work with in other tools.


