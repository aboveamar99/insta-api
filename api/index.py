import json
import requests

def handler(request):

    try:
        body = json.loads(request["body"])
        url = body.get("url")

        api = "https://tera.backend.live/allinone"

        r = requests.post(api, json={"url": url})

        data = r.json()

        video = data["video"][0]["video"]
        thumbnail = data["video"][0]["thumbnail"]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "video": video,
                "thumbnail": thumbnail
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
