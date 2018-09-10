s1 = "pascal obispo"
s2 = "pablo picasso"

assert len(s1) == len(s2)

print(s1 + " is an anagram of " + s2 + "?")
# solution with loops
for c1 in s1:
    for c2 in s2:
        if c1 == c2:
            s1 = s1.replace(c1, "", 1)
            s2 = s2.replace(c2, "", 1)

print(len(s1) == len(s2))

# solution with lists
s1 = sorted(list("pascal obispo"))
s2 = sorted(list("pablo picasso"))
print(s1 == s2)
