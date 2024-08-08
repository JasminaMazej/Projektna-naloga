import os
import pandas as pd
import re
import csv

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


#k podatkom želimo dodati še rojstni dan oseb, ki je razviden iz imena datoteke
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
            print(f'Obdelujem datoteko: {datoteka}')  
            match = re.match(r'famous_birthdays_(\D+)(\d+).csv', datoteka)
            if match:
                mesec_imenik, dan = match.groups()
                
                #pretvori mesec v številko
                mesec = meseci.get(mesec_imenik.lower(), 'Unknown')
                print(f'Mesec imenik: {mesec_imenik}, Mesec številka: {mesec}')  
                
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
                print(f'Posodobljena datoteka: {datoteka} - Rojstni dan: {rojstni_dan}')
            else:
                print(f'Imena datoteke {datoteka} ni mogoče razbrati.')
        else:
            print(f'Datoteka {datoteka} ni CSV format.')

def doloci_horoskop(dan, mesec):
    mesec = int(mesec)
    dan = int(dan)

    if (mesec == 3 and dan >= 21) or (mesec == 4 and dan <= 19):
        return 'Oven'
    elif (mesec == 4 and dan >= 20) or (mesec == 5 and dan <= 20):
        return 'Bik'
    elif (mesec == 5 and dan >= 21) or (mesec == 6 and dan <= 20):
        return 'Dvojčka'
    elif (mesec == 6 and dan >= 21) or (mesec == 7 and dan <= 22):
        return 'Rak'
    elif (mesec == 7 and dan >= 23) or (mesec == 8 and dan <= 22):
        return 'Lev'
    elif (mesec == 8 and dan >= 23) or (mesec == 9 and dan <= 22):
        return 'Devica'
    elif (mesec == 9 and dan >= 23) or (mesec == 10 and dan <= 22):
        return 'Tehtnica'
    elif (mesec == 10 and dan >= 23) or (mesec == 11 and dan <= 21):
        return 'Škorpijon'
    elif (mesec == 11 and dan >= 22) or (mesec == 12 and dan <= 21):
        return 'Strelec'
    elif (mesec == 12 and dan >= 22) or (mesec == 1 and dan <= 19):
        return 'Kozorog'
    elif (mesec == 1 and dan >= 20) or (mesec == 2 and dan <= 18):
        return 'Vodnar'
    elif (mesec == 2 and dan >= 19) or (mesec == 3 and dan <= 20):
        return 'Ribi'
    else:
        return 'Neznan'

def dodaj_horoskop_v_datoteko(datoteka):
    #branje obstoječe datoteke
    with open(datoteka, mode='r', newline='', encoding='utf-8') as dat:
        reader = csv.DictReader(dat)
        podatki = list(reader)
    
    #dodajanje stolpca 'Horoskop'
    for vrstica in podatki:
        rojstni_dan = vrstica['Rojstni dan']
        dan, mesec = rojstni_dan.split('-')
        horoskop = doloci_horoskop(dan, mesec)
        vrstica['Horoskop'] = horoskop
    
    #pisanje posodobljenih podatkov nazaj v datoteko
    with open(datoteka, mode='w', newline='', encoding='utf-8') as dat:
        fieldnames = ['Ime', 'Starost', 'Poklic', 'Rojstni dan', 'Horoskop']
        writer = csv.DictWriter(dat, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(podatki)
    
    print(f'Posodobljena datoteka: {datoteka}')