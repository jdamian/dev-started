// import modules
var robot = require('robotjs');

var mensaje="hello world";

//robot.moveMouseSmooth(100,100);
//console.log(robot);

// export modules

//module.exports = mensaje;
var obj= {
    init: function () {
        console.log("mensaje de prueba");
    }
}

module.exports= obj;