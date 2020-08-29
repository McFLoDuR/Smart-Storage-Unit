<?php
	session_start();
	require_once 'includes/lib-inc.php';
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	//checkIfSignedIn("includes/logout-inc.php");
	if(isset($_SESSION['username'])) {
		if ((!isset($_POST['search-submit']))) {
			header("Location: home.php");
			exit();
		}
		else {
			$searchString = $_POST['search'];
			$legitRedirect_Results = true;
			require_once 'results-mainContent.php';
		}
	}
	else {
		header("Location: login.php?redir=ect");
		exit();
	}
?>