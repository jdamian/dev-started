<?php

if(!$_POST){
    header('Location: form.php');
} 

$nombre = $_POST['nombre'];
$sexo = $_POST['sexo'];
$year = $_POST['year'];
$terminos = $_POST['terminos'];

echo 'Hola '. $nombre . $year;

?>