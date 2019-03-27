import time
import xlsxwriter

class LogInfo:
    def __init__(self,path = '',mode = 'w'):
        fname = path+time.strftime('%Y-%m-%d-%H-%M-%S',time.gmtime())+'.txt'
        self.log = open(fname,mode)

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()

class XLLogInfo:
    def __init__(self,tablename,path = ""):
        # 先初始化一个Excel对象
        fname = path + time.strftime('%Y-%m-%d-%H-%M-%S', time.gmtime()) + '.xlsx'
        self.xl = xlsxwriter.Workbook(fname)
        # 创建一张Excel表
        self.table = self.xl.add_worksheet(tablename)
        self.table.set_column('A:E',50)
        # 定义特殊背景
        self.style = self.xl.add_format({'font_color':'red'})

        self.row = 0

    def log_write(self,args):
        # 先定义行和列参数，到时候好控制换号
        # 行
        row = 0
        # 列
        col = 0
        style = ''
        if 'error' in args:
            style = self.style
        for msg in args:
            # 转换为字符串格式，不然写不进去
            m = str(msg)
            self.table.write_string(self.row,col,m,style)
            # 写完之后换一列
            col += 1
        # 写完一行之后换行
        self.row += 1

    def log_close(self):
        self.xl.close()



if __name__ == '__main__':
    # log = LogInfo()
    # log.log_write("测试")
    # log.log_close()

    arg = {'username':'caipiao','password':'caipiao01'}
    err = '用户名或者密码错误'
    msg = []
    msg.append(arg)
    msg.append('error')
    msg.append(err)
    print('msg',msg)
    log = XLLogInfo('测试表')
    log.log_write(msg)
    log.log_close()

    # for m in msg:
    #     print(m)