"""
数据分离，从文件中读取数据
ele_dict = {
        'url' : 'http://gy1yinhe.fftechs.com:2086/',
        'text_xpath': '//*[@id="header"]/div/div[3]/div[1]/span[2]',
        'user_xpath': '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/input',
        'pwd_xpath': '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/input',
        'login_xpath': '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[7]/span',
        'alter_xpath': '//*[@id="layui-layer3"]',
        'username': 'caipiao01',
        'password': 'caipiao01'
    }
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from usedata import get_webinfo
from usedata import  get_userinfo
import time
from log_module import LogInfo
import sys
import os

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

def checkRusult(driver,err_xpath,arg,log):
    """
    请输入6-11位的正确用户名
    请输入6-12位的正确密码
    用户名或密码错误
    :param driver:
    :param args:
    :return:
    """
    time.sleep(3)
    try:
        err = driver.find_element_by_xpath(err_xpath)
        msg = "%s:error:%s"%(arg,err.text)
        log.log_write(msg)
    except:
        msg = "%s:pass"%(arg)
        log.log_write(msg)

def login_test(ele_dict,user_list):
    driver = openBrower()
    loadUrl(driver,ele_dict['url'])
    ele_tuple = findElement(driver,ele_dict)
    log = LogInfo('demo')
    time.sleep(3)
    for arg in user_list:
        sendValues(ele_tuple,arg)
        checkRusult(driver,ele_dict['alter_xpath'],arg,log)
    log.log_close()

if __name__ == '__main__':
    """
    ele_dict = {
        'url' : 'http://gy1yinhe.fftechs.com:2086/',
        'text_xpath': '//*[@id="header"]/div/div[3]/div[1]/span[2]',
        'user_xpath': '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/input',
        'pwd_xpath': '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/input',
        'login_xpath': '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[7]/span',
        'alter_xpath': '//*[@id="layui-layer3"]',
        'username': 'caipiao01',
        'password': 'caipiao01'
    }
   
    user_list = [{ 'username': 'caipiao01', 'password': 'caipiao01'}]
      """
    user_list = get_userinfo('userinfo.txt')

    ele_dict = get_webinfo('webinfo.txt')
    login_test(ele_dict,user_list)
