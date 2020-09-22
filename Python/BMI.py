dictionary = {"Sottopeso severo": 16.5,
              "Sottopeso": 18.4,
              "Normale": 24.9,
              "Sovrappeso": 30,
              "Obesità primo grado": 34.9,
              "Obesità secondo grado": 40}

class Persona:
    def __init__(self, peso, altezza):
        self.peso = peso
        self.altezza = altezza
        self.BMI = self.peso / (self.altezza / 50)

    def BMICalc(self):
        if all([self.peso is not None, self.altezza is not None]):
            if self.BMI < dictionary["Sottopeso severo"]:
                risultato = "Sottopeso severo"
            elif self.BMI < dictionary["Sottopeso"]:
                risultato = "Sottopeso"
            elif self.BMI < dictionary["Normale"]:
                risultato = "Normale"
            elif self.BMI < dictionary["Obesità primo grado"]:
                risultato = "Obesità primo grado"
            elif self.BMI < dictionary["Obesità secondo grado"]:
                risultato = "Obesità secondo grado"
            elif self.BMI > dictionary["Obesità secondo grado"]:
                risultato = "Obesità terzo grado"
            else:
                risultato = "ERRORE nel calcolo"
                print(risultato)

            if risultato != "ERRORE nel calcolo":
                print("\nAltezza: {:.2f} cm\nPeso: {:.2f} kg\n\nBMI: {:.2f}\nCondizione: {}".format(self.altezza,
                                                                                                    self.peso,
                                                                                                    self.BMI,
                                                                                                    risultato))
                return self.altezza, self.peso, self.BMI, risultato
        else:
            print("Dati mancanti")


peso = float(input("Inserisci il peso in kg: ").strip().replace(',', '.'))
altezza = float(input("Inserisci l'altezza in cm: ").strip().replace(',', '.'))

utente = Persona(peso, altezza)

BMICalc = utente.BMICalc()
