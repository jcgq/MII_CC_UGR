import unittest
import sys
sys.path.insert(1, 'src')
from recetas import Receta

def test_validarCapacidades():
    recetilla = Receta("Caracoles", "1 kilo de habichuelas, medio litro de agua, dos ralladuras de melón","Cocinar todo con mucho tranquiilp", 67)
    assert(Receta.validarAlimentos(recetilla, Receta.unidadesPermitidas) == True)

