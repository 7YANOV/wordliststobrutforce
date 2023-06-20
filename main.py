

file1 = open("test_pass1.txt", "r")
file2 = open("test_pass2.txt", "r")

sortedFile1 = open("sorted_test_pass1.txt", "w+")
sortedFile2 = open("sorted_test_pass2.txt", "w+")


def sortFile(file, sortedFile):
    lines = file.readlines()
    lines.sort()
    for line in lines:
        sortedFile.write(line)
    sortedFile.close()


def mergeSortedLists(sortedPass1, sortedPass2):
    resultFile = open("result.txt", "w+")
    currentLine1 = sortedPass1.readline()
    currentLine2 = sortedPass2.readline()

    previousLine = ''
    while (currentLine1 != '' and currentLine2 != ''):
        if (currentLine1 < currentLine2):
            if (previousLine == currentLine1):
                currentLine1 = sortedPass1.readline()
                continue

            previousLine = currentLine1
            resultFile.write(currentLine1)
            currentLine1 = sortedPass1.readline()
        else:
            if (previousLine == currentLine2):
                currentLine2 = sortedPass2.readline()
                continue

            previousLine = currentLine2
            resultFile.write(currentLine2)
            currentLine2 = sortedPass2.readline()

    if (currentLine1 == ''):
        while (currentLine2 != ''):
            if (previousLine == currentLine2):
                currentLine2 = sortedPass2.readline()
                continue

            previousLine = currentLine2
            resultFile.write(currentLine2)
            currentLine2 = sortedPass2.readline()
    else:
        while (currentLine1 != ''):
            if (previousLine == currentLine1):
                currentLine1 = sortedPass1.readline()
                continue

            previousLine = currentLine1
            resultFile.write(currentLine1)
            currentLine1 = sortedPass1.readline()

    resultFile.close()


sortFile(file1, sortedFile1)
sortFile(file2, sortedFile2)

mergeSortedLists(open("sorted_test_pass1.txt", "r"), open("sorted_test_pass2.txt", "r"))
