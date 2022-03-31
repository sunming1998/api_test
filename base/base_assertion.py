from base.base_requests import MyRequests
from base.base_do_excel import DoExcel
import json

class Assertion():
    def __init__(self, test_dict, test_data_path):
        # 这里将类方法传两个实例化属性，一个是传入字典，因为下面的requests的方法需要用字典取出测试用例
        # 一个是实例化一个属性，为Doexcel的写入返回结果的方法
        self.test_dict = test_dict
        self.test_data_path = test_data_path


    def send_request(self):
        res = MyRequests().send_requests(method=self.test_dict['method'], url=self.test_dict['url'], data=self.test_dict['data'],
                                        headers=self.test_dict['headers'])

        # 写回返回结果
        self.test_data_path.write_data(int(self.test_dict['case_id']) + 1, 8, str(res.text))
        return res

    def assertion_result(self):
        # 实例化res，将res做断言
        res = self.send_request()
        assert eval(self.test_dict['expected'])
        test_result = "pass"
        self.test_data_path.write_data(int(self.test_dict['case_id'])+1, 9, test_result)







