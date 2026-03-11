def cantidad_perdidas(notas, umbral=3.0):
    if not isinstance(notas, list):
        raise TypeError("El parámetro 'notas' debe ser una lista")
    
    return sum(1 for nota in notas if nota < umbral)