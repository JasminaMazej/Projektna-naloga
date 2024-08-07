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


def dodaj_rojstni_dan(mapa_za_csv):
    # Slovar za pretvorbo imen mesecev v številke
    meseci = {
        'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05',
        'june': '06', 'july': '07', 'august': '08', 'september': '09', 'october': '10',
        'november': '11', 'december': '12'
    }
    
    for datoteka in os.listdir(mapa_za_csv):
        if datoteka.endswith('.csv'):
            # Preveri, ali ime datoteke ustreza vzorcu
            print(f"Obdelujem datoteko: {datoteka}")  # Diagnosticiranje
            match = re.match(r'famous_birthdays_(\D+)(\d+).csv', datoteka)
            if match:
                mesec_imenik, dan = match.groups()
                
                # Pretvori mesec v številko
                mesec = meseci.get(mesec_imenik.lower(), 'Unknown')
                print(f"Mesec imenik: {mesec_imenik}, Mesec številka: {mesec}")  # Diagnosticiranje
                
                # Prilagodi format rojstnega dne
                if mesec == 'Unknown':
                    rojstni_dan = f'Unknown-{dan}'
                else:
                    # Zagotovi, da dan ima pravilno formatiranje (01-31) in mesec dvomestni format
                    dan = dan.zfill(2)  # Dodaj ničlo spredaj, če je dan enomesten
                    rojstni_dan = f'{dan}-{mesec}'

                # Preberi CSV datoteko
                df = pd.read_csv(os.path.join(mapa_za_csv, datoteka))
                
                # Dodaj stolpec z rojstnim dnevom
                df['Rojstni dan'] = rojstni_dan
                
                # Shrani posodobljeno datoteko
                df.to_csv(os.path.join(mapa_za_csv, datoteka), index=False)
                print(f"Posodobljena datoteka: {datoteka} - Rojstni dan: {rojstni_dan}")
            else:
                print(f"Imena datoteke {datoteka} ni mogoče razbrati.")
        else:
            print(f"Datoteka {datoteka} ni CSV format.")