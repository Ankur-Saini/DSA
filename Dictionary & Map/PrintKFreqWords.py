s="this is a word string having many many word"
k=2

words=s.split()
words

d={}
for w in words:
    if w in d:
        d[w]=d[w]+1
    else:
        d[w]=1

d={}
for w in words:
    d[w]=d.get(w,0)+1

for w in d:
    if d[w]==k:
        print(w)

def printKFreqWords(s,k):
    words=s.split()
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)

printKFreqWords(s,k)
