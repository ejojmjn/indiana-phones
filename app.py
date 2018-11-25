from wifi import Cell, Scheme
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def landingpage(path):
  return "Hi there"

@app.route("/wifi")
def wifi():
  cells = Cell.all('wlan0')
  str = ''
#  for c in cells:
#    str = str + c.ssid + '\n'
  networks = [c.ssid for c in cells]
  return render_template('wifi.html', networks=networks)


@app.route("/connect/<string:ssid>", methods=["POST"])
def connect(ssid):
  print("POST asking to connect to %s" % ssid)
  print(request.form['password'])
  return "Connected to " + ssid

