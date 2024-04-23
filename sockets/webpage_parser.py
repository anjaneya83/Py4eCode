# Web page parsering using urllib
import urllib.request, urllib.parse, urllib.error

fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fh:          # line is an array of bytes so we need to decode it into utf-8 using decode()
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
print(counts)