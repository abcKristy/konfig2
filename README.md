# konfig2
# Задание №2
Разработать инструмент командной строки для визуализации графа
зависимостей, включая транзитивные зависимости. Сторонние средства для
получения зависимостей использовать нельзя.

Зависимости определяются для git-репозитория. Для описания графа
зависимостей используется представление Mermaid. Визуализатор должен
выводить результат на экран в виде кода.

Построить граф зависимостей для коммитов, в узлах которого находятся
списки файлов и папок. Граф необходимо строить только для тех коммитов, где
фигурирует файл с заданным хеш-значением.

Конфигурационный файл имеет формат csv и содержит:

• Путь к программе для визуализации графов.
• Путь к анализируемому репозиторию.
• Путь к файлу-результату в виде кода.
• Файл с заданным хеш-значением в репозитории.

Все функции визуализатора зависимостей должны быть покрыты тестами.