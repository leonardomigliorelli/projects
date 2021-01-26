import json

fileName = 'file.json'

try:  # provo ad aprire il file
    file = open(fileName, 'r')
    myObj = json.loads(file.read())
except FileNotFoundError:  # se non riesco lo creo
    file = open(fileName, 'x')
    myObj = {}
except:
    print("ERRORE, FILE CORROTTO")

while True:
    nome = input("Inserire il nome nel valore (! per uscire): ")
    if(nome == '!'):
        break

    valore = input("Inserire il valore (! per uscire): ").strip().split(',')
    if(valore == '!'):
        break
    # ["io"],3,'hello', 3.4
    valore = [var.replace('"', "'") for var in valore]
    #valore = [var.strip('[]') for var in valore]

    # valore = [float(var) if (var.replace("'", "") == var) else var
    #          for var in valore]
    #valore = [var.replace("'", "") if (int(var) == var) else var for var in valore]
    
    # TODO: trasforma var in valore
    for var in valore:
        if(var.replace("'", "") == var):  # se stiamo parlando di numeri
            # se il valore non ha uno 0 dopo la virgola è un intero
            var = [int(var) if str(float(var)).split(
                ".")[1] == 0 else float(var)]
        else:  # se stiamo parlando di stringhe
            var = var.replace("'", "")

    myObj[nome] = valore
    with open(fileName, 'w') as outfile:
        json.dump(myObj, outfile, indent=2)
