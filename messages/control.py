import time

from messages.base import Base
from protobuf import message_pb2


class ControlMessage(Base):
    def __init__(self):
        self.instance = message_pb2.ChatMessage()

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【直播间信息】'
