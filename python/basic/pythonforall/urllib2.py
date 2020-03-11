# read readline readlines close
# geturl info
# headers

import urllib

try:
    f = urllib.urlopen("http://www.python.org")
    print(f.read())
except expression as identifier:
    pass