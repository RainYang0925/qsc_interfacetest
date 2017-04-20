# __author__ = 'zzy'
#-*-coding:utf-8-*-

from models import myunit
from db_fixture.mysql_setting import MySQLOperating
from models.buildcase import BuildCase
import unittest

'''
===========说明============
功能:测试用例定义
入口:ecxel表格测试用例
==========================
'''


class Interface(myunit.MyTest):
    '''轻松筹:微爱项目'''

    db = MySQLOperating()
    # test = Testcase()

    # 构建测试用例,一条测试用例对应一个函数
    FUNC_TEMPLATE = '''@unittest.skipUnless({state},'state值为0,跳过测试')\ndef {func}(self):
            '{casename}'
            BuildCase().execute_case({onecase},'{sheetname}')
            '''

    # 获取sheet页中的测试用例,返回测试用例字典
    testcaselist = db.get_caselist('interface_love')
    for testcase in testcaselist:
        exec (FUNC_TEMPLATE.format(func=testcase['case_id'],
                                   casename=testcase['case_name'],
                                   onecase=testcase,
                                   sheetname='interface_love',
                                   state=testcase['state'],
                                   ))


if __name__ == '__main__':
    unittest.main()