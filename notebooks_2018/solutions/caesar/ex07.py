def cipher(text, key=0):
    "Encrypt the `text` using the Caesar cipher technique. "
    text = list(text)
    for i, c in enumerate(text):
        if c.isalpha():
            j = alphabet.index(c)
            text[i] = alphabet[(j+key)%26]
    return "".join(text)

cipher('s kw k zidryxscdk!', 42)