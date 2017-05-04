
import re


def merge_spaces(string):
    return re.sub(' +', ' ', string)


def merge_newlines(string):
    return re.sub('\n+( +\n)*', '\n', string)


def strip_alnum(string):
    string = string.strip()
    return ''.join([char for char in string if '\u4e00' <= char <= '\u9fff'])


def strip_sticker(string):
    """去除表情符号, 如：
    [微笑][闭嘴][惊讶]...
    """
    return re.sub(r'\[[\u4e00-\u9fffa-zA-Z]{1,3}\]', '', string)


def strip_space(string):
    sentence_list = string.split('\n')
    for index, sentence in enumerate(sentence_list):
        sentence_list[index] = sentence.strip(' \t')

    return '\n'.join(sentence_list)


def replace_breaks(string, rep=' '):
    """把 Str 中的换行，非半角空格等替换成 rep
    """
    return rep.join(string.split())
