# Метод для генерации массива префиксов слова
# Необходим для работы алгоритма КМП
def get_prefixes(word):
    jCount = 0
    iCount = 1
    prefixArray = [0] * len(word)

    while iCount < len(word):
        if word[jCount] == word[iCount]:
            prefixArray[iCount] = jCount + 1
            iCount += 1
            jCount += 1
        else:
            if jCount == 0:
                prefixArray[iCount] = 0
                iCount += 1
            else:
                jCount = prefixArray[jCount - 1]

    return prefixArray


# Метод, в котором выполняется алгоритм КМП
# для определения, является ли word циклическим
# сдвигом text
def execute_kmp_circle_algorithm(word, text):

    wordLength = len(word)
    textLength = len(text)
    prefixArray = get_prefixes(word)
    shiftIndex = -1
    iCount = 0
    jCount = 0

    if wordLength != textLength:
        return shiftIndex

    while iCount < textLength * 2:
        if text[iCount % textLength] == word[jCount]:
            iCount += 1
            jCount += 1
            if jCount == wordLength:
                shiftIndex = iCount - wordLength
                return shiftIndex
        else:
            if jCount > 0:
                jCount = prefixArray[jCount - 1]
            else:
                iCount += 1

    return shiftIndex


text = input()
word = input()
print(execute_kmp_circle_algorithm(word, text))
