def maxima_nota(notas):
    
    if len(notas) == 0:
        return 0
    
    
    mayor = notas[0]
    

    for i in range(len(notas)):
        
        if notas[i] > mayor:
            mayor = notas[i]
            
    return mayor