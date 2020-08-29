<?php
    session_start();
    $legalRedirect_dbh = true;
    require_once 'dbh-inc.php';

    if (!isset($_SESSION['username'])) {
        header("Location: login.php?redir=ect");
        exit();
    }
    
    $sql = "SELECT weight FROM items WHERE ID=".$_SESSION['itemid'];
    if(!mysqli_query($conn, $sql)) {
        header("Location: home.php?error=sqlerror");
        exit();
    }
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_array($result);
    $itemweight = $row['weight'];

    $sql = "SELECT stateValue FROM statestorage";
    if(!mysqli_query($conn, $sql)) {
        header("Location: home.php?error=sqlerror");
        exit();
    }
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_array($result);
    $itemCount = 1;
    $itemCount = $row['stateValue'] / $itemweight;
    echo "<p>";
    echo "$itemCount item(s) are on the scale. <br>(".$row['stateValue']."g)";
    echo "</p>";
?>