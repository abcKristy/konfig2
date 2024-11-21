import csv

def read_config():
    """Считывает конфигурацию из файла config.csv."""
    try:
        with open("config.csv", "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return next(reader)
    except StopIteration:
        print("Ошибка: config.csv пуст или не содержит данных.")
        return None
    except FileNotFoundError:
        print("Ошибка: файл config.csv не найден.")
        return None
