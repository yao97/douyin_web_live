from config.helper import config
from output.IOutput import IOutput
from typing import IO
from datetime import datetime
import time


class XMLWriter(IOutput):
    """
    可输出与B站弹幕姬兼容的xml弹幕格式，可用于转成ass字幕
    """

    def __init__(self):
        self._file_mappings: "dict[str, IO[str]]" = {}
        self.time_mappings: "dict[str, float]" = {}
        self._file_name_pattern: "str" = config()['output']['xml']['file_pattern'] 
 
    def _get_fd_by_room_id(self, room_id: str) -> IO[str]:
        if room_id in self._file_mappings:
            return self._file_mappings[room_id]
        cur_ts = time.time()
        fd = open(self._file_name_pattern.format_map({
            "room_id": room_id,
            "ts": cur_ts
        }), "w", encoding="UTF-8")
        self._file_mappings[room_id] = fd
        self.time_mappings[room_id] = cur_ts
        return fd

    def _close_fd_by_room_id(self, room_id: str):
        if room_id in self._file_mappings:
            fd = self._file_mappings[room_id]
            if not fd.closed:
                fd.close()
            del self._file_mappings[room_id]
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
# 弹幕模块
    def chat_output(self, message):
        fd = self._get_fd_by_room_id(message.room_id)
        if fd is None:
            return
        cur_time = time.time()
    # Unix转时间
        _c = """<d timestamp="{}" user="{}" user_id="{}" content="{}"></d>\r\n""".format(
        datetime.fromtimestamp(cur_time).strftime('%Y-%m-%d %H:%M:%S'),
        message.user().nickname,
        message.user().id,
        message.content
        )
        fd.write(_c)
        fd.flush()
# 进入模块
    def member_output(self, message):
        fd = self._get_fd_by_room_id(message.room_id)
        if fd is None:
            return
        cur_time = time.time()
        # 将当前时间戳转换为datetime对象
        dt = datetime.fromtimestamp(cur_time)
        # 将datetime对象转换为指定格式的字符串
        time_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        _c = """<into time="{}" user="{}" user_id="{}"></into>\r\n""".format(
            time_str, message.user().nickname, message.user().id
        )
        fd.write(_c)
        fd.flush()
# 礼物模块
    # def gift_output(self, message):
    #     fd = self._get_fd_by_room_id(message.room_id)
    #     if fd is None:
    #         return
    #     cur_time = time.time()
    #     _c = """<gift ts="{:.2f}" user="{}" user_id="{}" giftname="{}" giftcount="{}"></gift>\r\n""".format(
    #         self._get_bias_ts_by_room_id(message.room_id, cur_time),
    #         message.user().nickname,message.user().id, message.gift.name, message.instance.repeatCount
    #     )
    #     fd.write(_c)
    #     fd.flush()



    def terminate(self):
        print("保存所有弹幕文件中...")
        # copy
        _rooms = [i for i in self._file_mappings.keys()]
        for _room_id in _rooms:
            self._close_fd_by_room_id(_room_id)
        print("保存完毕")
