@echo off
title Bot Durum Kontrolu
color 0B

echo.
echo ========================================
echo    BOT DURUM KONTROLU
echo ========================================
echo.

echo Python surecleri kontrol ediliyor...
tasklist /fi "imagename eq python.exe" /fo table
echo.
echo Pythonw surecleri kontrol ediliyor...
tasklist /fi "imagename eq pythonw.exe" /fo table
echo.

echo Bot calisiyor mu kontrol edildi.
echo.
pause 