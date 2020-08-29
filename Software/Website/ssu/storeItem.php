<?php
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
	}
	elseif(isset($_SESSION['username'])) {
		$sql = "SELECT * FROM permissions WHERE ID=".$_SESSION['permID'];
		if(!mysqli_query($conn, $sql)) {
		  header("Location: home.php?error=sqlerror");
		  exit();
		}
		$result = mysqli_query($conn, $sql);
		$row = mysqli_fetch_array($result);
		if($row['storeItems'] == 0) {
		  header("Location: home.php?error=insufficientperms");
		  exit();
		}

		$legalRedirect_storeItem = true;
		require_once 'storeItem-mainContent.php';
	}
?>