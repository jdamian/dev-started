"use strict";

var nombres = ['Carlos', 'Juan', 'Manuel', 'Cesar'];
var numero_caracteres = nombres.map(function (nombre) {
  console.log("".concat(nombre, " tiene ").concat(nombre.length, " letras"));
});
var numero_caracteres1 = nombres.map(function (nombre) {
  console.log("".concat(nombre, " tiene ").concat(nombre.length, " letras"));
});
var numero_caracteres2 = nombres.map(function (nombre) {
  return "".concat(nombre, " tiene ").concat(nombre.length, " letras");
});
console.log(numero_caracteres2); //en una sola linea

var numero_caracteres3 = nombres.map(function (nombre) {
  return "".concat(nombre, " tiene ").concat(nombre.length, " letras");
});
console.log(numero_caracteres3);
/*
(parametro)=>{
    return
}
*/