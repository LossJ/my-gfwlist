import os
import base64

import requests


url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
content = requests.get(url).text
decoded_content = base64.b64decode(content).decode("utf-8")

mylist_path = "./mylist.txt"
mylist = ""
with open(mylist_path, "r") as f:
    mylist = f.read()

decoded_content = decoded_content + "\n" + mylist
encoded_content = base64.b64encode(decoded_content.encode("utf-8"))
with open("./gfwlist.txt", "wb") as f:
    f.write(encoded_content)

