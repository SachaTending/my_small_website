from base import Plugin, Flask
from flask import request

class is_routing_plugin(Plugin):
    id = "is_routing"
    name = "Is routing?"
    def __init__(self) -> None:
        super().__init__()
        self.id = "is_routing"
        self.name = "Is routing?"
    def pre_init(self):
        return
    def app_setup(self, app: Flask):
        @app.before_request
        def patch():
            if "X-Forwarded-For" in request.headers or "/site" in request.path:
                #request.path = request.path.removeprefix("/site")
                pass
    def post_init(self):
        return