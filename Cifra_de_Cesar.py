from string import ascii_lowercase as alpha, digits



def Cifra(function):

    def interna(frase, rot=3 ):
        frase_encryptada = ''

        if function.__name__ == 'decrypt':
            rot = -3

        for letra in frase:
            if letra in digits:
                frase_encryptada += digits[(digits.index(letra) + (rot)) % 10]
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