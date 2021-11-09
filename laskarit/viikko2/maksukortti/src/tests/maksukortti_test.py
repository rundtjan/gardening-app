import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")


    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti))

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti))

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kortti.lataa_rahaa(-25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_kortilla_voi_ostaa_edullisen_lounaan_jos_sen_verran_rahaa(self):
        uusiKortti = Maksukortti(2.5)
        uusiKortti.syo_edullisesti()
        self.assertEqual("Kortilla on rahaa 0.0 euroa", str(uusiKortti))

    def test_kortilla_voi_ostaa_maukkaan_lounaan_jos_sen_verran_rahaa(self):
        uusiKortti = Maksukortti(4)
        uusiKortti.syo_maukkaasti()
        self.assertEqual("Kortilla on rahaa 0 euroa", str(uusiKortti))