<?php
	/*
	This script is for when a user doesn't log out correctly and the userSignedIn value is still set to 1.
	Can be called anytime to reset all the user's signed-in status.
	*/
    $legalRedirect_dbh = true;
    require_once 'dbh-inc.php';

    $sql = "UPDATE users SET userSignedIn=0";
    if(!mysqli_query($conn, $sql)) {
        header("Location: profile.php?error=sqlerror");
        exit();
    }
    else {
        header("Location: ../login.php");
        exit();
    }
?>