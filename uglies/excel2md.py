import xlrd

def excel2md(file_path):
    excel = xlrd.open_workbook(file_path)
    table = sheet_by_index(0)

