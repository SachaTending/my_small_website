from base import Plugin, Flask, general_gen, gen_path
from flask import Response

class WebtvPOC(Plugin):
    id = 'bebtv_hacking'
    name = 'Webtv HTTP Vulnerable POC'
    def app_setup(self, app: Flask):
        @app.route(gen_path("/webtv_hacking/"))
        def webtv_hack():
            return general_gen("webtv_fucking.html")
        @app.route(gen_path("/webtv_hacking/poc"))
        def hack_it():
            return general_gen('boxhack.html')