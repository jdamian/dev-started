class Usuario{
    constructor(nombre, edad, correo){
        this.nombre = nombre,
        this.edad = edad,
        this.correo =  correo
    }

    mostrarSaludo(mensaje){
        return mensaje;
    }

    monstrarInfo(){
        return `
            Nombre: ${this.nombre} <br />
            Edad: ${this.edad} <br />
            Correo: ${this.correo} <br />
            <hr />            
        `;
    }
}

const carlos = new Usuario('juan carlos', 38,'correo@correo.com');
document.write(carlos.nombre);
document.write(carlos.mostrarSaludo("Hola mundo"));
document.write(carlos.monstrarInfo());

class Estudiante extends Usuario{
    constructor(nombre, edad, correo, carrera){
        super(nombre, edad, correo);
        this.carrera = carrera;
    }

    monstrarInfo(){
        return `
            Nombre: ${this.nombre} <br />
            Edad: ${this.edad} <br />
            Correo: ${this.correo} <br />
            Carrera: ${this.carrera} <br />
            <hr />            
        `;
    }
}

const alejo = new Estudiante('alejandro', 30, 'alejo@correo.com', 'desarrollador web');
document.write(alejo.monstrarInfo());