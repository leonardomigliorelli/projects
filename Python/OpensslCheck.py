from hashlib import *

possibilities = {'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512'}

hash = None
file = str(open(input("Inserire il percorso del file: ").strip(), 'rb')).encode('utf-8')
knowHash = input("Inserire il codice da verificare (vuoto se non richiesto): ").strip()
tipo = input("Inserire il tipo di hash: ").replace(' ', '').lower()

if tipo == 'md5':
	hash = md5(file).hexdigest()
elif tipo == 'sha1':
	hash = sha1(file).hexdigest()
elif tipo == 'sha224':
	hash = sha224(file).hexdigest()
elif tipo == 'sha256':
	hash = sha256(file).hexdigest()
elif tipo == 'sha384':
	hash = sha384(file).hexdigest()
elif tipo == 'sha512':
	hash = sha512(file).hexdigest()
elif tipo == 'sha3_224':
	hash = sha3_224(file).hexdigest()
elif tipo == 'sha3_256':
	hash = sha3_256(file).hexdigest()
elif tipo == 'sha3_384':
	hash = sha3_384(file).hexdigest()
elif tipo == 'sha3_512':
	hash = sha3_512(file).hexdigest()
else:
	print("Tipo di hash non riconosciuto: {} \nAssicurati che si trovi in {}".format(tipo, possibilities))

if knowHash == hash:
	print("Il documento è sicuro")
elif knowHash == '':
	print("L'hash del documento è", hash)
else:
	print("Il valore inserito\n {}\nNon corrisponde con l'hash\n {}".format(knowHash, hash))
