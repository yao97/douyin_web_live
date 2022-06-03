import os

from handler.common import MESSAGE_QUEUE
from protobuf import message_pb2
from protobuf import wss_pb2
import gzip
from messages.member import MemberMessage
from messages.like import LikeMessage
from messages.roomuserseq import RoomUserSeqMessage
from messages.gift import GiftMessage
from messages.social import SocialMessage
from messages.chat import ChatMessage
from output import OUTPUTER

def loop_queue():
    while True:
        message = MESSAGE_QUEUE.get()
        if type(message) == str:
            message = message.encode("UTF-8")
        try:
            response = message_pb2.Response()
            wss = wss_pb2.WssResponse()
            wss.ParseFromString(message)
            decompressed = gzip.decompress(wss.data)
            response.ParseFromString(decompressed)
            decodeMsg(response.messages)
        except Exception as e:
            # 发出去的信息无法解析
            pass

def decodeMsg(messages):
    for message in messages:
        try:
            if message.method == 'WebcastMemberMessage':
                member_message = MemberMessage()
                member_message.set_payload(message.payload)
                for output in OUTPUTER:
                    output.member_output(member_message)
            elif message.method == 'WebcastSocialMessage':
                social_message = SocialMessage()
                social_message.set_payload(message.payload)
                for output in OUTPUTER:
                    output.social_output(social_message)
            elif message.method == 'WebcastChatMessage':
                chat_message = ChatMessage()
                chat_message.set_payload(message.payload)
                for output in OUTPUTER:
                    output.chat_output(chat_message)
            elif message.method == 'WebcastLikeMessage':
                like_message = LikeMessage()
                like_message.set_payload(message.payload)
                for output in OUTPUTER:
                    output.like_output(like_message)
            elif message.method == 'WebcastGiftMessage':
                gift_message = GiftMessage()
                gift_message.set_payload(message.payload)
                for output in OUTPUTER:
                    output.gift_output(gift_message)
            elif message.method == 'WebcastRoomUserSeqMessage':
                room_user_seq_message = RoomUserSeqMessage() 
                room_user_seq_message.set_payload(message.payload)
                for output in OUTPUTER:
                    output.userseq_output(room_user_seq_message)
            else:
                ...
        except Exception as e:
            print(e)
