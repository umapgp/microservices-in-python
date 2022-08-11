from flask import Flask,jsonify, render_template
import socket

app = Flask(__name__)

# Function to fetch host name and ip
def fetchdetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/details")
def details():
    hostname, ip = fetchdetails()
    return render_template('index.html', HOST=hostname, IP=ip)