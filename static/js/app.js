// ---- sidebar menu ------

const botones = document.querySelectorAll('.link__sidebar'); // Selecciona todos los botones del menu
const secciones = document.querySelectorAll('.seccion__menu'); // Selecciona todas las secciones de contenido

botones.forEach(boton => {
  boton.addEventListener('click', function (event) {
    console.log("prueba boton")
    event.preventDefault(); // Evita que el enlace <a href=""> recargue la página

    // Oculta todas las secciones
    secciones.forEach(sec => sec.classList.remove('activa'));

    // Obtiene el nombre de la sección a mostrar
    const target = this.getAttribute('data-seccion');

    // Muestra solo la sección correspondiente
    const seccionMostrar = document.querySelector(`[data-content="${target}"]`);

    seccionMostrar.classList.add('activa');
  });
});