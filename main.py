import sys
import threading
import subprocess
from urllib.parse import urlparse

from config.helper import config
from handler.http_server import app
from handler.utils import loop_queue
from scripts import webdriver

if __name__ == '__main__':
    if len(sys.argv) == 1 or not urlparse(sys.argv[1]).scheme:
        print('Invalid url provided, please check...')
        sys.exit(1)
    api_thread = threading.Thread(target=app.run, args=(config()["http"]["host"], config()["http"]["port"],))
    api_thread.start()
    mitmproxy_process = subprocess.Popen([
        config()["mitm"]["bin"], "-s", "./scripts/mitmproxy.py", "-q",
        "--listen-host", config()["mitm"]["host"], "--listen-port", str(config()["mitm"]["port"])
    ])
    t = threading.Thread(target=webdriver.go, args=(sys.argv[1],))
    t.start()
    queue_thread = threading.Thread(target=loop_queue)
    queue_thread.start()
    queue_thread.join()

    
