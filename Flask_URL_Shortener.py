from flask import Flask, request, render_template, redirect, url_for
import random


app = Flask(__name__)
res = None
url_dct = {}


@app.route('/')
def index():
    shr_url = None
    if request.args.get("post_red"):
        shr_url = request.args.get("post_red")
    return render_template("shr.html", shr_url=shr_url, url_dct=url_dct)


@app.route('/res/', methods=["POST"])
def shorter():
    global res
    if request.form["url"]:
        res = rand_str(request.form["url"])
    else:
        res = None
    return redirect(url_for("index", post_red=res))


@app.route('/brk_app/<sh_url>')
def redir(sh_url):
    if sh_url in url_dct:
        return redirect(url_dct[sh_url])
    else:
        return redirect(url_for("index"))


def rand_str(req_url):
    global url_dct
    alph = list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    while 1:
        random.shuffle(alph)
        shr_url = ''.join([random.choice(alph) for x in range(7)])
        if shr_url not in url_dct:
            url_dct[shr_url] = req_url
            return shr_url


if __name__ == '__main__':
    app.run()
