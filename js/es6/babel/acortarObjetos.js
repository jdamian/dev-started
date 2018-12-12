"use strict";

var crearObejto = function crearObejto(nombre, edad) {
  return {
    nombre: nombre,
    edad: edad,
    mostrarInfo: function mostrarInfo() {
      return "".concat(nombre, " tiene ").concat(edad, " a\xF1os");
    }
  };
}; //console.log(crearObejto('Carlos', 38));


console.log(crearObejto('Carlos', 38).mostrarInfo());