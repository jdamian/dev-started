let nombre= 'Juan';
let apellido= 'Damian';
const edad = 38;

//uso de template string
function nombres(){
    return (`${nombre} ${apellido}`);
}

console.log('Hola ' + nombre);
console.log(nombres());
console.log(`Soy ${nombre} ${apellido} tengo ${edad}`);