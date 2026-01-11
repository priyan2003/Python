import pandas as pd
import requests

url = "https://api.github.com/users/priyan2003"
data = requests.get(url).json()

df = pd.DataFrame([data])  # wrap dict in a list
df.to_csv('test3.csv')
print(df)
d2 = pd.read_csv('test3.csv')
print(d2)
d3 = d2.to_json(orient = 'records')
print(d3)