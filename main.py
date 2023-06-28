import argparse
import platform
import os


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
        files_to_sort = f.read().splitlines()
    sorted_file_list = []
    for file in files_to_sort:
        if file.strip() == '':
            continue
        file = file.strip()
        print(f"Sorting {file}...")
        sorted_file = open(f"sorted_{file}", "w+")
        sorted_file_list.append(f"sorted_{file}")
        sortFile(open(file, "r"), sorted_file)
    return sorted_file_list


def mergeSortedLists(sortedPass1, sortedPass2):
    resultFile = open("temp_wordlist.txt", "w+")
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



if __name__ == "__main__":
    if os.path.exists("result_wordlists.txt"):
        os.remove("result_wordlists.txt")
    parser = argparse.ArgumentParser(description="Sort files from a list.")
    parser.add_argument("list_of_files", metavar="FILE_LIST", help="Path to the file list")
    args = parser.parse_args()
    sorted_file_list = sort_files_from_list(args.list_of_files)
    if sorted_file_list:
        mergeSortedLists(open(sorted_file_list[0], "r"), open(sorted_file_list[1], "r"))
        os.rename("temp_wordlist.txt", "result_wordlists.txt")
        for i in range(2, len(sorted_file_list)):
            mergeSortedLists(open("result_wordlists.txt", "r"), open(sorted_file_list[i], "r"))
            os.remove("result_wordlists.txt")
            os.rename("temp_wordlist.txt", "result_wordlists.txt")
        print("Done!")
    for file in sorted_file_list:
        print(f"Removing {file}")
        os.remove(file)


