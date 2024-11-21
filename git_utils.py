import subprocess

def get_commits_with_file(repo_path, file_path):
    """
    Возвращает список коммитов, изменивших указанный файл.
    """
    process = subprocess.run(
        ["git", "-C", repo_path, "log", "--pretty=format:%H", "--follow", file_path],
        capture_output=True,
        text=True,
    )
    commits = process.stdout.splitlines()
    #print(f"Список коммитов, изменивших {file_path}: {commits}")  # Для отладки
    return commits

def get_changed_files(repo_path, commit_hash):
    """
    Возвращает список файлов, измененных в указанном коммите.
    """
    process = subprocess.run(
        ["git", "-C", repo_path, "show", "--pretty=format:", "--name-only", commit_hash],
        capture_output=True,
        text=True,
    )
    changed_files = process.stdout.splitlines()
    #print(f"Измененные файлы в коммите {commit_hash}: {changed_files}")  # Для отладки
    return changed_files

def get_commit_history(repo_path):
    """Возвращает историю коммитов"""
    process = subprocess.run(["git", "-C", repo_path, "log", "--pretty=format:%H %P"], capture_output=True, text=True)
    return process.stdout.splitlines()