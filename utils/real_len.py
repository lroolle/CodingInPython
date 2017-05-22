

def real_len(string):
    """ Dont know WTF is real len, copy from sb's code
    """
    return len(string) - sum(1 for c in string if c > chr(127)) / 3
