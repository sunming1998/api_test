import requests
import json
from requests_toolbelt import MultipartEncoder


class MyRequests:
    def send_requests(self, method, url, data, headers=None):
        res = None
        if method.lower() == "get":
            res = requests.get(url=url,params=data)

        elif method.lower() == "post":
            data = json.dumps(eval(data))
            headers =eval(headers)

            if headers =={'Content-Type':'application/json'}:
                    res = requests.post(url=url, data=data, headers=headers)
            else:
                    data= MultipartEncoder(fields=data)
                    res = requests.post(url=url, data=data, headers={'Content-Type': data.content_type})
        return res

