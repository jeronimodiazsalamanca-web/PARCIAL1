def cantidad_perdidas(notas):
    perdidas = 0

    for nota in notas:
        if nota < 3:
            perdidas += 1

    return perdidas