import requests
import json
from requests_toolbelt import MultipartEncoder


class MyRequests:
    # 创建一个发起请求的类，填必传参数
    def send_requests(self, method, url, data, headers=None):
        res = None
    # 做判断，是否为get请求
        if method.lower() == "get":
            res = requests.get(url=url,params=data)
    # 做判断，是否为post请求
        elif method.lower() == "post":
    # 用eval方法转换一下格式，毕竟从Excel里面取出来的都是str
            data = json.dumps(eval(data))
            headers =eval(headers)
    # 这里做个判断，请求头是否为json格式，如果是就传post，如果不是，则吧请求头写死，传其他格式
            if headers =={'Content-Type':'application/json'}:
                    res = requests.post(url=url, data=data, headers=headers)
            else:
                    data= MultipartEncoder(fields=data)
                    res = requests.post(url=url, data=data, headers={'Content-Type': data.content_type})
        return res

