import requests
from bs4 import BeautifulSoup
import csv
import time

def pridobi_podatke_o_rojstnih_dnevih(mesec, dan):
    # Formatiranje meseca in dneva z dvema mestoma (npr. 08 za avgust, 06 za šesti dan)
    mesec_dan = f"{mesec:02}-{dan:02}"
    
    # Prilagojen URL za določen datum
    url = f"https://www.imdb.com/search/name/?birth_monthday={mesec_dan}"

    # Določitev uporabniškega agenta
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Pošiljanje HTTP GET zahteve z glavo
    rezultat = requests.get(url, headers=headers)

    # Preverjanje uspešnosti zahteve
    if rezultat.status_code == 200:
        # Parsiranje HTML vsebine
        soup = BeautifulSoup(rezultat.content, 'html.parser')

        # Iskanje vseh osebnosti na strani
        osebnosti = soup.find_all('div', class_='lister-item mode-detail')

        # Ime datoteke temelji na datumu
        ime_datoteke = f"imdb_birthdays_{mesec_dan}.csv"

        # Odpiranje CSV datoteke za pisanje
        with open(ime_datoteke, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Ime', 'Poklic', 'Znan po'])

            # Obdelava posameznih osebnosti
            for oseba in osebnosti:
                # Pridobivanje imena
                ime_element = oseba.find('h3', class_='lister-item-header').find('a')
                ime = ime_element.get_text(strip=True) if ime_element else 'Ni imena'

                # Pridobivanje poklica
                poklic_element = oseba.find('p', class_='text-muted text-small')
                poklic = poklic_element.get_text(strip=True).split('|')[0].strip() if poklic_element else 'Ni poklica'

                # Pridobivanje znanih del
                znan_po_element = oseba.find_all('p')[2].find_all('a')
                znan_po = ', '.join([delce.get_text(strip=True) for delce in znan_po_element]) if znan_po_element else 'Ni znanih del'

                # Zapisovanje podatkov v CSV datoteko
                writer.writerow([ime, poklic, znan_po])
        
        # Dodana časovna zakasnitev
        time.sleep(2)
    else:
        print(f"Napaka pri dostopu do strani: {rezultat.status_code}")

# Primer uporabe funkcije za 6. avgust
pridobi_podatke_o_rojstnih_dnevih(8, 6)
