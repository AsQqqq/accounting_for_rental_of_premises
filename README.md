# Учетное ПО для Аренды Помещений "Муха"
 
## Введение

Данное приложение, разработанное на языке Python, предназначено для учета аренды помещений. Проект был выполнен в качестве курсовой работы, и последнюю актуальную версию программы всегда можно найти в разделе "релизы".

# Установка и компиляция кода

Перед запуском программы необходимо установить необходимые зависимости, приведенные в файле req.txt. Это можно сделать, используя следующую команду:

```pip install -r req.txt```

## Конвертация из .ui в .py

Для преобразования файлов интерфейса из формата Qt Designer (.ui) в Python-код (.py), используйте следующую команду:

```
pyuic5.exe -x .\designer\login.ui -o .\designe\login.py; 
pyuic5.exe -x .\designer\main.ui -o .\designe\main.py; 
pyuic5.exe -x .\designer\main2.ui -o .\designe\main2.py
```

## Конвертация из .py в .exe

Для создания исполняемого файла (.exe) из кода Python, используйте команду pyinstaller, как показано ниже:

```
pyinstaller --noconfirm --onefile --windowed --add-data "database.py;." --add-data "local.sqlite;." --add-data "designe/login.py;." --add-data "designe/main.py;." --add-data "designe/main2.py;." --add-data "source_rc.py;." "app.py"
```

После успешной компиляции, вы найдете сгенерированный .exe файл в созданной папке dist, который теперь можно запускать для использования программы.