<?php
    $host = "localhost";
    $username = "root";
    $password = "";
    $db_name = "test";

    $conn = new mysqli($host, $username, $password, $db_name);

    if($conn->connect_error) {
        echo "Connection failed: " . $conn->connect_error;
    }

    echo "Connect Successfully";


    $conn->close();
?>