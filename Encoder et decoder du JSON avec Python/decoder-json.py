import json

txt = '{"Image": {"Width": 800, "Height": 500, "Title": "View from 15th Floor", "Thumbnail": {"Url": "http://www.example.com/image/481989943", "Height": 125, "Width": 100}, "Animated": false, "Comment": null, "Evaluation": 4.72, "IDs": [116, 943, 234, 38793]}}'

obj = json.loads(txt)

print(obj["Image"])
