<?php

$nombre = "carlos";
$munero = 6;
$decimal=5.5;
$valor= false;

echo $nombre;
echo $munero;

echo 'Hola ' . $nombre;

// constantes

define('PI', 3.14);

echo PI;

// arreglos indexado

$semana = array('Lunes'. 'Martes', 'Miercoles');
$arreglo = ['lunes', 'martes'];

// arreglo asociativo

$alex = array('telefono' => 98765654, 'edad' => 25, 'nombre' => 'juan carlos');
echo $alex['edad'];

echo count($semana);

sort($semana);
rsort($semana);

foreach ($semana as $dia) {
    echo $dia;
}


$numeros = [1,4,2,6,8,9];
sort($numeros);
foreach ($numeros as $numero) {
    echo $numero;
}

switch ($mes) {
    case 'enero':
        # code...
        break;
    
    default:
        # code...
        break;
}

$edad = (isset($edad))? $edad : 'el usuario no establecio su edad' ;

?>