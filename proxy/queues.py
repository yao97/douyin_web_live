from queue import SimpleQueue
from proxy.common import MessagePayload

MESSAGE_QUEUE: "SimpleQueue[MessagePayload]" = SimpleQueue()
