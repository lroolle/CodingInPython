def is_nested(nested_lst):
    for i in nested_lst:
        if isinstance(i, (list, set, tuple)):
            return True
    return False


def unnest(nested_lst):
    while is_nested(nested_lst):
        # backward to pop the list/set/tuple item in the nested list
        for i in range(len(nested_lst)-1, -1,-1):
            if not isinstance(nested_lst[i], (list, set, tuple)):
                continue

            for j in nested_lst[i]:
                if j not in nested_lst: # get rid of duplicated elements
                    nested_lst.append(j)

            nested_lst.pop(i)

    return nested_lst