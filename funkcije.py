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
    # Slovar za pretvorbo imen mesecev v številke
    meseci = {
        'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05',
        'june': '06', 'july': '07', 'august': '08', 'september': '09', 'october': '10',
        'november': '11', 'december': '12'
    }
    
    for datoteka in os.listdir(mapa):
        if datoteka.endswith('.csv'):
            #preveri, ali ime datoteke ustreza vzorcu
            print(f"Obdelujem datoteko: {datoteka}")  
            match = re.match(r'famous_birthdays_(\D+)(\d+).csv', datoteka)
            if match:
                mesec_imenik, dan = match.groups()
                
                #pretvori mesec v številko
                mesec = meseci.get(mesec_imenik.lower(), 'Unknown')
                print(f"Mesec imenik: {mesec_imenik}, Mesec številka: {mesec}")  
                
                #prilagodi format rojstnega dne
                if mesec == 'Unknown':
                    rojstni_dan = f'{dan}-Unknown'
                else:
                    #zagotovi, da dan ima pravilno formatiranje in mesec dvomestni format
                    dan = dan.zfill(2)  #doda ničlo spredaj, če je dan enomesten
                    rojstni_dan = f'{dan}-{mesec}'

                #prebere CSV datoteko
                df = pd.read_csv(os.path.join(mapa, datoteka))
                
                #doda stolpec z rojstnim dnevom
                df['Rojstni dan'] = rojstni_dan
                
                #shrani posodobljeno datoteko
                df.to_csv(os.path.join(mapa, datoteka), index=False)
                print(f"Posodobljena datoteka: {datoteka} - Rojstni dan: {rojstni_dan}")
            else:
                print(f"Imena datoteke {datoteka} ni mogoče razbrati.")
        else:
            print(f"Datoteka {datoteka} ni CSV format.")