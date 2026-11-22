@echo off
::echo Начинаем отсчет:
::for /L %%i in (1, 1, 5) do (z
 ::   echo Номер: %%i )
    echo make folder
    for %%d in ( Documentt Videoss Musicc Imagess ) do ( echo making folders %%d
    md  C:\"%%d" )
    echo all done
    echo Список всех текстовых файлов в этой директории:
    for /R %%f in (*.txt) do ( echo Найдено: %%d
     )