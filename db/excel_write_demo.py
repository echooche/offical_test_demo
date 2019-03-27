import xlsxwriter

def grammer():
    # 先创建一个excel文件
    xl = xlsxwriter.Workbook('write.xlsx')
    table = xl.add_worksheet('用户信息表')
    # 只有向表中插入数据的时候，这个表才会真正的被产生
    table.write_string('A1','username')
    # 设置单元格大小
    table.set_column('A:E',20)
    xl.close()


