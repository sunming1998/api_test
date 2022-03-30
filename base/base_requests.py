import requests
import json
from requests_toolbelt import MultipartEncoder

class MyRequests:
    def send_requests(self,method,url,data,headers = None):
        if method.lower == "get":
            res = requests.get(url=url,params=data)
        else:
            data = json.dumps(eval(data))
            headers = eval(headers)
            res = requests.post(url=url,data=data,headers = headers)
        return res

