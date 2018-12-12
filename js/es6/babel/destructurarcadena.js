"use strict";

function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance"); }

function _iterableToArrayLimit(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }

var persona = ['carlos', 38, 'peru', 'desarrollador web']; //destructurar

var nombre = persona[0],
    edad = persona[1],
    pais = persona[2],
    _persona$ = persona[3],
    profesion = _persona$ === void 0 ? 'No especificado' : _persona$;
console.log(persona[0]);
console.log(profesion); //destructurar en una funcion

var mostrarInfo = function mostrarInfo() {
  var _ref = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : persona,
      _ref2 = _slicedToArray(_ref, 3),
      nombre = _ref2[0],
      pais = _ref2[2];

  console.log(nombre, pais);
}; //en una linea
//const mostrarInfo = ([nombre,,pais] = persona) => console.log(nombre, pais);


mostrarInfo(persona);