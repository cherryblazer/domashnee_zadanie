import collections
from typing import Collection
import requests
import re

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
line = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)

res = requests.get(url)

con = list(map(str, res.text.split('\n')))

ans = []
ips = set()

for i in con:
    data = re.search(line, i)
    if data:
        datadict = data.groupdict()
        ip = datadict["ipaddress"]
        ans.append(ip)
        ips.add(ip)

cnt = collections.Counter(ans)
mx = -1
spammer = ""
for i in ips:
    if mx < cnt[i]:
        mx = cnt[i]
        spammer = i
print(spammer)