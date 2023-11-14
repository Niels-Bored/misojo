document.getElementById("inpUser").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Usuario");
}});

document.getElementById("inpPass").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Contraseña");
}});

document.getElementById("inpCPass").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Confirmar Contraseña");
}});

document.getElementById("btnsubmit").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Registrarse");
}});

document.getElementById("btnLogin").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Login");
}});

document.getElementById("error").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        if (document.getElementById("error").textContent != "") {
            talk("Credenciales inválidas");
        }
}});

document.getElementById("regi").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Registro de Usuario");
}});
function talk(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}