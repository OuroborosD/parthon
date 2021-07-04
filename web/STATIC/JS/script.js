document.querySelector("div").onclick = function () {  
    // Call python's random_python function
    eel.gerador_cpf()(function(strg){                      
      // Update the div with a random number returned by python
      document.querySelector(".cpf").innerHTML = strg;
    })
  }