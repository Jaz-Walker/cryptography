# transposition cipher

# enctryption function
def scrambleEncrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1

    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halflength = len(cipherText) // 2
    evenChars = cipherText[halflength:]
    oddChars = cipherText[:halflength]
    plainText = ""

    for i in range(halflength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText