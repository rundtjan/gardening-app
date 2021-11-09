import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10000)
        self.koyhakortti = Maksukortti(10)

    def test_kassan_saldo_alussa_oiken(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_edulliset_myyty_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_maukkaat_myyty_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisella_edullisesti_lisaa_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisella_edullisesti_lisaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.edulliset, 2)

    def test_kateisella_edullisesti_oikea_vaihtoraha(self):
        self.assertAlmostEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_kateisella_edullisesti_raha_ei_riita_kaikki_palautetaan(self):
        self.assertAlmostEqual(self.kassapaate.syo_edullisesti_kateisella(220), 220)

    def test_kateisella_edullisesti_raha_ei_riita_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(220)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_edullisesti_raha_ei_riita_ei_lisa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(210)
        self.kassapaate.syo_edullisesti_kateisella(210)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)

    def test_kateisella_maukkaasti_lisaa_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisella_maukkaasti_lisaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 2)

    def test_kateisella_maukkaasti_oikea_vaihtoraha(self):
        self.assertAlmostEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_kateisella_maukkaasti_raha_ei_riita_kaikki_palautetaan(self):
        self.assertAlmostEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)

    def test_kateisella_maukkaasti_raha_ei_riita_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_maukkaasti_raha_ei_riita_ei_lisa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(210)
        self.kassapaate.syo_maukkaasti_kateisella(210)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_vahentaa_kortin_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.maksukortti.saldo, 9760)

    def test_syo_edullisesti_kortilla_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kasvattaa_kassan_laskuria(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.kassapaate.edulliset, 2)

    def test_syo_edullisesti_kortilla_ei_kasvata_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_ei_vahenna_kortin_saldoa_ellei_rahat_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertAlmostEqual(self.koyhakortti.saldo, 10)

    def test_syo_edullisesti_kortilla_palauttaa_false_ellei_rahat_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti), False)

    def test_syo_edullisesti_ei_kasvata_kassan_laskuria_ellei_rahat_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_vahentaa_kortin_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.maksukortti.saldo, 9600)

    def test_syo_maukkaasti_kortilla_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kasvattaa_kassan_laskuria(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 2)

    def test_syo_maukkaasti_kortilla_ei_kasvata_kassan_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_ei_vahenna_kortin_saldoa_ellei_rahat_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertAlmostEqual(self.koyhakortti.saldo, 10)

    def test_syo_maukkaasti_kortilla_palauttaa_false_ellei_rahat_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti), False)

    def test_syo_maukkaasti_ei_kasvata_kassan_laskuria_ellei_rahat_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertAlmostEqual(self.maksukortti.saldo, 10010)

    def test_kortille_lataaminen_negatiivisella_luvulla_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertAlmostEqual(self.maksukortti.saldo, 10000)