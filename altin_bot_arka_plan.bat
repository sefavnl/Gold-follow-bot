@echo off
title Altin Bot Arka Plan

echo Altin takip botu arka planda baslatiliyor...
echo Bot durdurulmak istendiginde taskkill komutu kullanin

start /min pythonw altin_takip_bot.py

echo Bot arka planda calisiyor.
echo Durdurmak icin: taskkill /f /im pythonw.exe
echo.
pause 