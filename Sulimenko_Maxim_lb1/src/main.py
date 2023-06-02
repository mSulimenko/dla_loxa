# Класс маленьких квадртатов, из которых будет заполняться весь стол
class Square:
    # Метод для инициализзации переменных для размера и координат квадрата
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size


# Метод, возвращающий true, если данное место занято, и false в противном случае
def is_taken(table, x, y):
    for square in table:
        if square.x <= x < square.x + square.size and square.y <= y < square.y + square.size:
            return True
    return False


# Основная рекурсивная функция, последовательно пытающаяся расставить квардаты с помощью метода бектрекинга
def Backtracking(table, currentVolume, squareCount, minX, minY):
    global bestScore
    for x in range(minX, n):
        for y in range(minY, n):
            if not is_taken(table, x, y):
                right = min(n - x, n - y)
                for square in table:
                    if square.x + square.size > x and square.y > y:
                        right = min(right, square.y - y)

                for size in range(right, 0, -1):
                    square = Square(x, y, size)
                    currentTable = table.copy()
                    currentTable.append(square)
                    if currentVolume + square.size * square.size == n * n:
                        if squareCount + 1 < bestScore:
                            bestScore = squareCount + 1
                            bestTable[:] = currentTable.copy()
                    else:
                        if squareCount + 1 < bestScore:
                            Backtracking(currentTable, currentVolume + square.size * square.size, squareCount + 1, x,
                                         y + size)
                        else:
                            return
                return
        minY = int(n // 2)


n = int(input())
bestScore = 2 * n + 1
bestTable = []
sizeOfTable = 1

for i in range(2, n):
    if n % i == 0:
        sizeOfTable = i
n = n // sizeOfTable

startTable = [Square(0, 0, int((n + 1) // 2)), Square(0, int((n + 1) // 2), int(n // 2)),
              Square(int((n + 1) // 2), 0, int(n // 2))]

Backtracking(startTable, int((n + 1) // 2) * int((n + 1) // 2) + 2 * int(n // 2) * int(n // 2), 3,
             int(n // 2), int((n + 1) // 2))

print(len(bestTable))
for i in bestTable:
    print(str(i.x * sizeOfTable) + ' ' + str(i.y * sizeOfTable) + ' ' + str(i.size * sizeOfTable))
