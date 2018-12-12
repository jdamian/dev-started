"use strict";

var mostrarDatos = function mostrarDatos() {
  for (var _len = arguments.length, datos = new Array(_len), _key = 0; _key < _len; _key++) {
    datos[_key] = arguments[_key];
  }

  console.log(datos);
};

var arregloDatos = ["juan carlos", 23, "correo@hotmail.com"];
mostrarDatos.apply(void 0, arregloDatos);