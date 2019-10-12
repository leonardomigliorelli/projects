@echo off
title Copia file
:inizio
cls
set /p percorso=Inserisci il percorso del file da copiare 
set /p percorsodest=Inserisci il percorso dove copiare il file 
set /a massimo=-1
set /p massimo=Inserisci il numero massimo di file da copiare (lasciarlo vuoto equivale a un tempo infinito) 
set i=0
:loop
set /a i+=1
echo Copio file n.%i%
copy "%percorso%" "%percorsodest%\%i%">nul
rem exit condition
if %massimo% gtr 0 set /a massimo-=1
if %massimo% equ 0 goto exit
goto loop
:loop
goto loop
:exit
echo Finito
pause
goto inizio