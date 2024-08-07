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
    osebe = []
    blocks = polepsano_soup.find_all('div', class_='tile__item')
    
    if not blocks:
        print("Ni najdenih 'tile' elementov.")
    
    for block in blocks:
        ime_in_starost = block.find('p', class_='type-16-18-small').get_text(strip=True) if block.find('p', class_='type-16-18-small') else 'Ni imena'
        poklic = block.find('p', class_='tile__description type-14-16').get_text(strip=True) if block.find('p', class_='tile__description type-14-16') else 'Ni poklica'
        
        if ', ' in ime_in_starost:
            ime, starost = ime_in_starost.rsplit(', ', 1)
        else:
            ime = ime_in_starost
            starost = None

        #shranimo le tiste osebe, ki imajo definirano starost
        if starost:
            osebe.append([ime, starost, poklic])
    return osebe

def shrani_v_csv(podatki, ime_datoteke, mapa):
    if not podatki:
        print(f"Ni podatkov za shranjevanje v {ime_datoteke}.")
        return
    
    if not os.path.exists(mapa):
        os.makedirs(mapa)

    celotna_pot = os.path.join(mapa, ime_datoteke)

    with open(ime_datoteke, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ime', 'Starost', 'Poklic'])
        writer.writerows(podatki)
    print(f"Podatki so shranjeni v {ime_datoteke}.")

for day in range(1, 32):
    #pridobimo podatke za julij in avgust
    podatki_jul = podatki_julij(day)
    podatki_avg = podatki_avgust(day)

    izlusceni_jul = izlusci_podatke(podatki_jul)
    izlusceni_avg = izlusci_podatke(podatki_avg)

    shrani_v_csv(izlusceni_jul, f'famous_birthdays_july{day}.csv', 'podatki')
    shrani_v_csv(izlusceni_avg, f'famous_birthdays_august{day}.csv', 'podatki')
