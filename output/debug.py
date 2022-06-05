import os
import time
import traceback
from output.IOutput import IOutput


class DebugWriter(IOutput):
    def other_output(self, message_type: str, message_raw: bytes):
        if not os.path.isdir(os.path.join("", "debug")):
            os.makedirs(os.path.join("", "debug"))
        if not os.path.isdir(os.path.join("", "debug", message_type)):
            os.makedirs(os.path.join("", "debug", message_type))
        with open(os.path.join("", "debug", message_type, str(time.time())), "wb") as f:
            f.write(message_raw)

    def error_output(self, message_type: str, message_raw: bytes, exception: Exception):
        if not os.path.isdir(os.path.join("", "error")):
            os.makedirs(os.path.join("", "error"))
        if not os.path.isdir(os.path.join("", "error", message_type)):
            os.makedirs(os.path.join("", "error", message_type))
        ts = time.time()
        with open(os.path.join("", "error", message_type, str(ts)), "wb") as f:
            f.write(message_raw)
        traceback.print_exc(file=open(os.path.join("", "error", message_type, str(ts)) + ".exc", "w", encoding="UTF-8"))


