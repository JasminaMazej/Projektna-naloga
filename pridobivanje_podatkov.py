from funkcije_zajem import *

for day in range(1, 32):
    #pridobimo podatke za julij in avgust
    podatki_jul = podatki_julij(day)
    podatki_avg = podatki_avgust(day)

    izlusceni_jul = izlusci_podatke(podatki_jul)
    izlusceni_avg = izlusci_podatke(podatki_avg)

    shrani_v_csv(izlusceni_jul, f'famous_birthdays_july{day}.csv', 'podatki')
    shrani_v_csv(izlusceni_avg, f'famous_birthdays_august{day}.csv', 'podatki')
    

    #pridobimo podatke se za ostale mesece z 31 dnevi
    pod_jan = podatki_po_mesecih('january', day)
    pod_mar = podatki_po_mesecih('march', day)
    pod_maj = podatki_po_mesecih('may', day)
    pod_okt = podatki_po_mesecih('october', day)
    pod_dec = podatki_po_mesecih('december', day)

    i_jan = izlusci_podatke(pod_jan)
    i_mar = izlusci_podatke(pod_mar)
    i_maj = izlusci_podatke(pod_maj)
    i_okt = izlusci_podatke(pod_okt)
    i_dec = izlusci_podatke(pod_dec)

    shrani_v_csv(i_jan, f'famous_birthdays_january{day}.csv', 'podatki')
    shrani_v_csv(i_mar, f'famous_birthdays_march{day}.csv', 'podatki')
    shrani_v_csv(i_maj, f'famous_birthdays_may{day}.csv', 'podatki')
    shrani_v_csv(i_okt, f'famous_birthdays_october{day}.csv', 'podatki')
    shrani_v_csv(i_dec, f'famous_birthdays_december{day}.csv', 'podatki')


#pridobimo podatke za februar
for day in range(7, 30):
    pod_feb = podatki_februar(day)
    izlusceni_feb = izlusci_podatke(pod_feb)
    shrani_v_csv(izlusceni_feb, f'famous_birthdays_february{day}.csv', 'podatki')

#pridobimo podatke za mesece, ki imajo po 30 dni
for day in range(1, 31):
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
