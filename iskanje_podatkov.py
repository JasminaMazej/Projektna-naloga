import re
import requests
import csv
from bs4 import BeautifulSoup


def html(url_povezava):
    """poišče html, podane spletne strani in ga vrne kot niz"""
    html = requests.get(url_povezava).text
    doc = BeautifulSoup(html, 'html.parser')
    return doc

url = 'https://www.bolha.com/avto-oglasi'
rezultat = html(url)
#print(rezultat)

sez = []


for stran in range(1, 12):
    url1 = f'https://www.bolha.com/avto-oglasi?page={stran}'
    stran = requests.get(url1).text
    doc1 = BeautifulSoup(stran, 'html.parser')
    

 
