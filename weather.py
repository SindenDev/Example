import urllib
import json

f = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Cheltenham,uk")
weather = f.read()