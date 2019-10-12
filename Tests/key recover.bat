echo off
title key recover
netsh wlan show profiles
echo Scegli una wifi e ti diro la sua password
set /p u=
netsh wlan show profiles "%u%" key=clear
echo inserisci password
pause