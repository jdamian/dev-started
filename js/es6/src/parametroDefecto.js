function registrarUsuario(nombre, pais = 'Peru', correo, telefono='0000'){
    return `Nombre: ${nombre}, Pais ${pais}, Correo:, ${correo}, Telefono: ${telefono}`;
}

console.log(registrarUsuario('Carlos',undefined,'correo@correo.com'));