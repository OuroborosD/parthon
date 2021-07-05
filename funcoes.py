from random import randint as r
import datetime

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


    
def gerar_nacimento():
    ano =str(r(1920,2020))
    mes =str(r(1,12))
    mes = mes.zfill(2)# preenche com 0, caso só tenha um digito.
    dia = str(r(1,31))
    dia = dia.zfill(2)
    nascimento = f'{dia}/{mes}/{ano}'
    return nascimento
    





def gerar_idade():
    """recebe a data de nascimento e calcula a idade.

    Returns:
        lista: contem lista[0] = data de nascimento
                      lista[1] = idade
    """
    nasceu = gerar_nacimento()   
    agora = datetime.datetime.now().strftime('%d/%m/%Y')
    idade = 0
    idade_info = []
    idade_info.append(nasceu)
    if int(nasceu[6:10]) <= int(agora[6:10]):
        
        if int(nasceu[3:5]) > int(agora[3:5]) and int(nasceu[6:10]) > int(agora[6:10]):
                return 'nascimento maior que a data atual: in'
        
        elif int(nasceu[3:5]) <= int(agora[3:5]) and int(nasceu[6:10]) < int(agora[6:10]) or  int(nasceu[3:5]) >= int(agora[3:5]) and int(nasceu[6:10]) < int(agora[6:10]) :
                idade = int(agora[6:10])  -  int(nasceu[6:10])  
                
        
        
        else:
        
                idade = (int(agora[3:5]) + 11)  -  int(nasceu[3:5])
                idade = f'{idade} meses'
        
        idade_info.append(idade)
        return idade_info
        
    return 'nascimento maior que  a data atual'

def gerar_sexo():
    sexos = ['f','m']
    escolha = r(0,1)
    return sexos[escolha]


