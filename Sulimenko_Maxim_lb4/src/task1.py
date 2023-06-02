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
# и находятся все вхождения слова в текст
def execute_kmp_algorithm(word, text):

    wordLength = len(word)
    textLength = len(text)
    prefixArray = get_prefixes(word)
    occurrenceArray = []
    iCount = 0
    jCount = 0

    while iCount < textLength:
        if text[iCount] == word[jCount]:
            iCount += 1
            jCount += 1
            if jCount == wordLength:
                occurrenceArray.append(iCount - wordLength)
                if jCount > 0:
                    jCount = prefixArray[jCount - 1]
                else:
                    iCount += 1
        else:
            if jCount > 0:
                jCount = prefixArray[jCount - 1]
            else:
                iCount += 1

    if len(occurrenceArray) > 0:
        return occurrenceArray

    return -1


word = input()
text = input()
print(*execute_kmp_algorithm(word, text), sep=',')
