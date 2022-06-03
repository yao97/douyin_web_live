from flask import Flask, request, Response
from handler.common import MESSAGE_QUEUE
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.post("/message")
def message_from_mitmproxy():
    payload = request.data
    MESSAGE_QUEUE.put(payload)
    return Response(status=204)