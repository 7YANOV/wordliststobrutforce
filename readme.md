### Script Readme
This repository contains a script that sorts files from a list.

### Usage
The script can be executed with the following command:
````
python main.py FILE_LIST
Replace FILE_LIST with the path to the file containing the list of files to sort.
````

### Requirements
Python 3.x \
argparse module

### Sorting Method
````
The script uses different sorting methods based on the operating system:

On Windows, it reads the lines from each file, sorts them, and writes them to a new file.
On Linux, it uses the sort command to sort the contents of each file.
Output
The script generates sorted files for each input file. The sorted files are prefixed with "sorted_". Additionally, the script merges the sorted files into a single result file named "result_wordlists.txt".
````
### Example
````
To sort files listed in the files.txt file, run the following command:

python main.py files.txt
The sorted files will be generated as sorted_file1.txt, sorted_file2.txt, etc. The merged result file will be named result_wordlists.txt.

Note: The script assumes that the files listed in the file list are text files.
````
### Cleanup
```
After generating the sorted files and the result file, the script removes the intermediate sorted files.
```
### Disclaimer
This script is provided as-is without any warranties. Use it at your own risk.