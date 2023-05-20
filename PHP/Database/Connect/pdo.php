<?php
    $host = "localhost";
    $username = "root";
    $password = "";
    $db_name = "test";

    try {
        $conn = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);

        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        echo "Connected successfully";
    }catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }

?>