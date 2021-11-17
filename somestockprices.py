import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

path = r"C:\Programação\Python\LCA_KUTOCSV.csv"
assert os.path.isfile(path)

workbench = pd.read_csv(r"C:\Programação\Python\LCA_KUTOCSV.csv", encoding="ISO-8859-1", sep=';')
stock_name = workbench['Ações']
price = workbench['Preço Atual']
x = 1

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for item in stock_name.head(-2):
    page = requests.get(f"https://br.financas.yahoo.com/quote/{item}.SA", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    span = soup.find_all("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    for n in span:
        workbench.loc[x, 'Preço Atual'] = n.text
        workbench.to_csv(path, index=False)
        x += 1
        print(f'{item}: {n.text} (SUCESSO)')

