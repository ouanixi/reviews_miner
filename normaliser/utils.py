import string

def remove_nonascii(text):
    printable = set(string.printable)
    text = filter(lambda x: x in printable, text)
    return text