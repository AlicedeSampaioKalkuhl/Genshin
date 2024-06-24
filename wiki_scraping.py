import pandas as pd 
from urllib.request import urlopen
import re
url = "https://genshin-impact.fandom.com/wiki/Character/List"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
start_index = html.find('<td><span class="item character newline">') + len('<span class="item character newline">')
end_index = html.find("</span></td>")
title = html[start_index:end_index]
print(title)

