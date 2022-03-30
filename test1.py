import pytest
import requests

class Test:
    def test_001(self):
        url = "https://www.baidu.com/"
        res = requests.get(url=url)
        print(res.text)
        assert 'www' in res.text


if __name__ == '__main__':
    pytest.main(['-v', 'test1.py'])