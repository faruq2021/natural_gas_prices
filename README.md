# natural_gas_prices
Natural Gas Price Scraper
This repository contains a Python script to extract monthly (or daily, with modification) natural gas prices from the EIA website (http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm) and save them as a CSV file.

Files:

natural_gas_prices.py: Python script for extracting and saving data
monthly_prices.csv: CSV file containing monthly natural gas prices (Date, Price) 
https://github.com/faruq2021/natural_gas_prices/blob/main/monthly_prices.csv


Libraries Used:

requests: Allows making HTTP requests to websites
beautifulsoup4: Parses HTML content
pandas: Data manipulation and analysis library
Process:

The script retrieves the HTML content of the EIA webpage using requests.
It uses beautifulsoup4 to parse the HTML and find the table containing the desired data (monthly or daily).
The script iterates through the table rows, extracting date and price data.
Extracted data is organized into a pandas DataFrame.

The DataFrame is saved as a CSV file named monthly_prices.csv (or daily_prices.csv for daily data).

Challenges Faced:

Identifying the correct table element within the HTML structure might require adjustments depending on website updates.
Handling potential changes in data format or table structure.
Extracting Daily Prices:

The provided code snippet focuses on extracting monthly prices from the website. Daily price isn't currently present on the website.


Running the Script:

Install the required libraries: pip install requests beautifulsoup4 pandas
Save the script as natural_gas_prices.py in a directory.
Run the script from the command line: python natural_gas_prices.py
