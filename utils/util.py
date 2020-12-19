import openpyxl


# 将已领用时导出表中的数据按行装载到received_list中
def get_received_excel(path):
    book = openpyxl.load_workbook(path)
    sheet = book.active
    # D需要编辑的为最后一列，循环找到最后一行的后一行再减一行即为最后一行
    n = 1
    row_str = 'D' + str(n)
    while sheet[row_str].value is not None:
        n += 1
        row_str = 'D' + str(n)
    n -= 1
    row_str = 'D' + str(n)
    received_excel = sheet['A2':row_str]
    # 按行获取整张表中的数据于list中
    received_list = []
    for goods_name, asset_numb, top, cloud in received_excel:
        row_dict = {'goods_name': goods_name.value, 'asset_numb': asset_numb.value, 'top': top.value, 'cloud': cloud.value}
        received_list.append(row_dict)
    return received_list