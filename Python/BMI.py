peso = float(input("Inserisci il peso in kg: ").strip().replace(',', '.'))
altezza = float(input("Inserisci l'altezza in cm: ").strip().replace(',', '.'))
dictionary = {"Sottopeso severo": 16.5,
              "Sottopeso": 18.4,
              "Normale": 24.9,
              "Sovrappeso": 30,
              "Obesità primo grado": 34.9,
              "Obesità secondo grado": 40}

BMI = peso / (altezza / 50)

if BMI < dictionary["Sottopeso severo"]:
    condizione = "Sottopeso severo"
elif BMI < dictionary["Sottopeso"]:
    condizione = "Sottopeso"
elif BMI < dictionary["Normale"]:
    condizione = "Normale"
elif BMI < dictionary["Obesità primo grado"]:
    condizione = "Obesità primo grado"
elif BMI < dictionary["Obesità secondo grado"]:
    condizione = "Obesità secondo grado"
elif BMI > dictionary["Obesità secondo grado"]:
    condizione = "Obesità terzo grado"
else:
    print("ERRORE")

print("\nAltezza: {:.2f} cm\nPeso: {:.2f} kg\n\nBMI: {:.2f}\nCondizione: {}\n".format(altezza, peso, BMI, condizione))
