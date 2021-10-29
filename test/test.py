import unittest
import sys
sys.path.insert(1, 'src')
from recetas import Receta

def test_validarCapacidades():
    recetaCorrecta = Receta("Caracoles", "1 kilo de habichuelas, medio litro de agua, dos ralladuras de melón","Cocinar todo con mucho tranquiilp", 67)
    assert(Receta.validarAlimentos(recetaCorrecta, Receta.unidadesPermitidas) == True)
    
    recetaIncorrecta = Receta("Caracoles", "1 carabinero de habichuelas, medio litro de agua, dos cazuelicas de melón","Cocinar todo con mucho tranquiilp", 67)
    assert(Receta.validarAlimentos(recetaIncorrecta, Receta.unidadesPermitidas) == False)   