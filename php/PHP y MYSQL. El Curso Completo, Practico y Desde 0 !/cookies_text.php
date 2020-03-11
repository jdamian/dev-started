<?php

if(isset($_COOKIE['font-size'])){
    $tamaño = htmlspecialchars($_COOKIE['font-size']);
} else {
    $tamaño = '15px';
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        p{
            font-size: <?php echo $tamaño ?>
        }
    </style>
</head>
<body>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ex velit quos impedit facilis illo consectetur culpa eum eius, suscipit veritatis. Repudiandae ad temporibus rerum earum harum dignissimos labore veritatis?</p>
</body>
</html>