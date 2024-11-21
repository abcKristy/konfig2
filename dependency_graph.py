# dependency_graph.py
from collections import defaultdict
import subprocess


def build_dependency_graph(repository_path, commits, target_hash=None):
    """Строит граф зависимостей коммитов."""
    graph = defaultdict(set)
    try:
        process = subprocess.run(
            ["git", "-C", repository_path, "log", "--pretty=format:%H %P"],
            capture_output=True,
            text=True,
            check=True,
        )
        commit_history = process.stdout.splitlines()
    except FileNotFoundError:
        print("Git не найден. Убедитесь, что git установлен и доступен в системе.")
        return {}

    for line in commit_history:
        parts = line.split()
        if len(parts) == 2:  # Проверка на наличие двух элементов
            commit, parents = parts
            if commit in commits:
                for parent in parents.split():
                    graph[parent].add(commit)
        """elif len(parts) == 1:  # Обработка случая с одним элементом (root commit)
            print(f"Коммит {parts[0]} не имеет родителей.")  # Информация для отладки
        else:
            print(f"Некорректная строка в истории коммитов: {line}")
"""
    return graph

