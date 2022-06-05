from output.IOutput import IOutput
from typing import IO
import time


class XMLWriter(IOutput):
    """
    可输出与B站弹幕姬兼容的xml弹幕格式，可用于转成ass字幕
    """
    def __init__(self):
        self.file_mappings: "dict[str, IO[str]]" = {}
        self.time_mappings: "dict[str, float]" = {}

    def _get_fd_by_room_id(self, room_id: str) -> IO[str]:
        if room_id in self.file_mappings:
            return self.file_mappings[room_id]
        fd = open(f"{room_id}_{time.time()}.xml", "w", encoding="UTF-8")
        self.file_mappings[room_id] = fd
        self.time_mappings[room_id] = time.time()
        return fd

    def _close_fd_by_room_id(self, room_id: str):
        if room_id in self.file_mappings:
            fd = self.file_mappings[room_id]
            if not fd.closed:
                fd.close()
            del self.file_mappings[room_id]
        if room_id in self.time_mappings:
            del self.time_mappings[room_id]

    def control_output(self, message):
        # 下播了
        self._close_fd_by_room_id(message.room_id)

    def _get_bias_ts_by_room_id(self, room_id: str, cur_ts: float = 0):
        if cur_ts == 0:
            cur_ts = time.time()
        if room_id not in self.time_mappings:
            return 0
        return cur_ts - self.time_mappings[room_id]

    def chat_output(self, message):
        fd = self._get_fd_by_room_id(message.room_id)
        if fd is None:
            return
        cur_time = time.time()
        _c = """<d p="{:.2f},1,24,16777215,{:.0f},0,{},0" user="{}">{}</d>\r\n""".format(
            self._get_bias_ts_by_room_id(message.room_id, cur_time),
            cur_time*1000, message.user().id, message.user().nickname, message.content
        )
        fd.write(_c)

    def gift_output(self, message):
        fd = self._get_fd_by_room_id(message.room_id)
        if fd is None:
            return
        cur_time = time.time()
        _c = """<gift ts="{:.2f}" user="{}" giftname="{}" giftcount="{}"></gift>\r\n""".format(
            self._get_bias_ts_by_room_id(message.room_id, cur_time),
            message.user().nickname, message.gift.name, message.instance.repeatCount
        )
        fd.write(_c)
