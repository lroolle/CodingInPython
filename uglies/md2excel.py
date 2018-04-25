import xlwt


def markdown2excel(file_path):
    with open(file_path, 'r') as fp:
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('三方理财')
        c = 0
        for line in fp.readlines():
            row = line.strip('|').split('|')
            if not row or '--' in row[0] or len(row) < 2:
                continue

            name, host = row[0], row[1]
            host = host.replace('>', '').replace('<', '')
            print(name, host)
            sheet.write(c, 0, name)
            sheet.write(c, 1, host)
            c += 1
        book.save('/home/wrq/tmp/third_party.xls')

