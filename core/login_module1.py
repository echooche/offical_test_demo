"""
模块化
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

url = 'http://gy1yinhe.fftechs.com:2086/'

def getEle(driver,time,xpath,describe):
    ele = WebDriverWait(driver,time).until(lambda d: d.find_element_by_xpath(xpath))
    return ele

def openBrower():
    """
    :return: 返回驱动
    """
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle

def loadUrl(driver,url):
    """
    :param driver: 驱动
    :param url: URL地址
    """
    driver.get(url)
    driver.maximize_window()

def findElement(driver,kwargs):
    """
    kwargs must bu dict
    text_xpath;
    user_xpath:
    pwd_xpath:
    login_xpath:
    :param driver:
    :param kwargs:
    :return:
    """
    if 'text_xpath' in kwargs:
        login = getEle(driver, 10, kwargs['text_xpath'], '登录')
        login.click()
    username_inp = getEle(driver, 10, kwargs['user_xpath'], '用户名')
    pwd_inp = getEle(driver, 10, kwargs['pwd_xpath'], '密码')
    instant_login = getEle(driver, 10, kwargs['login_xpath'], '立即登陆')
    return username_inp,pwd_inp,instant_login

def sendValues(eletuple,arg):
    """

    :param eletuple:
    :param arg: username,password
    :return:
    """
    listkey = ['username','password']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i += 1
    assert  eletuple[2].text == '立即登录'
    eletuple[2].click()

def checkRusult(driver,args):
    """

    :param driver:
    :param args:
    :return:
    """
    try:
        div = getEle(driver,10,args['alter_xpath'],'点击登录之后出现的提示框')
        print('用户名或者密码格式不正确')
    except:
        print('登录成功')

def login_test():
    driver = openBrower()
    loadUrl(driver,url)

#     登录
    ele_dict = {
        'text_xpath' : '//*[@id="header"]/div/div[3]/div[1]/span[2]',
        'user_xpath' : '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/input',
        'pwd_xpath'  :  '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/input',
        'login_xpath' :  '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[7]/span',
        'alter_xpath' : '//*[@id="layui-layer3"]'
    }

    account_dict = {'username':'caipiao01','password':'caipiao01'}
    ele_tuple = findElement(driver,ele_dict)
    import time
    time.sleep(3)
    sendValues(ele_tuple,account_dict)
    checkRusult(driver,ele_dict)

if __name__ == '__main__':
    login_test()