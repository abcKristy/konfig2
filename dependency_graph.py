from collections import defaultdict
import subprocess

def build_dependency_graph(repository_path, commits):
    """
    Строит граф зависимостей коммитов.
    """
    graph = defaultdict(set)
    # Используем git для получения истории коммитов и их родителей
    process = subprocess.run(
        ["git", "-C", repository_path, "log", "--pretty=format:%H %P"],
        capture_output=True,
        text=True,
    )
    commit_history = process.stdout.splitlines()

    for line in commit_history:
        line = line.strip()  # Удаляем пробельные символы
        if line and len(line.split()) >= 2:  # Проверка наличия строки и количества элементов
            try:
                commit, parents = line.split(maxsplit=1)  # maxsplit=1 - разделяет строку только по первому пробелу
            except ValueError:
                print(f"Ошибка разбиения строки: {line}")  # Логируем ошибку для отладки
                continue  # Пропускаем эту строку
            if commit in commits:
                for parent in parents.split():
                    graph[parent].add(commit)
        else:
            print(f"Пустая или некорректная строка: {line}")  # Логируем ошибку для отладки

    print(f"Граф зависимостей: {graph}")  # Для отладки
    return graph