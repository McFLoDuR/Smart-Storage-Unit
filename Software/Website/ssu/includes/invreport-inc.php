<?php
    session_start();

    if (!isset($_SESSION['username'])) {
        header("Location: ../login.php?redir=ect");
        exit();
    }

    $uid = $_SESSION['userID'];
    if(isset($_POST['1'])) {
        $mode = 1;
	}
	elseif(isset($_POST['2'])) {
        $mode = 2;
	}
	elseif(isset($_POST['3'])) {
        $mode = 3;
	}
    if(shell_exec("python3 /home/ssu/Desktop/PDF-Creator/PDF_Creator.py --mode ".$mode." --userID ".$uid." &")) {
		header("Location: ../home.php?success=report");
		exit();
	}
?>