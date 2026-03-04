from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def insta():

    data = request.json
    url = data.get("url")

    api = "https://tera.backend.live/allinone"

    r = requests.post(api, json={"url": url})
    res = r.json()

    video = res["video"][0]["video"]
    thumbnail = res["video"][0]["thumbnail"]

    return jsonify({
        "video": video,
        "thumbnail": thumbnail
    })
