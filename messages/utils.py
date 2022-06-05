import os

from messages.control import ControlMessage
from messages.fansclub import FansclubMessage
from protobuf import message_pb2
from protobuf import wss_pb2
import gzip
from messages.member import MemberMessage
from messages.like import LikeMessage
from messages.roomuserseq import RoomUserSeqMessage
from messages.gift import GiftMessage
from messages.social import SocialMessage
from messages.chat import ChatMessage

from colorama import init, Fore
# define colors
RED   = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
RESET = Fore.RESET
init()

def unpackMsgBin(filepath):
    response = message_pb2.Response()
    wss = wss_pb2.WssResponse()
    try:
        with open(filepath, 'rb') as f:
            path_content = f.read()
            wss.ParseFromString( path_content )
            decompressed = gzip.decompress(wss.data)
            response.ParseFromString(decompressed)
            decodeMsg(response.messages)
    except Exception as e:
        os.remove(filepath)
        pass
    finally:
        os.remove(filepath)

def decodeMsg(messages):
    for message in messages:
        try:
            if message.method == 'WebcastMemberMessage':
                member_message = MemberMessage()
                member_message.set_payload(message.payload)
                member_message.persists()
                
                print(f"\n{RED}[+] {member_message} {RESET}")

            elif message.method == 'WebcastSocialMessage':
                social_message = SocialMessage()
                social_message.set_payload(message.payload)
                social_message.persists()

                print(f"\n{GREEN}[+] {social_message} {RESET}")

            elif message.method == 'WebcastChatMessage':
                chat_message = ChatMessage()
                chat_message.set_payload(message.payload)
                chat_message.persists()

                print(f"\n{BLUE}[+] {chat_message} {RESET}")

            elif message.method == 'WebcastLikeMessage':
                like_message = LikeMessage()
                like_message.set_payload(message.payload)
                like_message.persists()

                print(f"\n{CYAN}[+] {like_message} {RESET}")

            elif message.method == 'WebcastGiftMessage':
                gift_message = GiftMessage()
                gift_message.set_payload(message.payload)
                gift_message.persists()

                print(f"\n{MAGENTA}[+] {gift_message} {RESET}")

            elif message.method == 'WebcastRoomUserSeqMessage':
                room_user_seq_message = RoomUserSeqMessage() 
                room_user_seq_message.set_payload(message.payload)
                room_user_seq_message.persists()

                print(f"\n{YELLOW}[+] {room_user_seq_message} {RESET}")

            elif message.method == 'WebcastFansclubMessage':
                fansclub_message = FansclubMessage()
                fansclub_message.set_payload(message.payload)
                fansclub_message.persists()

                print(f"\n{RED}[+] {fansclub_message} {RESET}")

            elif message.method == 'WebcastControlMessage':
                control_message = ControlMessage()
                control_message.set_payload(message.payload)
                control_message.persists()

                print(f"\n{CYAN}[+] {control_message} {RESET}")

        except Exception as e:
            print(e)
