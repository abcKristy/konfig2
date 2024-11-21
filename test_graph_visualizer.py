import unittest
import main
import git_utils
import dependency_graph
import mermaid_generator

class TestGraphVisualizer(unittest.TestCase):

    def test_get_commits_with_file(self):
        repository_path = "path/to/repository"
        target_file = "file.txt"
        commits = git_utils.get_commits_with_file(repository_path, target_file)
        self.assertIsInstance(commits, list)

    def test_get_commit_history(self):
        repository_path = "path/to/repository"
        commit_history = git_utils.get_commit_history(repository_path)
        self.assertIsInstance(commit_history, list)

    def test_get_changed_files(self):
        repository_path = "path/to/repository"
        commit_hash = "commit_hash"
        changed_files = git_utils.get_changed_files(repository_path, commit_hash)
        self.assertIsInstance(changed_files, list)

    def test_build_dependency_graph(self):
        repository_path = "path/to/repository"
        commits = ["commit1", "commit2", "commit3"]
        graph = dependency_graph.build_dependency_graph(repository_path, commits)
        self.assertIsInstance(graph, dict)

    def test_generate_mermaid_code(self):
        graph = {"commit1": {"commit2"}, "commit2": {"commit3"}}
        mermaid_code = mermaid_generator.generate_mermaid_code(graph)
        self.assertIn("graph LR", mermaid_code)

    def test_visualize_dependencies(self):
        main.visualize_dependencies()
        # Проверка на наличие выходного файла и его содержимого
        # ...

if __name__ == "__main__":
    unittest.main()