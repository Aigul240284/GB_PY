d={}
d=dict()
d['q']='qwerty'
print(d)
d['w']="werty"
print(d)
print(d["w"])
for i in d:
    print(i)
    print("{}:{}".format(i,d[i]))
print(d.items())
for (k,v) in d.items():
    print(k,v)
    print(type(k))
    print(type(v))