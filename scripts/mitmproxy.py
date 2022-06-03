# ! IMPORT ! make sure you ran mitmproxy with this script, 
# eg: `/path/to/mitmproxy -s mitmproxy.py`
import time
from mitmproxy import http
import re
import requests
import base64

session = requests.session()


class Writer:
    def websocket_message(self, flow: http.HTTPFlow):
        re_c = re.search('webcast\d-ws-web-.*\.douyin\.com', flow.request.host)
        if re_c:
            message = flow.websocket.messages[-1].content
            session.post("http://127.0.0.1:5000/message", data=message, headers={
                "X-MITM_TS": str(time.time()),
                "X_REFERER": flow.request.host
            }, timeout=(1, 1))


addons = [Writer()]
