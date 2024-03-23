const autotestul = document.getElementById('form');
const front = document.querySelector('.front');
const back = document.querySelector('.back');
let index = 0;

cartesDues = []

function montrerQuestion(currentCardIndex) {
    front.innerText = carte.devant;
    autotestul.classList.add('hidden');
}

function montrerReponse(currentCardIndex) {
    back.innerText = carte.dos;
    document.getElementById('carte').classList.toggle('carte-bougeante');
    autotestul.classList.remove('hidden');
    front.removeEventListener(onclick);
}

montrerQuestion();