# Класс для решения задачи алгоритмом Ахо-Карасика и создания бора
class AchoKarasik:
    # Подкласс узла бора
    class TrieNode:
        # Инициализация полей класса узла
        def __init__(self):
            self.patterns = []
            self.children = {}
            self.suffixLink = None

    # Инициализация полей класса решения задачи
    def __init__(self):
        self.inputText = str()
        self.patterns = list()
        self.textLength = int()
        self.answer = list()

    # Инициализация бора(дерево паттернов)
    # Возвращает корень дерева
    def initialize_trie(self):
        root = self.TrieNode()
        for index, path in enumerate(self.patterns):
            node = root
            for symbol in path:
                node = node.children.setdefault(symbol, self.TrieNode())
            node.patterns.append(index)
        return root

    # Создание автомата для алгоритма Ахо-Карасика
    def create_statemachine(self):
        root = self.initialize_trie()
        queue = []
        for node in root.children.values():
            queue.append(node)
            node.suffixLink = root

        while len(queue) > 0:
            currentNode = queue.pop(0)
            for sym, child in currentNode.children.items():
                queue.append(child)
                currentSuffixLink = currentNode.suffixLink
                while currentSuffixLink is not None and sym not in currentSuffixLink.children:
                    currentSuffixLink = currentSuffixLink.suffixLink
                child.suffixLink = currentSuffixLink.children[sym] if currentSuffixLink else root
                child.patterns += child.suffixLink.patterns

        return root

    # Метод для нахождения всех подстрок из набора паттернов в строке
    def find_patterns(self):
        root = self.create_statemachine()
        node = root
        for i in range(len(self.inputText)):
            while node is not None and self.inputText[i] not in node.children:
                node = node.suffixLink
            if node is None:
                node = root
                continue
            node = node.children[self.inputText[i]]
            for pattern in node.patterns:
                self.answer.append((i - len(self.patterns[pattern]) + 2, pattern + 1))
        self.answer = sorted(self.answer)

    # Метод для ввода данных
    def input_data(self):
        self.inputText = input()
        self.textLength = int(input())
        self.patterns = [input() for _ in range(self.textLength)]

    # Метод для корректного вывода ответа
    def print_answer(self):
        for item in self.answer:
            print(*item)

    # Метод для начала решения и запуска необходимых методов
    def start_algorithm(self):
        self.input_data()
        self.find_patterns()
        self.print_answer()


solver = AchoKarasik()
solver.start_algorithm()
