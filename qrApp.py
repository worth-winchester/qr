import qrcode
import json
import os
from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=['GET'])
def update():
    cmd = request.args.get("cmd")
    if cmd != None:
        cmdDict = {
            "cmd": cmd
        }
        cmdJson = json.dumps(cmdDict)
        with open("test.txt", "w") as f:
            f.write(cmd)
        filename = "qrImage.png"
        img = qrcode.make(cmdJson)
        img.save(filename)
        os.system("rm static/images/qrImage.png")
        os.system("mv qrImage.png static/images/")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
