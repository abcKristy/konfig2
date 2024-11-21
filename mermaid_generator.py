def generate_mermaid_code(graph):
    """
    Генерирует Mermaid код для графа зависимостей.
    """
    print(f"Переданный граф в generate_mermaid_code: {graph}")  # Для отладки
    mermaid_code = "graph LR\n"
    for node, edges in graph.items():
        mermaid_code += f"    {node}[" + node + "] "
        for edge in edges:
            mermaid_code += f"--> {edge}[" + edge + "] "
        mermaid_code += "\n"
    return mermaid_code