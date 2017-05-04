

def table_render(data, style=None):
    """
    :param style: border style or sth
    :type data: list
    :return: table div
    """
    style = style if style else 'border:1px solid #ccc'
    td_size = len(data[0])
    tr_tpl = '<tr>{}</tr>'
    th_tpl = tr_tpl.format('<th style="text-align:center;min-width:80px;'
                           '{style}">{}''</th>' * td_size)
    td_tpl = tr_tpl.format('<td style="{style}">{}</td>' * td_size)
    table_tpl = '<div><table style="border-collapse: collapse;">' \
                '{header}{content}</table></div>'

    table = table_tpl.format(
        header=th_tpl.format(*data[0], style=style),
        content=''.join([td_tpl.format(*values, style=style)
                         for values in data[1:]]),
    )
    return table