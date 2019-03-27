import xlrd

def grammer():
    # 打开一个Excel文件
    wb = xlrd.open_workbook('login_test.xlsx')

    # 获取所有的表明
    names = wb.sheet_names()
    print("获取所有的表明", names)

    # 获取所有的表对象
    sheets = wb.sheets()
    print("获取所有的表对象", sheets)

    # 通过索引获取到第一张表
    table1 = sheets[0]
    print("通过索引获取到第一张表", table1.name)

    # 获取表的行数
    rows = table1.nrows
    print("获取表的行数", rows)

    # 获取一行的数据--结果为列表
    row = table1.row_values(0)
    print("获取一行的数据", row)

    # 循环读取每一行
    for row in range(1, rows):
        value = table1.row_values(row)
        print("----", value)

# 将数据拼接为一一对应的形式
def get_sheet_info(filename):
    wb = xlrd.open_workbook(filename)
    usertable = wb.sheet_by_name('浏览器信息表')
    liskkey = ['username','password']
    infolist = []
    for row in range(1,usertable.nrows):
        info = usertable.row_values(row)
        print("info=",info)
        # 将获取的每一行信息都接上关键字
        tem = zip(liskkey,info)
        print('tem',tem)
        # 将每一组数据添加到数据列表中
        infolist.append(dict(tem))
    return infolist


if __name__ == "__main__":
    infolist = get_sheet_info('login_test.xlsx')
    print('infolist',infolist)







