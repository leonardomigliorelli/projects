@echo off
title Crea file
:inizio
cls
set /p percorso=Inserisci un percorso nel quale creare i file 
set /p testo=Inserisci un'eventuale frase da includere nel nome 
set contenuto=type nul
set /p contenuto=Inserisci un'eventuale contenuto 
if not "%contenuto%"=="type nul" set contenuto=echo %contenuto%
set /p estensione=Inserisci un'eventuale estensione .
set /a massimo=-1
set /p massimo=Inserisci il numero massimo di file da creare (lasciarlo vuoto equivale a un tempo infinito) 
set i=0
:loop
set /a i+=1
set file=%testo%%i%.%estensione%
echo Creazione file: %file%
%contenuto%>"%percorso%\%file%"
rem exit condition
if %massimo% gtr 0 set /a massimo-=1
if %massimo% equ 0 goto exit
goto loop
:exit
echo Finito
pause
goto inizio