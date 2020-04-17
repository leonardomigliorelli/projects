import pyshorteners

link=input('Inserire il link da accorciare: ')

s=pyshorteners.Shortener()
print('Il link è:', s.tinyurl.short(link))