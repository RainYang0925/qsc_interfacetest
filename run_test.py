# __author__ = 'zhagnzhiyuan'
#-*-coding:utf-8-*-
import sys
sys.path.append('./test_case/models')
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders
from email import MIMEBase
import smtplib
import unittest
import time
import os

'''
==============说明===============
功能:测试用例执行,html报告生成,邮件发送
入口:测试用例目录
================================
'''
reload(sys)
sys.setdefaultencoding('utf8')
# =========================邮件接收者============================
mailto_list = sys.argv[2:] #接收命令行传入参数
#============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host="smtp.163.com"
mail_user="*************"
mail_pass="*************"
#===========================发送邮件============================
def send_mail(to_list,file_new):
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    me=mail_user
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = u'轻松筹接口自动化测试报告'
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    #发送附件
    # att = MIMEText(mail_body, 'base64', 'utf-8')
    # att["Content-Type"] = 'application/octet-stream'
    # att["Content-Disposition"] = 'attachment; filename="123.html"'
    # msg = MIMEMultipart('related')
    # msg.attach(att)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host,25)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

#==============查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "//" + fn))
    file_new = os.path.join(testreport,lists[-1])
    # print(file_new)
    return file_new

if __name__ == '__main__':
    parameter = sys.argv[1] #接受命令行传入参数
    testcase = parameter + '.py'
    # print testcase
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/html/' + now +'.html'
    # filename = './qscweb/report/html/11.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'轻松筹接口自动化测试报告',
                          description=u'环境 ：')
    discover = unittest.defaultTestLoader.discover('./test_case',pattern=testcase)
    # suite = unittest.TestSuite
    # suite.addTest()

    runner.run(discover)
    fp.close()
    file_path = new_report('./report/html/')
    temp = open(file_path, 'rb')
    a = temp.read()  # 读取报告内容
    temp.close()
    p = r"<td class='errorCase'>"  #查找报告中错误内容
    q = r"<td class='failCase'>"
    if p in a or q in a:
        print('we need to send E-mail.')
        if send_mail(mailto_list, file_path):
            print u"发送成功"
        else:
            print u"发送失败"
    else:
        print(u'测试通过不发送报告')