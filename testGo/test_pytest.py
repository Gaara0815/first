import pytest
import os
import allure

class Test_caseqq():
    def test_case1(self):
        print('test1')
        assert 1==0

    def test_case2(self):
        '''测试2'''
        print('test2')
        assert 1>0



if __name__ == '__main__':
    #生成测试报告
    pytest.main(['test_pytest.py','-s','--alluredir=tmp/allure_result'])
    os.system('allure serve tmp/allure_result')