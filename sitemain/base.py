from flask import Flask, request, render_template
import time

def gen_app(name="app", templ="templates"):
    app = Flask(name, template_folder=templ)
    @app.errorhandler(404)
    def e404(a=None):
        url = request.url
        print(f"lol, someone opened wrong url({url})")
        ret = "<h1>hello, it seems like you opened worng url"
        if url != None:
            ret += f"({url})"
        ret += ", pls recheck</h1>"
        print(f"generated string: {ret}")
        return ret
    return app

def gen_templ(*argv, **kwargv):
    s = time.time()
    d = render_template(*argv, **kwargv)
    e = time.time()
    out = e - s
    if d.startswith("<!DOCTYPE HTML>"):
        d += f"<h5>lol, this template generated under {out} seconds</h5>"
    return d