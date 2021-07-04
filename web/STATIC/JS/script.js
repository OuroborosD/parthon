document.querySelector("div").onclick = function () {  
    // Call python's random_python function
    eel.gerador_cpf()(function(valor_cpf){ // o valor_cpf é quem recebe o valor do return                      
      // Update the div with a random number returned by python
      document.querySelector(".cpf").innerHTML = valor_cpf;
    })

    eel.chamar_juntarnome()(function(nome){
      console.log(nome.length)
      if(nome.length > 20){
        document.querySelector("p").style.fontSize = 14;
      }
      document.querySelector(".nome").innerHTML = nome;
    })
  }