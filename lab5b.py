#!/usr/bin/env python3
# Author ID: ozaman1

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    tgtfile = open(file_name, 'r')
    readfile = tgtfile.read()
    tgtfile.close
    return readfile

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    tgtfile = open(file_name, 'r')
    readfile = tgtfile.read().splitlines()
    tgtfile.close
    return readfile

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    tgtfile = open(file_name, 'a')
    appendstring = tgtfile.write(str(string_of_lines))
    tgtfile.close
    return appendstring

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    tgtfile = open(file_name, 'w')
    for item in list_of_lines:
        tgtfile.write(str(item)+'\n')
    tgtfile.close
    return tgtfile

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    # Read first file
    tgtfile = open(file_name_read, 'r')
    filedata = tgtfile.readlines()
    tgtfile.close
    # Create and copy contents to the new file
    newfile = open(file_name_write, 'w')
    linenumber = 1
    for data in filedata:
        newfile.write(str(linenumber)+':'+(data))
        linenumber += 1
    newfile.close
    return newfile

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))