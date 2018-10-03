def char_to_int(c):
    if c.isalpha():
        k = ord(c) - ord('a')
        return k
    
def int_to_char(n):
    return chr(ord('a')+n%26)