document.addEventListener('DOMContentLoaded', function() {
    const autotestul = document.getElementById('form');
    const cartee = document.getElementById('carte');

    function montrerQuestion() {
        autotestul.classList.add('hidden');
    }

    function montrerReponse() {
        document.getElementById('carte').classList.toggle('carte-bougeante');
        autotestul.classList.remove('hidden');
        cartee.removeEventListener('click', montrerReponse);
    }

    montrerQuestion();

    cartee.addEventListener('click', montrerReponse);
});
