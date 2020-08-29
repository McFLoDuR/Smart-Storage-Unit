<?php
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

    if(isset($_SESSION['username'])) {
		$sqlerror = false;
		$changed = false;
		if (isset($_GET['error'])) {
			if ($_GET['error'] == "sqlerror") {
				$sqlerror = true;
			}
		}
		elseif (isset($_GET['success'])) {
			$changed = true;
		}

		$sql = "SELECT * FROM permissions WHERE ID=(SELECT permissionID FROM users WHERE ID ='" . $_SESSION['userID'] . "')";
		if(!mysqli_query($conn, $sql)) {
		  header("Location: permissions.php?error=sqlerror");
		  exit();
		}
		else {
		  $result = mysqli_query($conn, $sql);
		  $row = mysqli_fetch_array($result);
		}

		$legalRedirect_Permissions = true;
		require_once 'permissions-mainContent.php';
	}
	else {
		header("Location: login.php?redir=ect");
		exit();
	}
?>