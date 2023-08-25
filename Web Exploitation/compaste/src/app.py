import random
import string
from flask import Flask, render_template, request, redirect

# This is a C library
import fio

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


def gen_id(size: int = 6, chars: string = string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def get_content(fname: str | None) -> str:
    if not fname:
        return ""

    if any(c in fname for c in string.punctuation):
        return "can't do!"

    try:
        return "".join(
            map(lambda x: x.decode(), fio.read_file("files/" + fname + ".txt"))
        )
    except:
        return "error occured, not found?"


@app.get("/view")
def view_paste():
    paste_id = request.args.get("id")
    content = get_content(paste_id)

    return render_template("paste.html", paste_id=paste_id, content=content)


@app.post("/new")
def new_paste():
    content = request.form.get("content")
    if not content:
        return redirect("/")

    id = gen_id(32)
    with open(f"files/{id}.txt", "w") as f:
        f.write(content)

    return redirect(f"/view?id={id}")


@app.route("/")
def home():
    fname = request.args.get("fname")
    return render_template(
        "index.html",
        content=get_content(fname),
    )
