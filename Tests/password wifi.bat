@echo off
title Password Wifi
goto 0
:1
netsh wlan show profiles
echo [scegli una wifi e ti diro la sua password]
set /p u=
netsh wlan show profiles "%u%" key=clear
goto 2
:0
echo Inserisci la password
set /p r=
if %r%==l30 goto 1
:2
pause