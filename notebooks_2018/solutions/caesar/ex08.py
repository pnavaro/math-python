def cipher(text, key=0):
    "Encrypt the `text` using the Caesar cipher technique. "
    a = alphabet
    return "".join((a[(a.index(c)+key)%26] if c.isalpha() else c for c in text))

cipher('s kw k zidryxscdk!', 42)