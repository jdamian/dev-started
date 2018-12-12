const usuario = {
    nombre: 'carlos',
    correo: 'correo@correo.com',
    edad: 38,
    pais: 'peru',
    profesion: 'desarrollador web'
}

const {nombre, correo, profesion, cargo = 'no especificado'} = usuario;

console.log(profesion, cargo);

//funcion
const mostrarInfo = ({nombre, profesion}) => {
    console.log(`${nombre} es ${profesion}`);
}
//en una linea
//const mostrarInfo = ({nombre, profesion}) => console.log(`${nombre} es ${profesion}`);

mostrarInfo(usuario);