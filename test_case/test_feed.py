import pytest
from base.base_do_excel import DoExcel
from base.base_assertion import Assertion

test_data_path = DoExcel('test_demo.xlsx','case')
# 实例化类
test_demo_path = test_data_path.read_data()
# 实例化类方法

class TestDemo:
    @pytest.mark.parametrize('test_dict', test_demo_path)
    # 使用pytest装饰器方法，‘test_dict' 是参数化，’test_demo_path' 是一个列表，装饰器方法就是在这个列表里面循环取值
    def test_001(self, test_dict):
        assertion = Assertion(test_dict, test_data_path)
        assertion.send_request()
        assertion.assertion_result()


if __name__ == '__main__':
    pytest.main(['-v','test_feed.py'])

