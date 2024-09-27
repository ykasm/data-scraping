from bs4 import BeautifulSoup
import requests
import csv

# URL for Yahoo Finance historical data for AAPL
url = 'https://finance.yahoo.com/quote/AAPL/history/?period1=345479400&period2=1726773686'
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
response = requests.get(url, headers=HEADERS)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store extracted data
Date_list = []
Open = []
High = []
Low = []
Close = []
Adj_Close = []
Volume = []

# Find all rows with historical data
apple_data = soup.findAll('tr', class_='BdT')  # Adjust class if needed for correct table rows

# Loop through each row of data
for apple in apple_data:
    columns = apple.find_all('td')  # Get all the <td> elements in each row
    
    if len(columns) == 7:  # Ensure the row has 7 columns (Date, Open, High, Low, Close, Adj Close, Volume)
        Date_list.append(columns[0].text.strip())      # Date
        Open.append(columns[1].text.strip())           # Open
        High.append(columns[2].text.strip())           # High
        Low.append(columns[3].text.strip())            # Low
        Close.append(columns[4].text.strip())          # Close
        Adj_Close.append(columns[5].text.strip())      # Adj Close
        Volume.append(columns[6].text.strip())         # Volume

# Open a CSV file to write the data
with open('apple_stock_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
    
    # Write the data
    for i in range(len(Date_list)):
        writer.writerow([Date_list[i], Open[i], High[i], Low[i], Close[i], Adj_Close[i], Volume[i]])

print("Data saved to 'apple_stock_data.csv'")
