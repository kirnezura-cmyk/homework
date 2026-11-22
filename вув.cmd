echo Начинаем отсчет:
for /L %%i in (1, 1, 5) do (
    echo Номер: %%i
)

echo Создаем папки для проекта...

for %%d in (Images, Music, Videos, Documents) do (
    echo Создаю папку: %%d
    mkdir "%%d"
)

echo Все папки успешно созданы!


echo Список всех текстовых файлов в этой директории:

for /R %%f in (*.txt) do (
    echo Найдено: %%f
)