def char_to_int(c):
    if c.isalpha():
        i = 0
        while alphabet[i] != c: # Don't forget the ':' character.
            i += 1              # The body of the loop is indented
        return i

char_to_int("e"), char_to_int(" ")