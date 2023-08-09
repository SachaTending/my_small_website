import glob
import sys
from flask import Flask
import sitemain
from os.path import join as pathjoin
from config import SITE_PREFIX

slinks: str
class Plugin:
    id: str
    name: str
    def post_init(self): return
    def pre_init(self): return
    def app_setup(self, app: Flask): return
    def slinks_patch(self, slinks: str) -> str: return slinks

def general_gen(*args, **kwargs):
    output = sitemain.gen_templ(*args, **kwargs)
    output = slinks+output
    return output

def plugs_init() -> list[Plugin]:
    pl = []
    for i in glob.glob("plugins/*"):
        if i.endswith(".py"):
            i = i.removesuffix(".py")
        i = i.removeprefix("./plugins").removeprefix("plugins").removeprefix("/").removeprefix("\\")
        pl.append(i)
    sys.path.append("plugins")
    plugs: list = []
    for i in pl:
        try: imp = __import__(i)
        except Exception as e: print(f"Error while loading {i}: {e}");continue
        for a in dir(imp):
            try:
                if issubclass(getattr(imp, a), Plugin):
                    plugs.append(getattr(imp, a)())
            except: pass
    sys.path.remove("plugins")
    for i in plugs:
        if isinstance(i, Plugin): plugs.remove(i)
    print("Loaded: ", end="")
    for i in plugs:
        try: print(f"{i.name}({i.id})", end=", ")
        except: print(f"{i}", end=", ")
    print()
    return plugs

def gen_path(path: str):
    if path == "/":
        out = "/site"
        return out
    if path.startswith("/"): path = path.removeprefix("/")
    out = SITE_PREFIX + path
    print(out)
    return out