

def is_han(text):
    return all('\u4e00' <= char <= '\u9fff' for char in text)


def is_number(char):
    try:
        float(char)
        return True
    except ValueError:
        return False


def is_alpha(char):
    return ('\u0041' <= char <= '\u005a') \
           or ('\u0061' <= char <= '\u007a')


def is_alnum(char):
    return is_number(char) or is_alpha(char)


def is_unit(char):
    units = {'年', '月', '日', '天', '万', '千', '个', '号', '期', '类'}
    return char in units