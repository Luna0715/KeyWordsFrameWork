#encoding = utf-8

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.VarConfig import chromeDriverFilePath
from config.VarConfig import ieDriverFilePath
from config.VarConfig import firefoxDriverFilePath
from util.ClipboardUtil import Clipboard
from util.DirAndTime import getCurrentTime, createCurrentDateDir
from util.KeyBoardUtil import KeyboardKeys
from util.ObjectMap import getElement
from util.WaitUtil import WaitUtil

#定义全局driver变量
driver = None
#全局的等待类实例对象
waitUtil = None

def open_browser(browserName,*arg):
    #打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            #创建Chrome浏览器的一个Options实例对象
            chrome_options = Options()
            #添加屏蔽--ignore-certificate-errors提示信息的设置参数项
            chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath,chrome_options = chrome_options)
        else:
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
        #driver对象创建成后，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url,*arg):
    #访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*arg):
    #关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise

def sleep(sleepSeconds,*arg):
    #强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*arg):
    #清除输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    #在页面输入框中输入数据
    global driver
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*arg):
    #单击页面元素
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*arg):
    #断言页面源码是否存在某关键字或关键字符串
    global driver
    try:
        assert assertString in driver.page_source,"%s not found in page source!" %assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def assert_title(titleStr,*arg):
    #断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title,"%s not found in title!" %titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def getTitle(*arg):
    #获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSource(*arg):
    #获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def switch_to_frame(locationType,frameLocatorExpression,*arg):
    #切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locationType,frameLocatorExpression))
    except Exception as e:
        print("frame error")
        raise e

def switch_to_default_content(*arg):
    #切出frame
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def paste_string(pasteString,*arg):
    #模拟Ctrl+V操作
    try:
        Clipboard.setText(pasteString)
        #等待2s，防止代码执行的太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

def press_tab_key(*arg):
    #模拟tab键
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

def press_enter_key(*arg):
    #模拟Enter键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    #窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def capture_screen(*arg):
    #截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) +"\\" + str(currTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def waitPresenceOfElementLocated(locationType,locatorExpression,*arg):
    '''显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

def  waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,*arg):
    global waitUtil
    '''检查frame是否存在，存在则切换进frame控件中'''
    try:
       waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*arg):
    '''显式等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")
    driver.get("http://mail.163.com")
    capture_screen()