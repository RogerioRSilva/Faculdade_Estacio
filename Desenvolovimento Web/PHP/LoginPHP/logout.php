<?php
    session_start();
    $_SESSION = array();
    session_destroy(); // Aqui destroi todas as informações da sessão. 
    header("Location: index.php", true, 301);
?>