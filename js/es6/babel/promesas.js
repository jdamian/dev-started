"use strict";

var promesa = new Promise(function (resolve, reject) {
  //accion que se ejecutará - llamada Ajax
  //resolve();
  //reject();
  setTimeout(function () {
    var exito = true;

    if (exito) {
      resolve("La operacion tuvo exito");
    } else {
      reject("La operacion no tuvo exito");
    }
  }, 4000);
}); //el argumento es una funcion
// se ejecuta cuando es resolve

promesa.then(function (mensaje) {
  alert(mensaje);
}); // se ejecuta cuando es reject

promesa.catch(function (mensaje) {
  alert(mensaje);
});