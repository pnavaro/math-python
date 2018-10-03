def cipher(text, key=0):
    "Encrypt the `text` using the Caesar cipher technique."
    
    def shift(c):
        if c.isalpha():
            i = alphabet.index(c)
            return alphabet[(i+key)%26]
        else:
            return c
    
    return "".join(map(shift, text))
        
cipher('s kw k zidryxscdk!', 42)