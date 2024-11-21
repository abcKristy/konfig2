import csv

def read_config():
    """
    Считывает конфигурацию из файла config.csv.
    """
    with open("config.csv", "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        config_data = next(reader)
    return config_data