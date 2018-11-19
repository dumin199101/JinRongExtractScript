# coding=utf-8
"""
@Project: JinRong
@Time: 2018/9/26 15:59
@Name: ComputeFileLines
@Author: lieyan123091
"""
def compute_lines(filepath):
    count = 0
    for index, line in enumerate(open(filepath, 'r')):
        count += 1
    print count



if __name__ == '__main__':
    filepath = "Content_PDF_File.txt"
    compute_lines(filepath)