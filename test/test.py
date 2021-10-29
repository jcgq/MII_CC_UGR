import unittest
import sys
sys.path.insert(1, 'src')
from recetas import Receta

def test_validarCapacidades():
    recetaCorrecta = Receta("huevo frito", "un kilo de patatas; cien gramos de jamón", "Con mucho esmero y arte, se cocina un huevo", 22)    
    assert(isinstance(recetaCorrecta, Receta))

    recetaIncorrecta = Receta("Caracoles", "1 carabinero de habichuelas, medio litro de agua, dos cazuelicas de melón","Cocinar todo con mucho tranquiilp", 67)
    assert(isinstance(recetaIncorrecta, Receta))
