#encoding = utf-8
import os

ieDriverFilePath = ""
chromeDriverFilePath = "D:\driver\chromedriver"
firefoxDriverFilePath = ""

#获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#异常截图存放目录绝对路径
screenPicturesDir = parentDirPath + "\\exceptionpictures\\"

#测试数据文件存放绝对路径
dataFilePath = parentDirPath + "\\testData\\163邮箱发送邮件.xlsx"

#测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 2
testCase_testStepSheetName = 4
testCase_isExecute = 5
testCase_runTime = 6
testCase_testResult = 7

#用例步骤表中，部分列对应的数字序号
testStep_testStepDescirbe = 2
testStep_keyWords = 3
testStep_locationType = 4
testStep_locatorExpression = 5
testStep_operateValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errirPic = 10