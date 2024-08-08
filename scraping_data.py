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
    #izluscimo podatke o osebah iz zapisa
    osebe = []
    blocks = polepsano_soup.find_all('div', class_='tile__item')
    
    if not blocks:
        print("Ni najdenih 'tile' elementov.")
    
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

def shrani_v_csv(podatki, ime_datoteke, mapa):
    if not podatki:
        print(f"Ni podatkov za shranjevanje v {ime_datoteke}.")
        return
    
    if not os.path.exists(mapa):
        os.makedirs(mapa)

    celotna_pot = os.path.join(mapa, ime_datoteke)

    with open(celotna_pot, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Ime', 'Starost', 'Poklic'])
        writer.writerows(podatki)
    print(f"Podatki so shranjeni v {ime_datoteke}.")

def podatki_po_mesecih(mesec, dan):
    #pridobimo podatke za nek
    if dan in range(1,32):
        spletna = f'https://www.famousbirthdays.com/{mesec}{dan}.html'
        content = requests.get(spletna).text
        polepsano = BeautifulSoup(content, 'html.parser')
        return polepsano
    return None

#for day in range(1, 32):
    #pridobimo podatke za julij in avgust
#    podatki_jul = podatki_julij(day)
#    podatki_avg = podatki_avgust(day)
#
#    izlusceni_jul = izlusci_podatke(podatki_jul)
#    izlusceni_avg = izlusci_podatke(podatki_avg)
#
#    shrani_v_csv(izlusceni_jul, f'famous_birthdays_july{day}.csv', 'podatki')
#    shrani_v_csv(izlusceni_avg, f'famous_birthdays_august{day}.csv', 'podatki')
# 
#    pod_jan = podatki_po_mesecih('january', day)
#    pod_mar = podatki_po_mesecih('march', day)
#    pod_maj = podatki_po_mesecih('may', day)
#    pod_okt = podatki_po_mesecih('october', day)
#    pod_dec = podatki_po_mesecih('december', day)
#
#    i_jan = izlusci_podatke(pod_jan)
#    i_mar = izlusci_podatke(pod_mar)
#    i_maj = izlusci_podatke(pod_maj)
#    i_okt = izlusci_podatke(pod_okt)
#    i_dec = izlusci_podatke(pod_dec)
#
#    shrani_v_csv(i_jan, f'famous_birthdays_january{day}.csv', 'podatki')
#    shrani_v_csv(i_mar, f'famous_birthdays_march{day}.csv', 'podatki')
#    shrani_v_csv(i_maj, f'famous_birthdays_may{day}.csv', 'podatki')
#    shrani_v_csv(i_okt, f'famous_birthdays_october{day}.csv', 'podatki')
#    shrani_v_csv(i_dec, f'famous_birthdays_december{day}.csv', 'podatki')


def podatki_februar(dan):
    #pridobimo podatke za mesec februar
    if dan in range(1,30):
        spletna_feb = f'https://www.famousbirthdays.com/february{dan}.html'
        content_feb = requests.get(spletna_feb).text
        polepsano_feb = BeautifulSoup(content_feb, 'html.parser')
        return polepsano_feb
    return None

#for day in range(1, 30):
#    pod_feb = podatki_februar(day)
#    izlusceni_feb = izlusci_podatke(pod_feb)
#    shrani_v_csv(izlusceni_feb, f'famous_birthday_february{day}.csv', 'podatki')


for day in range(23, 30):
    pod_apr = podatki_po_mesecih('april', day)
    pod_jun = podatki_po_mesecih('june', day)
    pod_sep = podatki_po_mesecih('september', day)
    pod_nov = podatki_po_mesecih('november', day)

    izl_apr = izlusci_podatke(pod_apr)
    izl_jun = izlusci_podatke(pod_jun)
    izl_sep = izlusci_podatke(pod_sep)
    izl_nov = izlusci_podatke(pod_sep)

    shrani_v_csv(izl_apr, f'famous_birthdays_april{day}.csv', 'podatki')
    shrani_v_csv(izl_jun, f'famous_birthdays_june{day}.csv', 'podatki')
    shrani_v_csv(izl_sep, f'famous_birthdays_september{day}.csv', 'podatki')
    shrani_v_csv(izl_nov, f'famous_birthdays_november{day}.csv', 'podatki')

