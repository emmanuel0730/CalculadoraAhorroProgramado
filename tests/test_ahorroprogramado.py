import unittest
import sys
from pathlib import Path

# Permite importar desde la carpeta raíz del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.ahorro import *

class TestAhorroProgramado(unittest.TestCase):
    # CASOS NORMALES
    def test_caso_normal_uno(self):
        ahorro = AhorroProgramado(meta=1100000, plazo=6, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 179925.80)

    def test_caso_normal_dos(self):
        ahorro = AhorroProgramado(meta=9000000, plazo=12, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 719563.29)

    def test_caso_normal_tres(self):
        ahorro = AhorroProgramado(meta=170000000, plazo=36, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 4130954.55)

    #CASOS EXTRAORDINARIOS
    def test_meta_cero(self):
        ahorro = AhorroProgramado(meta=0, plazo=1, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 0)


    def test_ahorro_unico_mes(self):
        ahorro = AhorroProgramado(meta=90000, plazo=1, extra=0, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 90000)

    def test_extra_igual_meta(self):
        ahorro = AhorroProgramado(meta=400000, plazo=2, extra=400000, mes_extra=1)
        self.assertEqual(ahorro.calcular_ahorro(), 0)


    # CASOS DE ERROR
    def test_meta_menor_a_cero(self):
        with self.assertRaises(ErrorMetaMayorACero):
            ahorro = AhorroProgramado(meta=-1300000, plazo=15, extra=0, mes_extra=1)
            ahorro.calcular_ahorro()

    def test_plazo_cero(self):
        with self.assertRaises(ErrorPlazoMayorACero):
            ahorro = AhorroProgramado(meta=5000, plazo=0, extra=0, mes_extra=1)
            ahorro.calcular_ahorro()

    def test_abono_supera_meta(self):
        with self.assertRaises(ErrorAbonoSuperaMeta):
            ahorro = AhorroProgramado(meta=400000, plazo=2, extra=800000, mes_extra=1)
            ahorro.calcular_ahorro()

    def test_mes_extra_fuera_de_rango(self):
        with self.assertRaises(ErrorMesExtraFueraDelRango):
            ahorro = AhorroProgramado(meta=200000, plazo=3, extra=20000, mes_extra=5)
            ahorro.calcular_ahorro()
    
    def test_abono_menor_a_cero(self):
        with self.assertRaises(ErrorAbonoExtraMenorAcero):
            ahorro = AhorroProgramado(meta=200000, plazo=3, extra=-200000, mes_extra=1)
            ahorro.calcular_ahorro()

    
if __name__ == '__main__':
    unittest.main()