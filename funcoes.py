from random import randint as r



def gerador_nomes():
    letras = ['aeiou','bcdfghjklmnprstv']
    primeira_letra =  r(0,10)
    tamanho = r(5,12)
    nome = ''
    consoante_tamanho = len(letras[1])
    vogal_tamanho = len(letras[0])
    if primeira_letra == 0:
        controle = 0
        for i in range(tamanho):
            if controle == 0:
                nome += letras[0][r(0,vogal_tamanho-1)]
                controle = 1
            else:
                nome += letras[1][r(0,consoante_tamanho-1)]
                controle = 0
    else:
        controle = 1
        for i in range(tamanho):
            
            if controle == 0:
                nome += letras[0][r(0,vogal_tamanho-1)]
                controle = 1
            else:
                nome += letras[1][r(0,consoante_tamanho-1)]
                controle = 0
   
    return nome


def juntar_nomes():
    quantidade_nomes = r(2,3)
    nome_completo = ''
    if quantidade_nomes == 2:
        for i in range(quantidade_nomes):
            nome_aux = gerador_nomes()
            nome_completo +=   f"{nome_aux} "
    else:
        for i in range(quantidade_nomes):
            nome_aux = gerador_nomes()
            nome_completo +=   f"{nome_aux} "
    
    
    nome_completo = nome_completo.lstrip()#apagar o ultimo espaço
    return nome_completo
    


