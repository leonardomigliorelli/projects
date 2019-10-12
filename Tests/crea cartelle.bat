@echo off
title Crea cartelle
:inizio
cls
set /p percorso=Inserisci un percorso nel quale creare le cartelle 
set /p testo=Inserisci una frase da includere nel nome 
set /a massimo=-1
set /p massimo=Inserisci il numero massimo di cartelle da creare (lasciarlo vuoto equivale a un tempo infinito) 
set /a i=0
:loop
set /a i+=1
set file=%testo%%i%
echo Creazione cartella: %file%
md "%percorso%\%file%"
rem exit condition
if %massimo% gtr 0 set /a massimo-=1
if %massimo% equ 0 goto exit
goto loop
:exit