from src.funciones import maxima_nota

def test_maxima_nota():
    
    lista_prueba = [3.5, 4.0, 2.8, 5.0]
    resultado = maxima_nota(lista_prueba)
    assert resultado == 5.0
    
    
    assert maxima_nota([]) == 0
    
    
    assert maxima_nota([0.0, 1.5, 4.9]) == 4.9