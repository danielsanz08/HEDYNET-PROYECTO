// Obtén el elemento contenedor
let container = document.getElementById('container');

// Agrega la clase 'expand' al formulario
document.querySelector('.form').classList.add('expand');

// Define la función toggle para alternar entre las clases 'sign-in' y 'sign-up'
const toggle = () => {
    container.classList.toggle('sign-in');
    container.classList.toggle('sign-up');
}

// Agrega la clase 'sign-in' al contenedor después de un retraso de 200ms
setTimeout(() => {
    container.classList.add('sign-in');
}, 200);
