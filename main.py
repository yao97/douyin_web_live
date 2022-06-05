import threading
import subprocess

from config.helper import config
from handler.http_server import app
from handler.utils import loop_queue
from browser.manager import BrowserManager

if __name__ == '__main__':
    mitmproxy_process = subprocess.Popen([
        config()["mitm"]["bin"], "-s", "./proxy_script.py", "-q",
        "--listen-host", config()["mitm"]["host"], "--listen-port", str(config()["mitm"]["port"])
    ])
    api_thread = threading.Thread(target=app.run, args=(config()["http"]["host"], config()["http"]["port"],))
    api_thread.start()
    manager = BrowserManager()
    queue_thread = threading.Thread(target=loop_queue)
    queue_thread.start()
    queue_thread.join()

    
