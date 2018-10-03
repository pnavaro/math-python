def char_to_int(c):
    if c.isalpha():
        for i, a in enumerate(alphabet):
            if c == a:
                return i

char_to_int("e"), char_to_int(" ")