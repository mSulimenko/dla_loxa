# Класс для решения задачи алгоритмом Ахо-Карасика и создания бора
class AchoKarasik:
    # Подкласс узла бора
    class TrieNode:
        # Инициализация полей класса узла
        def __init__(self):
            self.children = {}
            self.listOfPatterns = []
            self.suffixLink = None

    # Инициализация полей класса решения задачи
    def __init__(self):
        self.inputText = str()
        self.listOfPatterns = list()
        self.pattern = str()
        self.mask = str()
        self.answer = list()

    # Инициализация бора(дерево паттернов)
    # Возвращает корень дерева
    def initialize_trie(self):
        root = self.TrieNode()
        for index, path in enumerate(self.listOfPatterns):
            node = root
            for symbol in path:
                node = node.children.setdefault(symbol, self.TrieNode())
            node.listOfPatterns.append(index)
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
            for symbol, child in currentNode.children.items():
                queue.append(child)
                currentSuffixLink = currentNode.suffixLink
                while currentSuffixLink is not None and symbol not in currentSuffixLink.children:
                    currentSuffixLink = currentSuffixLink.suffixLink
                child.suffixLink = currentSuffixLink.children[symbol] if currentSuffixLink else root
                child.listOfPatterns += child.suffixLink.listOfPatterns
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
            for pattern in node.listOfPatterns:
                self.answer.append((i - len(self.listOfPatterns[pattern]) + 1, pattern))
        self.answer = sorted(self.answer)

    # Создает части - паттерны - из строки с джокером
    # и их начальные индексы в строке с джокером
    def create_parts_and_indices(self):
        parts = list(filter(bool, self.pattern.split(self.mask)))
        indices = list()
        isMask = True
        for index, symbol in enumerate(self.pattern):
            if symbol == self.mask:
                isMask = True
                continue
            if isMask:
                indices.append(index)
                isMask = False
        return parts, indices

    # Метод для нахождения всех подстрок из набора паттернов в строке
    # С джокером
    def find_patterns_with_mask(self):
        parts, indices = self.create_parts_and_indices()
        self.listOfPatterns = parts
        self.find_patterns()

        text = [0] * len(self.inputText)
        for ind, pInd in self.answer:
            index = ind - indices[pInd]
            if 0 <= index < len(text):
                text[index] += 1

        result = []
        for i in range(len(text) - len(self.pattern) + 1):
            if text[i] == len(self.listOfPatterns):
                result.append(i + 1)
        self.answer = result

    # Метод для ввода данных
    def input_data(self):
        self.inputText = input()
        self.pattern = input()
        self.mask = input()

    # Метод для корректного вывода ответа
    def print_answer(self):
        print(*self.answer, sep="\n")

    # Метод для начала решения и запуска необходимых методов
    def start_algorithm(self):
        self.input_data()
        self.find_patterns_with_mask()
        self.print_answer()


solver = AchoKarasik()
solver.start_algorithm()
