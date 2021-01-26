import json

fileName = 'file.json'
corrotto = False

try:  # provo ad aprire il file
    file = open(fileName, 'r')
    myObj = json.loads(file.read())
except FileNotFoundError:  # se non riesco lo creo
    file = open(fileName, 'x')
    myObj = {}
except:
    print("ERRORE, FILE CORROTTO")
    corrotto = True

while not corrotto:
    nome = input("Inserire il nome nel valore (! per uscire): ")
    if(nome == '!'):
        break

    valore = input("Inserire il valore (! per uscire): ").strip().split(',')
    if(valore == '!'):
        break
    # ["io"],3,'hello', 3.4
    valore = [var.replace('"', "'") for var in valore]
    valore = [var.strip('[]') for var in valore]

    # TODO: trasforma var in valore
    for i in range(len(valore)):
        if(valore[i].replace("'", "") == valore[i]):  # se stiamo parlando di numeri
            # se il valore non ha uno 0 dopo la virgola è un intero
            valore[i] = (int(valore[i]) if (
                str(float(valore[i])).split(".")[1] == '0') else float(valore[i]))
        else:  # se stiamo parlando di stringhe
            valore[i] = valore[i].replace("'", "")

    myObj[nome] = valore
    with open(fileName, 'w') as outfile:
        json.dump(myObj, outfile, indent=2)
