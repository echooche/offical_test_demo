import codecs
def get_webinfo_byfile(path):
    """
    从文件读取浏览器信息
    :param path:
    :return:
    """
    webinfo = {}
    # config = open(path)
    config = codecs.open(path,'r','utf-8')
    for line in config:
        result = [ele.strip() for ele in line.split('==')]
        webinfo.update(dict([result]))
    return webinfo

def get_userinfo_byfile(path):
    """
    从文件读取用户信息
    :param path:
    :return:
    """
    userinfo = []
    config = codecs.open(path, 'r', 'utf-8')
    for line in config:
        user_dict = {}
        result = [ele.strip() for ele in line.split(';')]
        for r in result:
            data = [ele.strip() for ele in r.split('=')]
            print('data',data)
            user_dict.update(dict([data]))
        userinfo.append(user_dict)
    return userinfo

# 从Excel读取数据的类
import xlrd
class XLUserInfo():
    def __init__(self,path):
        """
        初始化对象的时候创建一个表对象
        :param path:
        """
        self.xl = xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,name,describle):
        """
        通过表名获取到Excel表，然后再从表中获取数据
        :param name:
        :return: 通过获取的表对象去读取数据
        """
        self.table = self.xl.sheet_by_name(name)
        return self._get_sheet_info(describle)

    def get_sheetinfo_by_index(self,index,describle):
        """
        通过索引获取到Excel表，再从表中获取数据
        :param index:
        :return: 通过获取的表对象去读取数据
        """
        self.table = self.xl.sheet_by_index(index,)
        return self._get_sheet_info(describle)

    # 该方法外部拿去没用，所以进行私有化
    def _get_sheet_info(self,describle):
        """
        从表中获取数据，并给于格式
        :param describle: 描述信息，通过该描述信息判断返回的值以及值的格式
        :return: 返回读取的数据
        """
        userkey = ["username","password"]
        # 用户信息
        userinfo = []
        # 浏览器信息
        webinfo = []
        # 循环读取没一行数据
        for row in range(1,self.table.nrows):
            # 通过行号获取每一行
            info = self.table.row_values(row)
            if describle == "user":
                # 做格式拼接
                temp = zip(userkey,info)
                # 将拼接好的数据加入到用户信息列表中
                userinfo.append(dict(temp))
            elif describle == "web":
                # 将拼接好的数据加入到浏览器信息列表中
                webinfo.append(info)
        # 通过判断需要的值返回响应的值
        if describle == "web":
            return dict(webinfo)
        elif describle == "user":
            return userinfo

if __name__ == '__main__':
    # info = get_webinfo_byfile('webinfo.txt')
    # for s in info:
    #     print(s,info[s])
    # print(info)

    xluserinfo = XLUserInfo('login_test.xlsx')
    # info = xluserinfo.get_sheetinfo_by_name('用户信息表','user')
    info = xluserinfo.get_sheetinfo_by_index(1,"web")
    print(info)

