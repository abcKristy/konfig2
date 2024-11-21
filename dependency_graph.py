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
        try:
            commit, parents = line.split()
            if commit in commits:
                for parent in parents.split():
                    graph[parent].add(commit)
        except ValueError as e:
            print(f"Ошибка при разборе строки: {line}, ошибка: {e}")
    return graph

