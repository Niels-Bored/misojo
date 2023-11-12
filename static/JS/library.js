function checkFile(url){
    window.location.href=url
}

function isEnter(item) {
    if (event.key === "Enter") {
      checkFile('/player/' + item);
    }
  }
  

const h1s = document.querySelectorAll("h1");

for (const h1 of h1s) {
    h1.addEventListener("mouseover", ()=>{
        talk("Librería");
    });

    h1.addEventListener("keyup", (e)=> {
        if( e.which == 9 ) {
        console.log("tit");
            talk("Librería");
        }
    });
}

const as = document.querySelectorAll("a");

for (const a of as) {
    a.addEventListener("mouseover", ()=>{
        talk(a.textContent);
    });

    a.addEventListener("keyup", (e)=> {
        if( e.which == 9 ) {
            talk(a.textContent);
        }
    });
}

const ps = document.querySelectorAll("p");

for (const p of ps) {
    p.addEventListener("mouseover", ()=>{
        talk(p.textContent);
    });

    p.addEventListener("keyup", (e)=> {
        if( e.which == 9 ) {
        console.log("p tag");

            talk(p.textContent);
        }
    });
}

const tds = document.querySelectorAll("td");

for (const td of tds) {
    td.addEventListener("mouseover", ()=>{
        talk(td.textContent);
    });

    td.addEventListener("keyup", (e)=> {
        if( e.which == 9 ) {
        console.log("td tag");

            talk(td.textContent);
        }
    });
}

function talk(text) {
    console.log(text);
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-MX';
    speechSynthesis.speak(utterance);
}