import codecs
def get_webinfo(path):
    webinfo = {}
    # config = open(path)
    config = codecs.open(path,'r','utf-8')
    for line in config:
        result = [ele.strip() for ele in line.split('==')]
        webinfo.update(dict([result]))
    return webinfo

def get_userinfo(path):
    userinfo = []
    config = codecs.open(path, 'r', 'utf-8')
    for line in config:
        user_dict = {}
        result = [ele.strip() for ele in line.split(';')]
        for r in result:
            data = [ele.strip() for ele in r.split('=')]
            user_dict.update(dict([data]))
        userinfo.append(user_dict)
    return userinfo

if __name__ == '__main__':
    # info = get_webinfo('webinfo.txt')
    # for s in info:
    #     print(s,info[s])

    info = get_userinfo('userinfo.txt')
    for s in info:
        print(s)