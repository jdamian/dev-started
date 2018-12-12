const promesa = new Promise( (resolve, reject) => {
    //accion que se ejecutará - llamada Ajax
    
    //resolve();
    //reject();

    setTimeout(()=>{
        let exito = true;
        if(exito){
            resolve("La operacion tuvo exito");
        } else{
            reject("La operacion no tuvo exito");
        }
    },4000);
} ); //el argumento es una funcion

// se ejecuta cuando es resolve
promesa.then((mensaje)=>{
    alert(mensaje);
})

// se ejecuta cuando es reject
promesa.catch((mensaje)=>{
    alert(mensaje);
});