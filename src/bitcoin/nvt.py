import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime

url = "https://api.blockchain.info/charts/n-transactions?format=json&timespan=30days"

response = requests.get(url)
data = response.json()

dates = []
volumes = []	 
prices = []
for point in data['values']:
    dates.append(datetime.datetime.fromtimestamp(point['x']).strftime('%Y-%m-%d'))
    volumes.append(point['y'])
    prices.append(point['x'])
 
df = pd.DataFrame({'date': dates, 'volume': volumes})
df['volume'] = df['volume'].astype(float)
df['prices'] = df['volume'].astype(float)
df['volume_usd'] = df['volume']*df['prices']


url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily"
response = requests.get(url)
data = response.json()

market_cap_data = [(datetime.datetime.fromtimestamp(item[0]/1000).strftime('%Y-%m-%d'), item[1]) for item in data["market_caps"]]
df2 = pd.DataFrame(market_cap_data, columns=['Date', 'Market Cap'])
df2['Market Cap'] = df2['Market Cap'].astype(float)
df2 = df2.groupby('Date').mean().reset_index()
df2['nvt'] = df2['Market Cap']/df['volume_usd']

st.write("#🧊 Blockchain Intelligence Lab 👨🏻‍🔬")
st.line_chart(df2.set_index('Date')['nvt'])