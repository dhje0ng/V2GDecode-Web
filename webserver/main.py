#!/usr/bin/python3

from flask import Flask, request, render_template
from requests import post
from requests.exceptions import ConnectionError
from xml.parsers.expat import ExpatError

app = Flask(__name__)

ISO15118_HOST = "172.16.0.4" # v2gdecoder-container(ISO15118)
DIN70121_HOST = "172.16.0.2" # v2gdecoder-container(ISO15118)
SERVER_PORT = 9000

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        try:
            data = request.form.get('exi_msg')
            decode_type = request.form.get('decode_type')
            if decode_type == "DIN-70121" and data is not None:
                result = decode_to_xml_iso15118(data, "EXI")
                if not result:
                    return render_template("index.html", data=data, decode_type=decode_type, result="Error")
                return render_template("index.html", data=data, decode_type=decode_type, result=result)
                
        except ExpatError:
            return render_template("index.html", data=data, decode_type=decode_type, result="No EXI Format")

def decode_to_xml_iso15118(data, type):
    try:
        service = f"http://{ISO15118_HOST}:{SERVER_PORT}"
        res = post(service, headers={"Format":type}, data=data)
        return res.text

    except ConnectionError:
        return False

def decode_to_xml_iso15118(data, type):
    try:
        service = f"http://{DIN70121_HOST}:{SERVER_PORT}"
        res = post(service, headers={"Format":type}, data=data)
        return res.text

    except ConnectionError:
        return False

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)
