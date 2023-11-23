a={1:2,3:4,"list":[1,23],"dict":{1:2}}
a

a['list']
a.get('list')
print(a.get("li"))
a.get('li',0)
a.keys()
a.values()
a.items()

for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

"list" in a

2 in a

a
a['t']=(1,2,3)
a
a[1]=10
a
b={3:5,'the':4,2:100}
a.update(b)
a
a.pop('t')
a
del a[1]
a
a.clear()
a
del a
a


