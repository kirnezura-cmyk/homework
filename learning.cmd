@echo off
title Мой первый скрипт-помощник
cls

echo === Шаг 1: Создаем папку для бэкапа ===
md C:\BackupFolder

echo === Шаг 2: Копируем важный файл ===
copy "C:\Users\Public\Documents\*.txt" "C:\BackupFolder\"

echo === Шаг 3: Очистка временных файлов Windows ===
del /q /s %temp%\*

echo Все задачи успешно выполнены!
pause