<?php
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

    if(isset($_SESSION['username'])) {
			$repeatPwd = false;
			$invalidRepeat = false;
			$sqlerror = false;
			$changed = false;
			$invalid = false;
			$colortaken = false;
			if (isset($_GET['error'])) {
				if ($_GET['error'] == "repeatpwd") {
					$repeatPwd = true;
				}
				elseif ($_GET['error'] == "sqlerror") {
					$sqlerror = true;
				}
				elseif ($_GET['error'] == "invalid") {
					$invalid = true;
				}
				elseif ($_GET['error'] == "invalidRepeat") {
					$invalidRepeat = true;
				}
				elseif ($_GET['error'] == "colortaken") {
					$colortaken = true;
				}
			}
			elseif (isset($_GET['success'])) {
				$changed = true;
			}
			$legalRedirect_Profile = true;
			require_once 'profile-mainContent.php';
	}
	else {
		header("Location: login.php?redir=ect");
		exit();
	}
?>