# Задание №2
Разработать инструмент командной строки для визуализации графа
зависимостей, включая транзитивные зависимости. Сторонние средства для
получения зависимостей использовать нельзя.

Зависимости определяются для git-репозитория. Для описания графа
зависимостей используется представление Mermaid. Визуализатор должен
выводить результат на экран в виде кода.

Построить граф зависимостей для коммитов, в узлах которого находятся
списки файлов и папок. Граф необходимо строить только для тех коммитов, где
фигурирует файл с заданным хеш-значением.

Конфигурационный файл имеет формат csv и содержит:

• Путь к программе для визуализации графов.

• Путь к анализируемому репозиторию.

• Путь к файлу-результату в виде кода.

Все функции визуализатора зависимостей должны быть покрыты тестами.

Консольное приложение, позволяющее визуализировать транзитивные зависимости пакетов Maven в виде графа.

# 1. Клонирование репозитория

Клонируйте репозиторий с исходным кодом и тестами:

```bash
git clone <URL репозитория>
cd <директория проекта>
```

# 2. Виртуальное окружение

```shell
python -m venv venv
venv/Scripts/activate
```

# 3. Установка зависимостей

```shell
pip install -r requirements.txt
```


# 4. Запуск программы

```shell
py main.py
```

# 5. Тестирование

Для запуска тестирования необходимо запустить следующий скрипт:
```shell
pytest -v
```

Просмотр результатов покрытия:

# отчет о покрытии

Конфигурационный файл

Пример конфигурационного файла:

```shell
tool_path,repository_path,output_file,target_file,target_hash
,"C:\Users\lolut\Desktop\вуз\конфиг\hm1","codeMer.txt","final_dz1\main.py","e40e60dd5f9fa3e6921bc42dbf8c7c1d04c96afa"
```
Где:

target_file - Путь к программе в файле

repository_path - Путь к репозиторию программы

output_file — файл в котором для удобства сохранияетя сод графа

target_hash - это хеш конкретного коммита в вашем Git-репозитории

Результат покрытия тестами

![image](https://github.com/user-attachments/assets/af0ce6a6-4423-467a-99eb-37aaeeea801c)
