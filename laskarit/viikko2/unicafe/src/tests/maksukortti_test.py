import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertAlmostEqual(self.maksukortti.saldo, 10)

    def test_kortin_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(5)
        self.assertAlmostEqual(self.maksukortti.saldo, 5)
    
    def test_saldo_ei_muutu_jos_liian_vahan_rahaa(self):
        self.maksukortti.ota_rahaa(12)
        self.assertAlmostEqual(self.maksukortti.saldo, 10)

    def test_palauttaa_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(12), False)

    def test_palauttaa_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(9), True)

    def test_lisays_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2)
        self.assertEqual(self.maksukortti.saldo, 12)

    def test_kortti_tulostaa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")