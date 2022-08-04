from unittest import TestCase, main
from Cifra_de_Cesar import encrypt, decrypt


class Cifra_de_Cesar(TestCase):

    def teste_quando_encrypt_z90a_com_rot3_deve_retornar_c23d(self):
        valor_enviado = 'z90a'
        valor_esperado = 'c23d'

        self.assertEqual(encrypt(valor_enviado), valor_esperado)

    def teste_quando_decrypt_c23d_com_rot3_deve_retornar_z90a(self):
        valor_enviado = 'c23d'
        valor_esperado = 'z90a'

        self.assertEqual(decrypt(valor_enviado), valor_esperado)

    def teste_quando_tiver_spaço_ou_pontuaçao_deve_adiciona_lo_a_frase(self):
        valor_enviado = 'z 9--?'
        valor_esperado = 'c d2--?'

        self.assertEqual(encrypt(valor_enviado), valor_esperado)


if __name__ == '__main__':
    main()
