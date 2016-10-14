import urllib.request
import re
from urllib.error import URLError
try:
    response  = urllib.request.urlopen("http://www.weather.com.cn/weather1d/101280601.shtml")
except URLError as e:
    print("Error:", e.reason)
html = response.read()
reg_html = re.compile(r'id="hidden_title"')
found_temperature = reg_html.search(html.decode("utf8"))
# print(html.decode("utf8"))
print(html.decode("utf8")[found_temperature.end():found_temperature.end()+34])