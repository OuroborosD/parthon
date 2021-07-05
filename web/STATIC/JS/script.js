document.querySelector(".moldura").onclick = function () {  
    eel.get_gerador_cpf()(function(valor_cpf){ // o valor_cpf é quem recebe o valor do return                      

      let tamanho = String(valor_cpf).length
      console.log(tamanho)
      document.querySelector(".cpf").innerHTML = valor_cpf;
    })

    eel.get_juntarnome()(function(nome){
      document.querySelector(".nome").innerHTML = nome;
      if(nome.length > 20){
        document.getElementById("nome").style.fontSize = "16px";
      }else{
        document.getElementById("nome").style.fontSize = "20px";
      }
      
    })

    eel.get_idade()(function(idade){
      console.log(typeof(idade))
      document.querySelector('.idade').innerHTML = idade[1];
      document.querySelector('.nascimento').innerHTML = idade[0];
    })

    eel.get_sexo()(function(sexo){
      document.querySelector('.sexo').innerHTML = sexo;
      if(sexo == 'f'){
        console.log(sexo);
        let feminino = document.querySelector(".foto");
        feminino.setAttribute('src', 'STATIC/IMG/f.jpg');
      }
      if(sexo == 'm'){
        console.log(sexo);
        let masculino = document.querySelector(".foto");
        masculino.setAttribute('src','STATIC/IMG/m.png');
      }
      
    })
  }