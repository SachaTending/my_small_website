import os, gunicorn, sitemain, sys
from flask import Flask, send_file
from datetime import datetime
from gunicorn import SERVER_SOFTWARE as gver
from base import plugs_init, general_gen, gen_path
import base

pcount: int = 0

slinks = f"<p>Site links: <a href=\"{gen_path('/')}\">index</a>, <a href=\"{gen_path('/stats')}\">stats</a>, <a href=\"{gen_path('/wtv')}\">wtv stuff</a></p>"
base.slinks = slinks
print("pls wait while im starting.")
plugs = plugs_init()
for i in plugs: i.pre_init()
print(f"Gunicorn version: {gunicorn.SERVER_SOFTWARE}")
print("building app...")
cwd = os.getcwd()
if not cwd.endswith("/"):
    cwd += "/"
app: Flask = sitemain.gen_app("site", templ=cwd+"templates")
sitemain.gen_site(app)

def get_pcount() -> int:
    global pcount
    pcount += 1
    return str(pcount)

@app.route(gen_path("/stats"))
def stats():
    return general_gen(
        "stats.html",
        uptime=os.popen("uptime").read()
    )

@app.route(gen_path("/wtv"))
def wtv():
    return general_gen("wtv.html")

@app.route(gen_path("/data/<file>"))
def data(file: str):
    return send_file(cwd+"data/"+file)
@app.route(gen_path("/"))
def index():
    return general_gen(
        "index.html", 
        peoples_joined=get_pcount(), 
        serv_time=datetime.now(),
        gver=gver,
        pyver=sys.version
    )
for i in plugs: i.app_setup(app)
for i in plugs: i.post_init()
print("server ready!")