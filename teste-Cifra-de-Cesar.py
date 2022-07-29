from unittest import TestCase, main
from Cifra_de_Cesar import encrypt, decrypt


class Cifra_de_Cesar(TestCase):

    def teste_quando_encrypt_abc_com_rot3_deve_retornar_def(self):
        valor_enviado = 'abc'
        valor_esperado = 'def'

        self.assertEqual(encrypt(valor_enviado), valor_esperado)

    def teste_quando_decrypt_def_com_rot3_deve_retornar_abc(self):
        valor_enviado = 'def'
        valor_esperado = 'abc'

        self.assertEqual(decrypt(valor_enviado), valor_esperado)
        
    def teste_quando_encrypt_xyz_com_rot3_deve_retornar_abc(self):
        valor_enviado = 'xyz'
        valor_esperado = 'abc'

        self.assertEqual(encrypt(valor_enviado), valor_esperado)

if __name__ == '__main__':
    main()
