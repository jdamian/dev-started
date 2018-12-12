"use strict";

var texto = "Hola mundo";
console.log(texto, " empieza con h:", texto.toLowerCase().startsWith("h"));
console.log(texto, " termina con o:", texto.toLowerCase().endsWith("o"));
console.log(texto, "incluye la palabra carlos:", texto.includes("carlos"));
var amigos = ["carlos", "alejandro", "cesar", "manuel"];
console.log(amigos.includes("manuel"));
console.log(amigos.find(function (amigo) {
  return amigo.length > 6;
}));
console.log(amigos.find(function (amigo) {
  return amigo.length > 6;
}));
console.log(amigos.find(function (amigo) {
  return amigo === "manuel";
}));
console.log(amigos.findIndex(function (amigo) {
  return amigo.length > 6;
}));
console.log(amigos.findIndex(function (amigo) {
  return amigo === "manuel";
}));