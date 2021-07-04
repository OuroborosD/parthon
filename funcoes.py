from random import randint as r

def gerador_cpf(estado = 10,  controle = 0, digitos = 0):
    
    if estado != 10:
        return "em construção"
    contador = 0
    digitos = str(r(000000000,999999999))
    if len(digitos) != 9: #foi colocada pois as vezes gera DIGITOS com 8 CARACTERES
        while True:      # força ele a ser de 9 caractes.
            digitos = str(r(000000000,999999999))
            contador += 1
            if len(digitos) == 9:
                break

    incremento = 0
    while controle != 2:
        aux_conta = 0
        holder = 0

        for i in range(9+incremento):
            
            aux_conta += int(digitos[i]) * (10+incremento-i)
            
       #digitos_ver.append(int(aux_conta*10/11))
        
        holder = (aux_conta * 10) %11
        
        if holder == 10:
            digitos += '0'
        else:
            digitos += str(holder)
        
        controle += 1 #incremento para sair o while.
        incremento = 1

  
    return digitos


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
    
for i in range(60):
    gerador_cpf()
    print(f'vez {i}')

