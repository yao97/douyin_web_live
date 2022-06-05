import json

from flask import Flask, request, Response
from handler.common import MESSAGE_QUEUE, MessagePayload
import logging
# 不要日志，当它不存在
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.post("/message")
def message_from_mitmproxy():
    payload = MessagePayload(request.data, request.headers.get("X-MITM-TS", ""))
    MESSAGE_QUEUE.put(payload)
    return Response(status=204)


@app.post("/user_info")
def user_info_from_mitmproxy():
    try:
        user_info = json.loads(request.data)
    except json.JSONDecodeError:
        return Response(status=403)
    print(user_info)
    if "user" not in user_info:
        # 这个请求有问题
        return Response(status=403)
    user = user_info['user']
    #有用的信息
    {
        # 抖音加密的用户id，也就是url上的id字符串
        "sec_user_id": user.get('sec_uid', ""),
        # 用户真实的数字id
        "user_id": user.get('uid', 0),
        # 开播状态，1是开播了
        "live_status": user.get('live_status', 0),
        # 和西瓜视频一样，每次开播，room_id都会变化，需要动态拿取
        "room_id": user.get('room_id', 0),
        "nickname": user.get('nickname', ""),
        # 多平台粉丝数，包含西瓜视频等关联字节公司下的账号粉丝总数
        "mp_fans_count": user.get('mplatform_followers_count', 0),
        # 近期加的归属地
        "ip_location": user.get('ip_location', ""),
    }
    return Response(status=204)
