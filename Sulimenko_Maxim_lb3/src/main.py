import time, queue
inf = 99999999


# Класс, в котором содержится основная информация о графе:
# матрица смежностей, количество вершин, путь, его длина, и переменная
# отвечающая за то, был ли уже найден путь
class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.numberOfNodes = len(matrix)
        self.path = []
        self.pathLength = inf
        self.isPathFound = False


#  Метод для считывания данных из файла и записи их в виде графа(списка из списков)
def read_input_from_file(fileName):
    file = open(fileName, 'r')
    matrix = []

    for line in file.readlines():
        row = []
        for elem in line.strip().split():
            if elem == "inf" or elem == '-':
                row.append(inf)
            else:
                row.append(int(elem))
        matrix.append(row)

    graph = Graph(matrix)

    return graph


# Функция реализует рекурсивный поиск оптимального пути методом перебора с возвратом
# На вход подаётся элемент типа Graph и путь полученный на прошлом уровне рекурсии
def iterate_search(graph, currentPath):
    if currentPath[0] >= graph.pathLength:
        return

    if len(currentPath[1]) == graph.numberOfNodes:
        if (graph.matrix[currentPath[1][-1]][graph.path[0]] != inf) and \
                ((currentPath[0] + graph.matrix[currentPath[1][-1]][graph.path[0]]) < graph.pathLength):
            graph.path.clear()

            for element in currentPath[1]:
                graph.path.append(element)
            graph.path.append(graph.path[0])
            graph.pathLength = currentPath[0] + graph.matrix[currentPath[1][-1]][graph.path[0]]
            return

    for count, element in enumerate(graph.matrix[currentPath[1][-1]]):
        if element != inf and count not in currentPath[1]:
            if currentPath[0] + element >= graph.pathLength:
                continue
            if len(currentPath) == graph.numberOfNodes - 1 and currentPath[0] + \
                    element + graph.matrix[count][graph.path[0]] >= graph.pathLength:
                continue

            currentPath[0] += element
            currentPath[1].append(count)

            iterate_search(graph, currentPath)
            
            currentPath[1].pop()
            currentPath[0] -= element
    return


# Метод для роверки существования и вычисления нижней границы гамильтонова цикла при помощи жадного алгоритма
def calculate_lower_bound(graph, path):
    graphQueue = queue.PriorityQueue()

    for node in range(graph.numberOfNodes):
        if graph.matrix[path[1][-1]][node] != inf:
            graphQueue.put((graph.matrix[path[1][-1]][node], node))

    while not graphQueue.empty():
        currentNode = graphQueue.get()[1]
        if currentNode != inf and currentNode not in path[1]:
            path[1].append(currentNode)
            path[0] += graph.matrix[path[1][-2]][currentNode]

            if len(path[1]) == graph.numberOfNodes:
                if graph.matrix[currentNode][path[1][0]] != inf:
                    graph.path = path[1]
                    graph.path.append(path[1][0])
                    graph.pathLength = path[0] + graph.matrix[currentNode][path[1][0]]
                    graph.isPathFound = True
                    break
                else:
                    path[1].pop()
                    path[0] -= graph.matrix[path[1][-1]][currentNode]
                    continue

            calculate_lower_bound(graph, path)

            if graph.isPathFound:
                break

            path[1].pop()
            path[0] -= graph.matrix[path[1][-1]][currentNode]
    return


# Метод, который вызывает необходимые функции и решает задачу о нахождении
# кратчайшего пути, а после этого выводит ответ в консоль.
# Помимо этого, происходит замер времени работы алгоритма
def start_algorithm(fileName):
    startTime = time.time()

    graph = read_input_from_file(fileName)
    path = [0, [0]]
    calculate_lower_bound(graph, path)

    if not graph.isPathFound:
        print("Гамильтонов путь не найден")
        return

    path = [0, [0]]
    iterate_search(graph, path)

    for i in range(len(graph.path)):
        graph.path[i] += 1

    endTime = time.time()

    print(graph.path, graph.pathLength, endTime - startTime)


start_algorithm("test.txt")
