#!/usr/bin/python3

from flask import Flask, request, render_template
from requests import post
from requests.exceptions import ConnectionError
from xml.parsers.expat import ExpatError

app = Flask(__name__)

SERVER_HOST = "172.16.0.2" # v2gdecoder-container
SERVER_PORT = 9000

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        try:
            data = request.form.get('exi_msg')
            if data is not None:
                result = decode_to_xml(data, "EXI")
                # xml_data = xml.dom.minidom.parseString(result)
                # xml_convert = xml_data.toprettyxml()
                if not result:
                    return render_template("index.html", data=data, result="Error")
                return render_template("index.html", data=data, result=result)
        except ExpatError:
            return render_template("index.html", data=data, result="No EXI Format")

def decode_to_xml(data, type):
    try:
        service = f"http://{SERVER_HOST}:{SERVER_PORT}"
        res = post(service, headers={"Format":type}, data=data)
        print(res, res.text)
        return res.text

    except ConnectionError:
        return False

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)
