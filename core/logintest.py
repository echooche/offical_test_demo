
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

url = 'http://gy1yinhe.fftechs.com:2086/'
username = 'caipiao01'
password = 'caipiao'


def getEle(driver,time,xpath,describe):
    ele = WebDriverWait(driver,time).until(lambda d: d.find_element_by_xpath(xpath))
    return ele


def login_test():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

#     登录
    login = getEle(driver,10,'//*[@id="header"]/div/div[3]/div[1]/span[2]','登录')
    login.click()

    username_inp = getEle(driver, 10, '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/input',
                          '用户名')
    pwd_inp = getEle(driver, 10, '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/input', '密码')
    username_inp.send_keys(username)
    pwd_inp.send_keys(password)

    instant_login = getEle(driver, 10, '//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[7]/span', '立即登陆')
    time.sleep(3)
    instant_login.click()

    try:
        # 通过xpath属性定位到父元素，在通过父元素定位子元素
        time.sleep(3)
        err = driver.find_element_by_xpath('//div[@type="dialog"]/div[2]')
        print(err.text)
        sure = driver.find_element_by_xpath('//div[@type="dialog"]/div[3]/a')
        sure.click()
    except:
        print('登录成功')




if __name__ == '__main__':
    login_test()