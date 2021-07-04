document.querySelector(".moldura").onclick = function () {  
    eel.get_gerador_cpf()(function(valor_cpf){ // o valor_cpf é quem recebe o valor do return                      

      let tamanho = String(valor_cpf).length
      console.log(tamanho)
      document.querySelector(".cpf").innerHTML = (`${valor_cpf} : ${tamanho}`);
    })

    eel.get_juntarnome()(function(nome){
      
      document.querySelector(".nome").innerHTML = nome;
    })
  }