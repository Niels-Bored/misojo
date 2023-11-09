document.getElementById("inpUser").addEventListener("mouseover", ()=>{
    talk("Usuario");
});

document.getElementById("inpUser").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Usuario");
}});

document.getElementById("inpPass").addEventListener("mouseover", ()=>{
    talk("Contraseña");
});

document.getElementById("inpPass").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Contraseña");
}});

document.getElementById("btnsubmit").addEventListener("mouseover", ()=>{
    talk("Ingresar");
});

document.getElementById("btnsubmit").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Ingresar");
}});

document.getElementById("btnsignup").addEventListener("mouseover", ()=>{
    talk("Registrarse");
});

document.getElementById("btnsignup").addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Registrarse");
}});

function talk(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}