// ---- sidebar menu ------

const botones = document.querySelectorAll('.link__sidebar'); 
const secciones = document.querySelectorAll('.seccion__menu'); 

botones.forEach(boton => {
  boton.addEventListener('click', function (event) {
    event.preventDefault(); 

    secciones.forEach(sec => sec.classList.remove('activa'));

    const target = this.getAttribute('data-seccion');

    const seccionMostrar = document.querySelector(`[data-content="${target}"]`);

    seccionMostrar.classList.add('activa');
  });
});

// --------- BTN ENCUESTA ----------

const botonesEncuesta = document.querySelectorAll('.btn__encuesta');

botonesEncuesta.forEach(boton => {
  boton.addEventListener('click', function (event) {
    event.preventDefault(); 

    botonesEncuesta.forEach(b => {
      b.style.backgroundColor = "";
      b.style.color = "";
    })

    boton.style.backgroundColor = "pink";
    boton.style.color = "black";
  });
});
