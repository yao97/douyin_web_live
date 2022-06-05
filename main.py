import threading
import subprocess

from config.helper import config
from handler.http_server import app
from browser.manager import init_manager as init_browser_manager
from output.manager import OutputManager

if __name__ == '__main__':
    mitmproxy_process = subprocess.Popen([
        config()["mitm"]["bin"], "-s", "./proxy_script.py", "-q",
        "--listen-host", config()["mitm"]["host"], "--listen-port", str(config()["mitm"]["port"])
    ])
    api_thread = threading.Thread(target=app.run, args=(config()["http"]["host"], config()["http"]["port"],))
    api_thread.start()
    browser_manager = init_browser_manager()
    output_manager = OutputManager()
    output_manager.start_loop()
    api_thread.join()
