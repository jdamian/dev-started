"use strict";

var usuario = {
  nombre: 'carlos',
  correo: 'correo@correo.com',
  edad: 38,
  pais: 'peru',
  profesion: 'desarrollador web'
};
var nombre = usuario.nombre,
    correo = usuario.correo,
    profesion = usuario.profesion,
    _usuario$cargo = usuario.cargo,
    cargo = _usuario$cargo === void 0 ? 'no especificado' : _usuario$cargo;
console.log(profesion, cargo); //funcion

var mostrarInfo = function mostrarInfo(_ref) {
  var nombre = _ref.nombre,
      profesion = _ref.profesion;
  console.log("".concat(nombre, " es ").concat(profesion));
}; //en una linea
//const mostrarInfo = ({nombre, profesion}) => console.log(`${nombre} es ${profesion}`);


mostrarInfo(usuario);