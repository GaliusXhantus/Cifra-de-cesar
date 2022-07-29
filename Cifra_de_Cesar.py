from string import ascii_lowercase as alpha


def encrypt(frase, rot=3):
    frase_encryptada = ''

    for letra in frase:
        frase_encryptada += alpha[alpha.index(letra) + rot]

    return frase_encryptada

def decrypt(frase, rot=3):
    frase_decryptada = ''

    for letra in frase:
        frase_decryptada += alpha[alpha.index(letra) - rot]

    return frase_decryptada