import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://ituens.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json()))

# json.dumps - allows to read JSON more comfortably
