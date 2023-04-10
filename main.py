import requests
import sys
import json

# email = "test@gmail.com"
email = sys.argv[1]
h = {
"User-Agent": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile DuckDuckGo/5 Safari/537.36"
}

r = requests.get(f"https://search.illicit.services/records?wt=json&emails={email}", headers=h)

if r.status_code == 200:
    with open(f"out_{email}.json", "w") as file:
        json.dump(r.json(), file)
    print("Done.")
else:
    print("Probably blocked.")
