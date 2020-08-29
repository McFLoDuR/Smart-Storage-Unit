<?php
    session_start();
    $legalRedirect_dbh = true;
    require_once 'dbh-inc.php';

    if (!isset($_SESSION['username'])) {
        header("Location: login.php?redir=ect");
        exit();
    }
    if(isset($_POST['onoroff'])) {
        echo "<button id='microscaleonbtn' class='withdrawstoreButton'>Extend Micro Scale</button>";
        echo "<button id='microscaleoffbtn' class='withdrawstoreButton'>Hide Micro Scale</button><br>";
        
        if($_POST['onoroff'] == "on") {
            echo "<button id='refreshvalue' class='withdrawstoreButton'>Refresh Values</button><br>";
            $sql="UPDATE statestorage SET stateActivated=1, stateChanged=1, UserID=".$_SESSION['userID'];
        }
        elseif($_POST['onoroff'] == "off") {
            $sql="UPDATE statestorage SET stateActivated=0, stateChanged=1";
        }
        if(!mysqli_query($conn, $sql)) {
            header("Location: home.php?error=sqlerror");
            exit();
        }

        echo "<div id='microscalevalueDiv'></div>";
    }
?>