# -*- coding: utf-8 -*-
"""natural_gas_prices.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15MaBUVrqFkmaiLdhzWmTB28YyejIJerb
"""



import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", width="675", border="0", cellspacing="0", cellpadding="2")
rows = table.find_all("tr")

data = []
for row in rows:
    cols = row.find_all(["th", "td"])
    cols = [col.text.strip() for col in cols if col.text.strip() != '']
    data.append(cols)

data = [row for row in data if row]

df = pd.DataFrame(data[1:], columns=data[0])
df.to_csv("Henry_hub_gas_price.csv", index=False)

