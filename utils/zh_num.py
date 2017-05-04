# coding: utf-8

import copy
import re


ZH_NUMBER_MAP = {
    '零': 0, '一': 1, '七': 7, '三': 3, '九': 9, '二': 2, '五': 5,
    '八': 8, '六': 6, '四': 4, '十': 10, '伍': 5, '叁': 3, '壹': 1,
    '拾': 10, '捌': 8, '柒': 7, '玖': 9, '肆': 4, '贰': 2, '陆': 6,
    '两': 2,
}

ZH_NUMERAL_MAP = {
    '十': 1e1, '百': 1e2, '千': 1e3, '万': 1e4, '亿': 1e8,
}


def zh_nums_iter(string):
    """ Iter ZH nums in String
    r'(?:(?:一|壹|十|叁|二|零|九|四|伍|六|玖|贰|拾|五|陆|捌|柒|两|三|八|肆|七)+
    (?:千|十|万|百|亿)?)+'
    NOTE: this excludes
            - ``万`` in ``一百万``;
            - ``1000万``;
    """
    zh_nums = ZH_NUMBER_MAP.keys()
    zh_numers = ZH_NUMERAL_MAP.keys()
    regex = r'(?:(?:{})+(?:{})?)+'.format('|'.join(zh_nums), '|'.join(zh_numers))
    return re.finditer(regex, string)


def mul(nums):
    """ Temporary support int < 十万
    """
    ret = list()
    i = 0
    while i < len(nums):
        item = nums[i]
        if item == 0:
            try:
                ret.append(nums[i + 1])
                break
            except IndexError:
                return None
        if item < 10:
            try:
                ret.append(item * nums[i + 1])
                i += 1
            except IndexError:
                ret.append(item)
        elif item == 10:
            ret.append(item)
        i += 1
    return int(sum(ret)) if ret else None


def parse_zh_num(num_str):
    """ Parse ZH numbers

    :type num_str: str
    :return: digit number
    """
    if ZH_NUMBER_MAP.get(num_str):
        return ZH_NUMBER_MAP.get(num_str)

    _map = copy.copy(ZH_NUMBER_MAP)
    _map.update(ZH_NUMERAL_MAP)
    nums = list()
    for char in num_str:
        num = _map.get(char)
        if num is None:
            return None
        nums.append(num)
    return mul(nums)


def zh_num2digit(string):
    """ Replace ZH nums to digit in String"""
    for match in zh_nums_iter(string):
        num_str = match.group(0)
        digit_num = parse_zh_num(num_str)
        if digit_num is None:
            continue
        string = string.replace(num_str, str(digit_num), 1)
    return string
