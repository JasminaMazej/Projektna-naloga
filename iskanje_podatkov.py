import pandas as pd
import os

def zdruzi_csv(mapa_za_csv, izhodna_datoteka):
    #seznam vseh CSV datotek v mapi
    vse_datoteke = [f for f in os.listdir(mapa_za_csv) if f.endswith('.csv')]
    
    #seznam DataFrame-ov za združevanje
    vsi_df = []
    
    for datoteka in vse_datoteke:
        pot_do_datoteke = os.path.join(mapa_za_csv, datoteka)
        df = pd.read_csv(pot_do_datoteke)
        vsi_df.append(df)
    
    #združi vse DataFrame-e v enega
    zdruzen_df = pd.concat(vsi_df, ignore_index=True)
    
    #shrani združen DataFrame v novo CSV datoteko
    zdruzen_df.to_csv(izhodna_datoteka, index=False)
    print(f'Datoteke so združene v {izhodna_datoteka}.')

