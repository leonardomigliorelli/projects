class InteresseComposto:
    def __init__(self, valore=0, aggiunta=0, interesse="", anni=""):
        self.addValore(valore)
        self.addAnnuale(aggiunta)
        self.addAnni(anni)
        self.addInteresse(interesse)
        self.valoreFuturo = 0
        self.interesseTotale = 1

    def Calcolo(self):  # valoreFuturo = iniziale * (1 + interesse) ^ anni
        if self.ValueControl():
            for i in range(self.anni):
                self.interesseTotale *= 1 + self.interesse / 100
            self.valoreFuturo = self.valore * self.interesseTotale
            return "{:.2f}".format(self.valoreFuturo)

    # Add Methods

    def addValore(self, valore):
        try:
            if (
                valore == "" or valore == None
            ):  # Se il valore è un qualche modo vuoto ci mettiamo il valore di default 0
                self.valore = 0
            else:
                if int(valore) >= 0:  # Se il valore è positivo lo impostiamo
                    self.valore = int(valore)
                else:
                    self.valore = "*"  # Se il valore non è positivo da errore
        except ValueError:  # Se int(valore) da errore allora siamo di fronte ad una stringa non vuota
            print("Errore - Inserire un valore numerico nel valore iniziale")
            self.valore = "*"

    def addAnnuale(self, aggiunta):
        try:
            if (
                aggiunta == "" or aggiunta == None
            ):  # Se il valore è un qualche modo vuoto ci mettiamo il valore di default 0
                self.aggiunta = 0
            else:
                if int(aggiunta) >= 0:  # Se il valore è positivo lo impostiamo
                    self.aggiunta = int(aggiunta)
                else:
                    self.aggiunta = "*"  # Se il valore non è positivo da errore
        except ValueError:  # Se int(valore) da errore allora siamo di fronte ad una stringa non vuota
            print("Errore - Inserire un valore numerico nell'aggiunta annuale")
            self.aggiunta = "*"

    def addAnni(self, anni):
        try:
            if (
                anni == "" or anni == None
            ):  # Se il valore è un qualche modo vuoto ci mettiamo il valore di default 0
                self.anni = 1
            else:
                if int(anni) > 0:  # Se il valore è positivo lo impostiamo
                    self.anni = int(anni)
                else:
                    self.anni = "*"  # Se il valore non è positivo da errore
        except ValueError:  # Se int(valore) da errore allora siamo di fronte ad una stringa non vuota
            print("Errore - Inserire un valore numerico in anni")
            self.anni = "*"

    def addInteresse(self, interesse):
        try:
            if (
                interesse == "" or interesse == None
            ):  # Se il valore è un qualche modo vuoto ci mettiamo il valore di default 0
                self.interesse = 0
            else:
                if int(interesse) >= 0:  # Se il valore è positivo lo impostiamo
                    self.interesse = int(interesse)
                else:
                    self.interesse = "*"  # Se il valore non è positivo da errore
        except ValueError:  # Se int(valore) da errore allora siamo di fronte ad una stringa non vuota
            print("Errore - Inserire un interesse numerico")
            self.interesse = "*"

    def ValueControl(self):
        if self.valore == "*":
            print("Il Valore iniziale deve essere un numero positivo")
        elif self.aggiunta == "*":
            print("L'aggiunta annuale deve essere un numero positivo")
        elif self.interesse == "*":
            print("L'interesse deve essere un numero positivo e non nullo")
        elif self.anni == "*":
            print("Gli anni devono essere numeri positivi")
        elif self.valore == 0 and self.aggiunta == 0:
            print(
                "Il Valore iniziale e L'aggiunta annuale non possono essere entrambi 0"
            )
        else:
            return True
        return False


i = InteresseComposto(
    valore=input("Inserisci il Valore Iniziale: ").replace(".", "").replace(",", ""),
    aggiunta=input("Inserisci L'aggiunta annuale: ").replace(".", "").replace(",", ""),
    interesse=input("Inserisci l'interesse: ").replace("%", ""),
    anni=input("Inserisci gli anni di durata: "),
)

print("valore finale: " + i.Calcolo())
