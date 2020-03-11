<?php
session_start();

if($_SESSION){
    $nombre = $_SESSION['nombre'];
} else {
    echo ' no has iniciado sesion';
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hola, <?php echo $nombre; ?></h1>
    <p>
    </p>
    <a href="sessions.php">Ir a la pagina 1</a>
    <p>
    </p>
    <a href="sessions_close.php">cerrar sessions</a>
</body>
</html>