import os
import pandas as pd
import re

def zdruzi_csv(mapa, nova_dat):
    #funkcija zdruzi vse csv-je v mapi v eno samo datoteko
    vse = [f for f in os.listdir(mapa) if f.endswith('.csv')]
    #seznam DataFrame-ov za združitev
    vsi_df = []

    for dat in vse:
        pot_do_dat = os.path.join(mapa, dat)
        df = pd.read_csv(pot_do_dat)
        vsi_df.append(df)

    #zdruzimo vse DF v enega
    zdruzen = pd.concat(vsi_df, ignore_index=True)

    zdruzen.to_csv(nova_dat, index=False)
    print(f'Datoteke so združene v {nova_dat}.')

def dodaj_rojstni_dan(mapa):
    # Seznam vseh CSV datotek v mapi
    vse_datoteke = [f for f in os.listdir(mapa) if f.endswith('.csv')]
    
    for datoteka in vse_datoteke:
        # Iz imena datoteke pridobi mesec in dan
        match = re.search(r'famous_birthdays_(\w+)(\d+).csv', datoteka)
        if match:
            mesec_imenik, dan = match.groups()
            
            # Pretvori mesec iz besede v številko
            meseci = {'july': '07', 'august': '08'}
            mesec = meseci.get(mesec_imenik.lower(), 'Unknown')
            
            # Preberi obstoječi CSV v DataFrame
            pot_do_datoteke = os.path.join(mapa, datoteka)
            df = pd.read_csv(pot_do_datoteke)
            
            # Dodaj stolpec z rojstnim dnevom
            df['Rojstni dan'] = f'{mesec}-{dan}'
            
            # Shrani nazaj v CSV
            df.to_csv(pot_do_datoteke, index=False)
            print(f"Stolpec 'Rojstni dan' dodan v {datoteka}.")
        
