<?php

$texto= ' <> & "" ';

trim($texto);
strlen(($texto));
substr(($texto),0,2);
strtoupper($texto);
strtolower($texto);
strpos($texto,'H');
htmlspecialchars($texto);

$arreglo = ['uno' => 1, 'dos' => 2, 'tres'=> 3];

extract($arreglo); // extrae los indices como variables;
array_pop($arreglo); // extrae el ultimo
join(' - ', $arreglo);
count($arreglo);
sort($arreglo);
array_reverse($arreglo);

$numero = 15.454;

round($numero,2);
rand(1,10);
ceil($numero); //redondeo hacia arriba
echo M_PI;


include 'vista.php';
require 'vista.php';

die(); // exit la ejecucion

?>