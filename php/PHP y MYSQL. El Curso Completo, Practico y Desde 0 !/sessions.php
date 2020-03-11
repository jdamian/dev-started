<?php
session_start();
$_SESSION['nombre'] = 'juan';

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Pagina de inicio</h1>
    <p>
    </p>
    <a href="sessions2.php">Ir a la pagina 2</a>
</body>
</html>