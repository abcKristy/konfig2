import config
import git_utils
import dependency_graph
import mermaid_generator

def visualize_dependencies():
    config_data = config.read_config()
    target_file = config_data["target_file"]
    commits = git_utils.get_commits_with_file(config_data["repository_path"], target_file)
    graph = dependency_graph.build_dependency_graph(config_data["repository_path"], commits)
    mermaid_code = mermaid_generator.generate_mermaid_code(graph)

    with open("codeMer.txt", "w", encoding='utf-8') as f:
        f.write(mermaid_code)

    print(f"Mermaid код сохранен в файл codeMer.txt")

    print(mermaid_code) # Выводим Mermaid код на экран

if __name__ == "__main__":
    visualize_dependencies()