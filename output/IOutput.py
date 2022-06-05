from messages.base import Base
from messages.chat import ChatMessage
from messages.control import ControlMessage
from messages.gift import GiftMessage
from messages.like import LikeMessage
from messages.member import MemberMessage
from messages.roomuserseq import RoomUserSeqMessage
from messages.social import SocialMessage


class IOutput():
    def output(self, message_type: str, message_obj: Base):
        ...

    def chat_output(self, message: ChatMessage):
        ...

    def like_output(self, message: LikeMessage):
        ...

    def member_output(self, message: MemberMessage):
        ...

    def social_output(self, message: SocialMessage):
        ...

    def gift_output(self, message: GiftMessage):
        ...

    def userseq_output(self, message: RoomUserSeqMessage):
        ...

    def control_output(self, message: ControlMessage):
        ...

    def other_output(self, message_type: str, message_raw: bytes):
        ...

    def error_output(self, message_type: str, message_raw: bytes, exception: Exception):
        ...