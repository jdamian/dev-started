const crearObejto = (nombre, edad) => {
    return {
        nombre,
        edad,
        mostrarInfo(){
            return `${nombre} tiene ${edad} años`;
        }
    }
}

//console.log(crearObejto('Carlos', 38));
console.log(crearObejto('Carlos', 38).mostrarInfo());