import requests
from bs4 import BeautifulSoup
import csv

#sprehajamo se po današnjem dnevu
url = 'https://www.famousbirthdays.com/'
rezultat = requests.get(url)
vsebina = rezultat.text

soup = BeautifulSoup(vsebina, 'html.parser')
#print(soup.prettify())

def podatki_julij(dan):
    #pridobimo podatke za mesec julij
    if dan in range(1,32):
        spletna_jul = f'https://www.famousbirthdays.com/july{dan}.html'
        content_jul = requests.get(spletna_jul).text
        polepsano_jul = BeautifulSoup(content_jul, 'html.parser')
        return polepsano_jul
    return None

def podatki_avgust(dan):
    #pridobimo podatke za mesec avgust
    if dan in range(1,32):
        spletna_avg = f'https://www.famousbirthdays.com/august{dan}.html'
        content_avg = requests.get(spletna_avg).text
        polepsano_avg = BeautifulSoup(content_avg, 'html.parser')
        return polepsano_avg
    return None

#poskusimo za naključen dan
#print(podatki_julij(7))

def izlusci_podatke(polepsano_soup):
    #funkcija izlusci podatke o osebah
    osebe = []
    blocks = polepsano_soup.find_all('div', class_='tile')
    for block in blocks:
        ime = block.find('a', class_='name').get_text(strip=True) if block.find('a', class_='name') else 'Ni imena'
        poklic = block.find('p', class_='title').get_text(strip=True) if block.find('p', class_='title') else 'Ni poklica'
        starost = block.find('p', class_='age').get_text(strip=True) if block.find('p', class_='age') else 'Ni starosti'
        osebe.append([ime, starost, poklic])
    return osebe

def shrani_v_csv(podatki, tabela_csv):
    with open(tabela_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ime', 'Poklic', 'Starost'])
        writer.writerows(podatki)


