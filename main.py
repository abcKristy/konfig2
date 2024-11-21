# main.py
import config
import git_utils
import dependency_graph
import mermaid_generator


def visualize_dependencies(config_data):

    """Визуализирует граф зависимостей."""
    repo_path = config_data["repository_path"]
    target_file = config_data["target_file"]
    target_hash = config_data.get("target_hash")

    commits = git_utils.get_commits_with_file(repo_path, target_file, target_hash)
    if not commits:
        print(f"Нет коммитов, изменяющих файл {target_file} после {target_hash}.")
        return

    graph = dependency_graph.build_dependency_graph(repo_path, commits, target_hash)
    if not graph:
        return

    mermaid_code = mermaid_generator.generate_mermaid_code(graph, repo_path)
    with open("codeMer.txt", "w", encoding='utf-8') as file:
        file.write(mermaid_code)
    print("Mermaid код сохранен в codeMer.txt")


if __name__ == "__main__":
    config_data = config.read_config()
    if config_data:
        visualize_dependencies(config_data)