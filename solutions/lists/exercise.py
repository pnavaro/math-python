s = "python LILLE 2018"
l = s.split(" ")
print(l)
l = l[:2] + ["april", 10] + l[2:]
print(l)
l[0] = l[0].capitalize()
print(l)
d = dict(course=l[0], month=l[2], day=l[3], year=l[4])
print(d.keys)
print(d.items())
d["place"] = l[1]
print(d)
