def menor_nome(nomes):
    menorNome = nomes[0]
    for i in nomes:
        i = i.strip()
        if len(i) < len(menorNome):
            menorNome = i

    return menorNome.capitalize()
