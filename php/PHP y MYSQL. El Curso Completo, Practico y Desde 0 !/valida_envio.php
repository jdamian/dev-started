<?php

if($_SERVER['REQUEST_METHOD'] == 'GET'){
    echo 'se envia por get';
} else {
    // POST

}

if (isset($_POST['submit-formulario'])){
    echo ' se han enviado correctamente';
}




?>