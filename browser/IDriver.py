import contextlib


class IDriver():
    def new_tab(self) -> str:
        ...

    def get_current_tab(self) -> str:
        ...

    def change_tab(self, tab_handler: str):
        ...

    def open_url(self, url: str, tab_handler: str = ""):
        ...

    @contextlib.contextmanager
    def op_tab(self, tab_handler: str):
        cur_handle = self.get_current_tab()
        if tab_handler == "":
            tab_handler = cur_handle
        try:
            self.change_tab(tab_handler)
            yield self
        finally:
            self.change_tab(cur_handle)

    def refresh(self, tab_handler: str = ""):
        ...

    def screenshot(self, tab_handler: str = "") -> str:
        ...
