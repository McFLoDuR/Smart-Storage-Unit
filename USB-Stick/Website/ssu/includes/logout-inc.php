<?php
   session_start();

   $legalRedirect_dbh = true;
   require_once 'dbh-inc.php';
   $sql = "UPDATE users SET userSignedIn=0 WHERE ID=" . $_SESSION['userID'];
   if(!mysqli_query($conn, $sql)) {
      header("Location: ../home.php?logout=failed");
      exit();
   }
   session_unset();
   session_destroy();
   header("Location: ../login.php");
   exit();