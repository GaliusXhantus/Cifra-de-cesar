from string import ascii_lowercase as alpha, digits


def encrypt(frase, rot=3):
    frase_encryptada = ''

    for letra in frase:
        if letra in digits:
                frase_encryptada += digits[(digits.index(letra) + rot) % 10]
        else:
            frase_encryptada += alpha[(alpha.index(letra) + rot) % 26]
    

    return frase_encryptada

def decrypt(frase, rot=3):
    frase_decryptada = ''

    for letra in frase:
        if letra in digits:
            frase_decryptada += digits[(digits.index(letra) - rot) % 10]
        else:
            frase_decryptada += alpha[(alpha.index(letra) - rot) % 26]


    return frase_decryptada