import pyAesCrypt
BufferSize=64*1024
file=input("Inserire il percorso del file:\n").strip()
password=input("Inserire la password:\n").strip()

a=input("Vuoi criptare[C] o  decriptare[D]?\n").upper()
if a=='C':
	fileaes=file+'.aes'
	pyAesCrypt.encryptFile(file, fileaes, password, BufferSize)
	print("File decriptato con successo")
elif a=='D':
	fileaes=file.replace('.aes','')
	pyAesCrypt.decryptFile(file, fileaes, password, BufferSize)
	print("File criptato con successo")
