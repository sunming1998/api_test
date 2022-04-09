import pytest
from base.base_readYaml import ReadYaml
from common.logger import Log
import requests
import json

@pytest.fixture(scope='class')
def login():
    # 获取用户id ，用户token的方法
    test_user = ReadYaml().read_yaml_data('test_usercase.yaml')
    test_user_phone = test_user['test_user']['phone'][0]
    test_user_password = test_user['test_user']['phone'][1]
    try:
        res = requests.post(url='http://api.kr-cell.net/login-register/login-by-phone',
                            headers = {'Content-Type': 'application/json'},
                             data =json.dumps({'phone':test_user_phone, 'password': test_user_password}))
        return  res.json()['userID'], res.json()['userKey']

    except Exception as e:
        Log().error('{}登录获取uid，token出错'.format(e))
        return 'None'

