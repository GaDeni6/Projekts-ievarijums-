receptes_numurs=input("Ievadiet receptes numuru: \n1) 1 kg abolu = 300 gr. cukura\n2) 1 kg abolu = 500 gr. cukura\n ")
cukura_cena=float(input("Ievadi cukura cenu: "))
aboli_kg = float(input("Ievadi, cik abolu tev ir (kg): "))
if receptes_numurs == "1":
    izmaksas = cukura_cena*aboli_kg*0.3
else:
    izmaksas = cukura_cena*aboli_kg*0.5
print(f"Par cukuru tu samaksasi {izmaksas} eiro")







