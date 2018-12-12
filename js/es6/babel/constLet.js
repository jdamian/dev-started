"use strict";

var nombre = 'Juan';
var apellido = 'Damian';
var edad = 38; //uso de template string

function nombres() {
  return "".concat(nombre, " ").concat(apellido);
}

console.log('Hola ' + nombre);
console.log(nombres());
console.log("Soy ".concat(nombre, " ").concat(apellido, " tengo ").concat(edad));