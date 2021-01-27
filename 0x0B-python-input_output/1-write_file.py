#!/usr/bin/python3
'''Module- Open, read and write content on a file'''


def write_file(filename="", text=""):
    '''
    Write in (file)<filename> a text (str)<text>
    Args:
        filename: name of file to analyze
        text: text to write
    '''

    with open(filename, 'r+', encoding='utf8') as f:
        return f.write(text)
    f.closed
