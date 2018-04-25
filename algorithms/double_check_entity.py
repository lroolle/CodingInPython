

def get_entity_str(entity_list, offset):
    size = len(entity_list)
    entity_str = ''
    while offset < size:
        item = entity_list[offset]
        word, tag = item['word'], item['entity']
        single_entity = False
        offset += 1
        if offset == size:
            single_entity = True
        next_diff = entity_list[offset]['entity'][0] != tag[0] if offset < size else None
        if next_diff and tag.endswith('_s'):
            single_entity = True

        if not tag == 'o':
            entity_str += word

        if tag.endswith('_e') or single_entity:
            return tag[0], entity_str, offset


def double_check(ltp_entity_list, jieba_entity_list):
    i, j = 0, 0
    ltp_stop, jieba_stop = False, False
    while not (ltp_stop or jieba_stop):
        ltp_ret = get_entity_str(ltp_entity_list, i)
        if ltp_ret:
            ltp_tag, ltp_entity_str, i = ltp_ret
        else:
            ltp_stop = True

        jieba_ret = get_entity_str(jieba_entity_list, j)
        if jieba_ret:
            jieba_tag, jieba_entity_str, j = jieba_ret
        else:
            jieba_stop = True

        # Check if match
        if ltp_ret and jieba_ret:
            print('=' * 20)
            if not jieba_entity_str == ltp_entity_str:
                print('Wrong')
                print('   ltp : "{}"<-"{}"'.format(ltp_tag, ltp_entity_str))
                print('  jieba: "{}"<-"{}"'.format(jieba_tag, jieba_entity_str))
            else:
                print('Ok')

ltp = [{'word': 'abc', 'entity': 'e_s'}, {'word': 'def', 'entity': 'n_s'}]
jieba = [{'entity': 'e_s', 'word': 'ab'},
         {'entity': 'n_s', 'word': 'cd'},
         {'entity': 'n_e', 'word': 'ef'}]

double_check(ltp, jieba)

ltp = [{'word': 'a', 'entity': 'e_s'}, {'word': 'b', 'entity': 'e_i'},
       {'word': 'c', 'entity': 'e_e'}, {'word': 'def', 'entity': 'n_s'}]
jieba = [{'entity': 'e_s', 'word': 'ab'},
         {'entity': 'n_s', 'word': 'cd'},
         {'entity': 'n_e', 'word': 'ef'}]

double_check(ltp, jieba)

ltp = [{'word': 'a', 'entity': 'o'}, {'word': 'b', 'entity': 'n_s'},
       {'word': 'cd', 'entity': 'e_s'}, {'word': 'e', 'entity': 'e_i'},
       {'word': 'fg', 'entity': 'e_i'}, {'word': 'h', 'entity': 'e_e'},
       {'word': 'i', 'entity': 'o'}, {'word': 'j', 'entity': 'd_s'},
       {'word': 'kl', 'entity': 'o'},{'word': 'mn', 'entity': 'o'},]
jieba = [{'word': 'a', 'entity': 'o'}, {'word': 'b', 'entity': 'n_s'},
         {'word': 'c', 'entity': 'e_s'}, {'word': 'd', 'entity': 'e_s'},
         {'word': 'e', 'entity': 'e_i'},
         {'word': 'f', 'entity': 'e_i'}, {'word': 'g', 'entity': 'e_i'},
         {'word': 'h', 'entity': 'e_e'},
         {'word': 'i', 'entity': 'o'}, {'word': 'j', 'entity': 'd_s'},
         {'word': 'klmn', 'entity': 'o'}, ]

double_check(ltp, jieba)
