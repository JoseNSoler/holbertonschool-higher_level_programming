#!/usr/bin/python3
'''Module- Open, read and append content on a file'''


def append_write(filename="", text=""):
    '''
    Appends in (file)<filename> the text (str)<text>
    Args:
        filename: name of file to analyze
        text: text to append
    '''

    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
    f.closed
