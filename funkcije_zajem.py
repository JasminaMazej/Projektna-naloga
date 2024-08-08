from podatki import *
import requests
from bs4 import BeautifulSoup
import csv
import os

#sprehajamo se po današnjem dnevu
url = 'https://www.famousbirthdays.com/'
rezultat = requests.get(url)
vsebina = rezultat.text

soup = BeautifulSoup(vsebina, 'html.parser')
#print(soup.prettify())

def podatki_julij(dan):
    #pridobimo podatke za dan v mesecu julij
    if dan in range(1,32):
        spletna_jul = f'https://www.famousbirthdays.com/july{dan}.html'
        content_jul = requests.get(spletna_jul).text
        polepsano_jul = BeautifulSoup(content_jul, 'html.parser')
        return polepsano_jul
    return None

def podatki_avgust(dan):
    #pridobimo podatke za dan v mesecu avgust
    if dan in range(1,32):
        spletna_avg = f'https://www.famousbirthdays.com/august{dan}.html'
        content_avg = requests.get(spletna_avg).text
        polepsano_avg = BeautifulSoup(content_avg, 'html.parser')
        return polepsano_avg
    return None

def podatki_februar(dan):
    #pridobimo podatke za dan v mesecu februar
    if dan in range(1,30):
        spletna_feb = f'https://www.famousbirthdays.com/february{dan}.html'
        content_feb = requests.get(spletna_feb).text
        polepsano_feb = BeautifulSoup(content_feb, 'html.parser')
        return polepsano_feb
    return None

def podatki_po_mesecih(mesec, dan):
    #pridobimo podatke za nek datum
    #mesec mora biti napisan z besedo, v angleščini, npr. 'october'
    if dan in range(1,32):
        spletna = f'https://www.famousbirthdays.com/{mesec}{dan}.html'
        content = requests.get(spletna).text
        polepsano = BeautifulSoup(content, 'html.parser')
        return polepsano
    return None

def izlusci_podatke(polepsano_soup):
    #izluscimo podatke o osebah iz zapisa
    osebe = []
    blocks = polepsano_soup.find_all('div', class_='tile__item')
    
    if not blocks:
        print(f'Ni najdenih \'tile\' elementov.')
    
    for block in blocks:
        ime_in_starost = block.find('p', class_='type-16-18-small').get_text(strip=True) if block.find('p', class_='type-16-18-small') else 'Ni imena'
        poklic = block.find('p', class_='tile__description type-14-16').get_text(strip=True) if block.find('p', class_='tile__description type-14-16') else 'Ni poklica'
        
        #ločimo ime in starost
        if ', ' in ime_in_starost:
            ime, starost = ime_in_starost.rsplit(', ', 1)
        else:
            ime = ime_in_starost
            starost = None

        #shranimo le tiste osebe, ki imajo definirano starost
        if starost:
            osebe.append([ime, starost, poklic])
    return osebe

def shrani_v_csv(podatki, datoteka, mapa):
    if not podatki:
        print(f'Ni podatkov za shranjevanje v {datoteka}.')
        return
    
    if not os.path.exists(mapa):
        os.makedirs(mapa)

    celotna_pot = os.path.join(mapa, datoteka)

    with open(celotna_pot, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ime', 'Starost', 'Poklic'])
        writer.writerows(podatki)
    print(f'Podatki so shranjeni v {datoteka}.')
