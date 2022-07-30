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

    def teste_quando_decrypt_abc_com_rot3_deve_retornar_xyz(self):
        valor_enviado = 'abc'
        valor_esperado = 'xyz'

        self.assertEqual(decrypt(valor_enviado), valor_esperado)

    def teste_quando_encrypt_a3e_com_rot3_deve_retornar_d6h(self):
        valor_enviado = 'a3e'
        valor_esperado = 'd6h'

        self.assertEqual(encrypt(valor_enviado), valor_esperado)

    def teste_quando_decrypt_d6h_com_rot3_deve_retornar_a3e(self):
        valor_enviado = 'd6h'
        valor_esperado = 'a3e'

        self.assertEqual(decrypt(valor_enviado), valor_esperado)

    def teste_quando_encrypt_z90a_com_rot3_deve_retornar_c23d(self):
        valor_enviado = 'z90a'
        valor_esperado = 'c23d'

        self.assertEqual(encrypt(valor_enviado), valor_esperado)


if __name__ == '__main__':
    main()
