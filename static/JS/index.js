document.getElementById("inpUser").addEventListener("keyup", (e)=> {
    if( e.which == 9 || e.which == 37 || e.which == 39) {
        talk("Usuario");
}});

document.getElementById("inpPass").addEventListener("keyup", (e)=> {
    if( e.which == 9 || e.which == 37 || e.which == 39) {
        talk("Contraseña");
}});

document.getElementById("btnsubmit").addEventListener("keyup", (e)=> {
    if( e.which == 9 || e.which == 37 || e.which == 39) {
        talk("Ingresar");
}});

document.getElementById("btnsignup").addEventListener("keyup", (e)=> {
    console.log("Nel prro");
    if( e.which == 9 || e.which == 37 || e.which == 39) {
        talk("Registrarse");
}});

document.getElementById("error").addEventListener("keyup", (e)=> {
    if( e.which == 9 || e.which == 37 || e.which == 39) {
        if (document.getElementById("error").textContent != "") {
            talk("Credenciales inválidas");
        }
}});


document.getElementById("inises").addEventListener("keyup", (e)=> {
    if( e.which == 9 || e.which == 37 || e.which == 39) {
        talk("Inicio de sesión");
}});

function talk(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}

/*

No me gustó de todo el resultado

const KEYCODE = {
    LEFT: 37,
    RIGHT: 39
  };
  
  const formContent = document.querySelector('#formContent');
  formContent.addEventListener('keydown', onKeyDown);
  
  function onKeyDown(event) {
    switch (event.keyCode) {
      case KEYCODE.RIGHT:
        event.preventDefault();
        focusNextFormItem();
        break;
      case KEYCODE.LEFT:
        event.preventDefault();
        focusPreviousFormItem();
        break;
    }
  }
  
  function focusNextFormItem() {
    const item = document.activeElement;
    if (item.nextElementSibling) {
      activateFormItem(item.nextElementSibling);
    }
  }
  

  function focusPreviousFormItem() {
    const item = document.activeElement;
    if (item.previousElementSibling) {
      activateFormItem(item.previousElementSibling);
    }
  }
  function activateFormItem(item) {
    formContent.querySelectorAll('[tabindex]').forEach((el) => el.tabIndex = -1);
    
    item.tabIndex = 0;
    item.focus();
  }
  */