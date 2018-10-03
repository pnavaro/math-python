
from string import ascii_lowercase as lower
from string import ascii_uppercase as upper

def cipher(filename, key=0):
    with open(filename,"r") as f:
        text = f.read()
    a = { c:lower[(i+key)%26] for (i,c) in enumerate(lower)}
    A = { c:upper[(i+key)%26] for (i,c) in enumerate(upper)}
    table = str.maketrans(dict(a,**A))
    
    with open(filename,"w") as f:
        f.write(text.translate(table))
    
cipher("sample.txt",1)