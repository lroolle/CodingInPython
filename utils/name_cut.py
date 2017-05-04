
import re

from .alnum import is_alpha, is_alnum, is_unit
from .stripers import merge_spaces


def get_name_cut(string):
    """把中文串拆成字，英文/数字拆成整体，
    并且去除无关紧要的符号
    """
    s_cleaned = re.sub(r'\W+', ' ', string.replace(' ', '')).strip()
    s_len = len(s_cleaned)
    name_cut = ''
    for i, char in enumerate(s_cleaned):
        char = char.upper() if is_alpha(char) else char
        if i < s_len - 1 and is_alnum(char):
            if is_alnum(s_cleaned[i + 1]) or is_unit(s_cleaned[i + 1]):
                name_cut += char
            else:
                name_cut += char + ' '
        elif char == ' ' or i == s_len - 1:
            name_cut += char
        else:
            name_cut += char + ' '

    return merge_spaces(name_cut)