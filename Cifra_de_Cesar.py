from string import ascii_lowercase as alpha, digits, punctuation as pontos


def Cifra(function):

    def interna(frase, rot=3 ):
        frase_encryptada = ''

        if function.__name__ == 'decrypt':
            rot = -rot

        for letra in frase:
            if letra in digits:
                frase_encryptada += digits[(digits.index(letra) + (rot)) % 10]

            elif letra in pontos:
                frase_encryptada += letra

            elif letra == ' ':
                frase_encryptada += ' '

            else:
                frase_encryptada += alpha[(alpha.index(letra) + (rot)) % 26]    

        return frase_encryptada

    return interna

@Cifra
def encrypt():
    return 

@Cifra
def decrypt():
    return 