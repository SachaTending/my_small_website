import os, gunicorn, sitemain, sys
from flask import Flask, send_file
from datetime import datetime
from gunicorn import SERVER_SOFTWARE as gver

pcount: int = 0

slinks = "<p>Site links: <a href=\"/\">index</a>, <a href=\"/stats\">stats</a>, <a href=\"/wtv\">wtv stuff</a></p>"

print("pls wait while im starting.")
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

def general_gen(*args, **kwargs):
    output = sitemain.gen_templ(*args, **kwargs)
    output = slinks+output
    return output

@app.route("/stats")
def stats():
    return general_gen(
        "stats.html",
        uptime=os.popen("uptime").read()
    )

@app.route("/wtv")
def wtv():
    return general_gen("wtv.html")

@app.route("/data/<file>")
def data(file: str):
    return send_file(cwd+"data/"+file)
@app.route("/")
def index():
    return general_gen(
        "index.html", 
        peoples_joined=get_pcount(), 
        serv_time=datetime.now(),
        gver=gver,
        pyver=sys.version
    )
print("server ready!")