const nombres=['Carlos','Juan','Manuel','Cesar'];

const numero_caracteres = nombres.map(function(nombre){
    console.log(`${nombre} tiene ${nombre.length} letras`);
});

const numero_caracteres1 = nombres.map((nombre)=>{
    console.log(`${nombre} tiene ${nombre.length} letras`);
});

const numero_caracteres2= nombres.map(nombre=>{
    return `${nombre} tiene ${nombre.length} letras`;
});

console.log(numero_caracteres2);

//en una sola linea

const numero_caracteres3= nombres.map(nombre=>`${nombre} tiene ${nombre.length} letras`);
console.log(numero_caracteres3);
/*
(parametro)=>{
    return
}
*/