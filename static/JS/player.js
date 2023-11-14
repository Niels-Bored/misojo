function previousPage(filename, page){
    if(page==0){
        alert('No se puede ir más atrás')
    }else{
        page--
        window.location.href='/player/'+filename+"/"+page
    }
}

function nextPage(filename, page){
    page++
    window.location.href='/player/'+filename+"/"+page
}

const h3 = document.querySelector("h3");

h3.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk(h3.textContent);
}});

const ps = document.querySelectorAll("p");

for (const p of ps) {
    p.addEventListener("keyup", (e)=> {
        if( e.which == 9 ) {
            talk(p.textContent);
        }
    });
}

const a = document.querySelector("a");

a.addEventListener("keyup", (e)=> {
    if( e.which == 9 ) {
        talk(a.textContent);
}});

function talk(text) {
    console.log(text);
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}

const audio = document.querySelector('audio');
const playButton = document.querySelector('#btnplay');
const stopButton = document.querySelector('#btnstop');

playButton.addEventListener('click', () => {
  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
});

stopButton.addEventListener('click', () => {
  audio.pause();
});

const buttons = document.querySelectorAll("button");

for (const button of buttons) {
    button.addEventListener("keyup", (e)=> {
        if( e.which == 9 ) {
        console.log("p tag");

            talk(button.textContent);
        }
    });
}