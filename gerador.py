import eel
import os
from random import randint as num

path = os.path.dirname(os.path.realpath(__file__))
static = 'web'
path = os.path.join(path,static)
print(f' path é {path}')

eel.init(path)  
  
# Exposing the random_python function to javascript
@eel.expose    
def gerador_cpf(estado = 10,  controle = 0, digitos = 0):
    
    if estado != 10:
        return "em construção"
    
    digitos = str(num(000000000,999999999))
   
    incremento = 0
    while controle != 2:
        aux_conta = 0
        holder = 0
       
        for i in range(9+incremento):
            aux_conta += int(digitos[i]) * (10+incremento-i)
            
        
        #digitos_ver.append(int(aux_conta*10/11))
        holder = aux_conta*10%11
        digitos += str(holder)
        controle += 1 #incremento para sair o while.
        incremento = 1
    return digitos
    
  
# Start the index.html file
eel.start("index.html")