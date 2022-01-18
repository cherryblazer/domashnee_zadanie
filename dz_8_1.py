import collections
from typing import Collection
import requests
import re

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

line = re.compile(
    r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""",
    re.IGNORECASE)

res = requests.get(url)

con = list(map(str, res.text.split('\n')))

ans = []
ips = set()

for i in con:
    data = re.search(line, i)
    if data:
        datadict = data.groupdict()
        ip = datadict["ipaddress"]
        datetimestring = datadict["dateandtime"]
        url = datadict["url"]
        bytessent = datadict["bytessent"]
        referrer = datadict["refferer"]
        useragent = datadict["useragent"]
        status = datadict["statuscode"]
        method = data.group(6)

        ans.append((ip, datetimestring, method, url, status, bytessent))

print(ans)