document.getElementById("lblUser").addEventListener("mouseover", ()=>{
    talk(document.getElementById("lblUser").textContent);
});

document.getElementById("lblPass").addEventListener("mouseover", ()=>{
    talk(document.getElementById("lblPass").textContent);
});

document.getElementById("inpUser").addEventListener("mouseover", ()=>{
    talk("Entrada usuario");
});

document.getElementById("inpPass").addEventListener("mouseover", ()=>{
    talk("Entrada Contraseña");
});

document.getElementById("btnsubmit").addEventListener("mouseover", ()=>{
    talk("Enviar consulta");
});

document.getElementById("btnsignup").addEventListener("mouseover", ()=>{
    talk("Registrarse");
});

function talk(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}