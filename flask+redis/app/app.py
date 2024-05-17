from redis import Redis
import urllib
from flask import Flask, request

redis = Redis(host='myRedis', port=6379)

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/ssrf")
def ssrf():
    url = request.args.get("url")
    print(url)
    if url:
        info = urllib.request.urlopen(url)
        res = info.read()
        return res
    return "?url="


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
