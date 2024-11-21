from git_utils import get_changed_files # импорт в mermaid_generator.py
def generate_mermaid_code(graph, repo_path):
    """Генерирует Mermaid код с информацией о файлах в узлах."""
    mermaid_code = "graph LR\n"
    for commit_hash, parent_commits in graph.items():
        changed_files = get_changed_files(repo_path, commit_hash)  # Получаем файлы для каждого узла
        node_label = f"{commit_hash}\nFiles: {', '.join(changed_files)}"
        mermaid_code += f'    "{node_label}" --> "{",".join(parent_commits)}"\n'
    return mermaid_code