# git_utils.py
import subprocess

def get_commits_with_file(repo_path, file_path, commit_hash=None):
    """Возвращает список хешей коммитов, которые изменили указанный файл."""
    command = ["git", "-C", repo_path, "log", "--pretty=format:%H", "--follow", file_path]
    if commit_hash:
        command.append(f"--since={commit_hash}")
    try:
        process = subprocess.run(command, capture_output=True, text=True, check=True)
        commits = [commit.strip() for commit in process.stdout.splitlines() if commit.strip()]
        return commits
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды git: {e}")
        return []
    except FileNotFoundError:
        print("Git не найден. Убедитесь, что git установлен и доступен в системе.")
        return []

def get_changed_files(repo_path, commit_hash):
    """Возвращает список файлов, измененных в указанном коммите."""
    try:
        process = subprocess.run(
            ["git", "-C", repo_path, "show", "--pretty=format:", "--name-only", commit_hash],
            capture_output=True,
            text=True,
            check=True,
        )
        return [f.strip() for f in process.stdout.splitlines() if f.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды git: {e}")
        return []
    except FileNotFoundError:
        print("Git не найден. Убедитесь, что git установлен и доступен в системе.")
        return []
