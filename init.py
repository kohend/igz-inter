#!/usr/bin/env python3
print("Hello, Iguazio")

import http.client
import os
import json

conn = http.client.HTTPSConnection("api.openweathermap.org")

params = "id=293397&appid=" + os.environ["API_KEY"]

conn.request("GET", "/data/2.5/weather?" + params)

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))
weather = json.loads(data)
print(weather["weather"][0]["description"] + " " + "%.2fC" % (weather["main"]["temp"] - 273.15))