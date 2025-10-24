def calcular_media(listaNotas):
    for nota in listaNotas:
        soma +=nota    
    media1 = soma/len(listaNotas)
    return media1


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 > media < 6.9:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"
    