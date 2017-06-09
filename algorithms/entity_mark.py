"""
> Given a sentences, with different word cut,

Mark a different word list according to a marked entity list.

For example:
    marked = [('ab', 'o'), ('cd', 'e_s'), ('e', 'e_i'), ('fg', 'e_e')]
    to_be_marked = ['ab', 'cd', 'ef', 'g']

should return:
    marked_entity = [('ab', 'o'), ('cd', 'e_s'), ('ef', 'e_i'), ('g', 'e_e')]
"""


def mark(marked, to_mark):
    i, j, k = 0, 0, 0
    index = [0, 0]
    for marked_item in marked:
        marked_word, tag = marked_item['word'], marked_item['entity']
        i += len(marked_word)
        if tag == 'o':
            index[0] = i
        else:
            index[1] = i - 1
        print(index)

    return to_mark



