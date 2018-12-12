const persona = ['carlos',38,'peru','desarrollador web'];
//destructurar
const [nombre, edad, pais, profesion = 'No especificado']= persona;

console.log(persona[0]);
console.log(profesion);

//destructurar en una funcion
const mostrarInfo = ([nombre,,pais] = persona) => {
    console.log(nombre, pais);
}

//en una linea
//const mostrarInfo = ([nombre,,pais] = persona) => console.log(nombre, pais);

mostrarInfo(persona);