from output import IOutput


class DebugWriter(IOutput):
    def other_output(self, message_type: str, message_raw: bytes):
        print(message_type)
