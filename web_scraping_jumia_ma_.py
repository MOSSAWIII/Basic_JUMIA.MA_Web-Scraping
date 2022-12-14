!pip install requests
!pip install bs4

from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd

def scrap():
  pcs_ = []
  prices_ = []
  old_ = []
  for i in range(1, 18):
    jumia_pc = requests.get(f'https://www.jumia.ma/pc-portables/?page={i}#catalog-listing').content
    soup = bs(jumia_pc, 'html.parser')

    pcs = soup.find_all('h3', class_='name')
    prices = soup.find_all('div', class_='prc')
    old_prices = soup.find_all('div', class_='old')

    for i,j,k in zip(pcs, prices, old_prices):
      if len(i.get_text())!=0 and len(j.get_text())!=0 and len(k.get_text())!=0:
        pcs_.append(i.get_text())
        prices_.append(j.get_text())
        old_.append(k.get_text())

  table = np.array(list(zip(pcs_, prices_, old_)))
  df = pd.DataFrame(table, columns = ['item', 'current price', 'old price'])
  return df

print(scrap())
