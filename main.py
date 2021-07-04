import eel
import os   
import funcoes

path = os.path.dirname(os.path.realpath(__file__))
static = 'web'
path = os.path.join(path,static)
print(f' path é {path}')

eel.init(path)  
  
# Exposing the random_python function to javascript
@eel.expose    
def get_gerador_cpf():
    cpf = funcoes.gerador_cpf()
    return cpf

@eel.expose
def get_juntarnome():    
    nome = funcoes.juntar_nomes()
    return nome
  
# Start the index.html file
eel.start("index.html")