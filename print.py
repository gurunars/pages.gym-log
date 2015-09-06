import os
import jinja2


with open("base.html") as fil:
    tpl = jinja2.Template(fil.read())

with open("index.html", "w") as fil:
    items = [item for item in sorted(os.listdir(os.path.curdir)) if item.endswith(".png")]
    fil.write(tpl.render(items=items))
