import argparse
import platform
import os

file1 = open("test_pass1.txt", "r")
file2 = open("test_pass2.txt", "r")
file3 = open("test_pass3.txt", "r")
sortedFile1 = open("sorted_test_pass1.txt", "w+")
sortedFile2 = open("sorted_test_pass2.txt", "w+")
sortedFile3 = open("sorted_test_pass3.txt", "w+")



def sortFile(file, sortedFile):
    if platform.system() == 'Windows':
        lines = file.readlines()
        lines.sort()
        for line in lines:
            sortedFile.write(line)
        sortedFile.close()
    elif platform.system() == 'Linux':
        os.system(f"sort {file} > {sortedFile}")


def sort_files_from_list(file_list):
    with open(file_list, 'r') as f:
        files_to_sort = f.readlines()

    for file in files_to_sort:
        if file.strip() == '':
            continue
        file = file.strip()
        sorted_file = open(f"sorted_{file}", "w+")
        sortFile(open(file, "r"), sorted_file)





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


sort_files_from_list("wordlists.txt")


#sortFile(file1, sortedFile1)
#sortFile(file2, sortedFile2)
#sortFile(file3, sortedFile3)

#mergeSortedLists(open("sorted_test_pass1.txt", "r"), open("sorted_test_pass2.txt", "r"))

