import requests
import json

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from config.helper import config

def go(url):
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s:%s' % (config()['mitm']['host'], config()['mitm']['port']))

    # 2022-04-09 添加一个忽略证书
    chrome_options.add_argument('-ignore-certificate-errors')
    chrome_options.add_argument('-ignore -ssl-errors')
    chrome_options.add_argument('--incognito')

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = "%s:%s" % (config()['mitm']['host'], config()['mitm']['port'])
    proxy.ssl_proxy = "%s:%s" % (config()['mitm']['host'], config()['mitm']['port'])

    capabilities = DesiredCapabilities.EDGE
    proxy.add_to_capabilities(capabilities)

    with webdriver.Chrome(options=chrome_options,
                            desired_capabilities=capabilities,
                            executable_path=config()['webdriver']['bin']
                            ) as driver:
        wait = WebDriverWait(driver, 10)

        driver.implicitly_wait(24 * 60 * 60)

        driver.get(url)

        first_result = wait.until(presence_of_element_located((By.ID, "RENDER_DATA")))
        json_str = requests.utils.unquote(first_result.get_attribute("textContent"))
        json_obj = json.loads(json_str)

        roomInfo = json_obj['initialState']['roomStore']['roomInfo']
        print(roomInfo)

        wait.until(presence_of_element_located((By.CLASS_NAME, "oSu9Aw19")))
        