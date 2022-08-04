import http.client
import json

conn = http.client.HTTPSConnection("api.openweathermap.org")
payload = ''
headers = {}
conn.request("GET", "/data/2.5/weather?lat=34.2268&lon=77.5619&appid=26c344b47a21c83165b6a347ae957ed0", payload, headers)
res = conn.getresponse()
data = res.read()
d=json.loads(data.decode("utf-8"))
print(f""" the  weather condition of {d["name"]} is {d["weather"]["id"]}&{d["weather"]["description"]}&{d["weather"]["icon"]}""")
