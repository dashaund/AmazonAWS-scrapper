import os
import re

url = ""

f = open("sample.txt", "r")
for x in f:
    url = x.rstrip()
    regex = r"\/(.*)\/(.*)\/(.*)\."
    match = re.search(regex, x)
    i = match.group(3)
    print(url)
    print(i)
    os.system("curl -X GET "+url+" --output %s.png" % i)