import time
from queue import SimpleQueue

MESSAGE_QUEUE: "SimpleQueue[MessagePayload]" = SimpleQueue()


class MessagePayload(object):
    def __init__(self, body: bytes, timestamp: str = ""):
        self.request_timestamp = timestamp
        self.body = body
        self.curretnt_timestamp = time.time()
