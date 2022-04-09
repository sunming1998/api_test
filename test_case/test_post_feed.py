import pytest
from base.base_assertion import Assertion
from base.base_do_excel import DoExcel

# 参数化
test_data_path = DoExcel('test_post_test.xlsx', 'test_post_feed')
test_post_data = test_data_path.read_data()

class TestPostFeed:
    # 使用pytest装饰器方法，‘test_dict' 是参数化，’test_demo_path' 是一个列表，装饰器方法就是在这个列表里面循环取值
    @pytest.mark.parametrize('test_dict', test_post_data)
    def test_demo(self, login, test_dict):
        # 找到字典里面的data 如果不为空，直接判断为post请求，替换数据
        if test_dict['data'] is not None:
            # 如果找到userid 则替换
            if test_dict['data'].find('${userID}') != -1:
                new_param = test_dict['data'].replace('${userID}', str(login[0]))
                test_dict['data'] = new_param

            # 找userkey 然后替换
            if test_dict['data'].find('${userKey') != -1:
                new_param = test_dict['data'].replace('${userKey}', "'" + str(login[1] + "'"))
                test_dict['data'] = new_param



