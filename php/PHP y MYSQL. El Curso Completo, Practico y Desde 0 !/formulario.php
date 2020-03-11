<?php

$errores = '';

if(isset($_POST['submit'])){
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];

    if (!empty($nombre)){
        //$nombre = stripslashes(htmlspecialchars(trim($nombre)));
        $nombre = filter_var($nombre, FILTER_SANITIZE_STRING);
        echo ' Tu nombres es: '. $nombre;
    } else {
        $errores .= 'Por favor agrega un nombre: <br />';
    }

    if (!empty($email)){
        $email = filter_var($nombre, FILTER_SANITIZE_EMAIL);
        if (filter_var($email, FILTER_VALIDATE_EMAIL)){
            $errores .= 'Por favor ingrese un correo v;álido <br>';
        }
        echo "tu correo es: $email";
    } else {
        $errores .= 'Por favor agrega un email: ';
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .error{color: red}
    </style>
</head>
<body>
    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="post">
        <input type="text" name="nombre" id="" placeholder="Nombre">
        <input type="email" name="email" id="" placeholder="Email">
        <?php if(!empty($errores)): ?>
            <div class="error"><?php echo $errores; ?></div>
        <?php endif; ?>

        <input type="submit" value="submit" name="submit">
    </form>
</body>
</html>