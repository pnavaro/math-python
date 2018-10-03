def cipher(text, key):
    "Encrypt the `text` using the Caesar cipher technique. "
    s = ""
    for c in text:
        position = char_to_int(c)
        if position:
            s += int_to_char(position+key)
        else:
            s += c
        
    return s

cipher('s kw k zidryxscdk!', 42)