import re


def split(string, chunk_size, char_regex=None):
    char_regex = char_regex if char_regex else '.'
    regex = r'(%s{%s})' % (char_regex, chunk_size)
    return [chunk for chunk in re.split(regex, string) if chunk]
