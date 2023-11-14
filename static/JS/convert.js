const h3 = document.querySelector("h3");

h3.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk(h3.textContent);
}});

const label = document.querySelector("label");

label.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk(label.textContent);
}});

const btnarch = document.getElementById("btnsel");

btnarch.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Seleccionar archivo");
}});

const btncon = document.getElementById("btncon");

btncon.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Convertir archivo");
}});

const p = document.querySelector("p");

p.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk("Archivo inválido");
}});

function talk(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}