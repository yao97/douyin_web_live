from config.helper import config
from browser.edge import EdgeDriver
from browser.chrome import ChromeDriver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Type
    from browser.IDriver import IDriver


class BrowserManager():
    _mapping: "dict[str, Type[IDriver]]" = {
        "chrome": ChromeDriver,
        "edge": EdgeDriver
    }

    def __init__(self):
        _config = config()["webdriver"]["use"]
        if _config not in self._mapping:
            raise Exception("不支持的浏览器")
        self._driver = self._mapping[_config]()

    @property
    def driver(self):
        return self._driver
