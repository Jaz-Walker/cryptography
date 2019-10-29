-# transposition cipher

# enctryption function
def scrambleEncrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = evenChars + ch
            charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText
