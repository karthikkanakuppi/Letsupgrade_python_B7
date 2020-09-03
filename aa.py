# LetsUpgrade Python Batch-7 assignmet day2

### List ###
a=[21,34,2,32,2]
b=['a',"cat"]
c=[1,2,34,4]
a.append(23) ##adding elememt at the end of the list
print(a)
a.sort()   ##sorting
print(a)
a.insert(2,111) ## inserting an element at particular index
print(a)
a.extend(b)
print(a)
a.index(2)
print(a)
print(sum(c))
print(max(c))
print(min(c))

### Dictionary ###
d={1:"A",2:"B",3:"C"}
print(d)
print(d.get(1)) ## accessing element
print(d.pop(1))
print(d.popitem()) ##removes an arbitrary elemen
print(d.keys())
print(d.values())

### Sets ###
m=set(["a","b","c"])
print(m)
m.add("d")
print(m)
m.remove("d")
print(m)
print(m.pop())
m.clear()
print(m)

### Tuples ###

q=(1,12,2,234,2)
r=("a","b")
t=q+r
print(t)
del(r)
print(len(t))
print(max(q))
print(min(q))
print(sorted(q))
print(q.count(2))


### Strings ###


strg="My name is LetsUpgrade"
strg1=str.swapcase(strg)
print(strg1)
st=str.strip(strg)
print(st)
stt=str.split(st)
print(stt)
print(str.casefold(st))
print(str.encode(st))

