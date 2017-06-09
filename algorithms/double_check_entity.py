

def _t(tag):
    return tag.split('_')[0]


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
        next_diff = _t(entity_list[offset]['entity']) != _t(tag) if offset < size else None
        if next_diff and tag.endswith('_s'):
            single_entity = True

        if not tag == 'o':
            entity_str += word

        if tag.endswith('_e') or single_entity:
            return _t(tag), entity_str, offset


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
                print('Ok "{}"<-"{}"'.format(jieba_tag, jieba_entity_str))


def get_entity_remark(ltp, jieba):
    i, j, k, ret = 0, 0, 0, list()
    consumed = True

    for ltp_item in ltp:
        ltp_word = ltp_item.get('word')
        i += len(ltp_word)

        if ret and not _t(ret[-1]['entity']) == _t(ltp_item.get('entity')):
            if not any([ltp_item.get('entity') == 'o', ret[-1]['entity'] == 'o']):
                consumed = True

        if consumed or ltp_item.get('entity') == 'o' or entity == 'o':
            entity = ltp_item.get('entity')

        while k < len(jieba):
            jieba_word = jieba[k]
            k += 1
            j += len(jieba_word)
            if j <= i:
                if ret and _t(ret[-1]['entity']) == _t(entity):
                    if ret[-1]['entity'].endswith(('_s', '_i')):
                        entity = _t(entity) + '_e'
                    if ret[-1]['entity'].endswith('_e'):
                        ret[-1]['entity'] = _t(entity) + '_i'

                ret.append({'word': jieba_word, 'entity': entity})
                consumed = True
            else:
                k -= 1
                j -= len(jieba_word)
                consumed = False
                break

    double_check(ltp, ret)
    return ret
