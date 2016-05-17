"""## Reverse Words

> Given a sentence, reverse the words one by one, keeping the blank.

For example:

`s = 'Hello Lroolle'`

 return `olleH elloorL`

"""


def reverse_words(s):
    return ' '.join(x[::-1] for x in s.split(' '))

print(reverse_words('Hello     Lroolle'))
