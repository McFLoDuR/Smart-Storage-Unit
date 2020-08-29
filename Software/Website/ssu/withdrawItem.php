<?php
	session_start();
	require_once 'includes/lib-inc.php';
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
	}
	if (!isset($_POST['quantity-submit'])) {
		if(!isset($_SESSION['numsth'])) {
			header("Location: login.php?redir=ect");
			exit();
		}
	}
	else {
		$_SESSION['quantity'] = $_POST['quantity'];
		$_SESSION['quantityWithdrawn'] = $_POST['quantity'];
	}

	if(isset($_SESSION['numsth']))
	{
		$sql = "SELECT * FROM storageh WHERE storagePosition IN(SELECT storagehID FROM storagep WHERE itemID=" . 
				$_SESSION['itemid'] . " ORDER BY quantity ASC);";
		if(!mysqli_query($conn, $sql)) {
			header("Location: home.php?error=sqlerror");
			exit();
		}
		$result = mysqli_query($conn, $sql);
		$storagehArray = [];
		while ($storagehRow = mysqli_fetch_array($result)) {
			array_push($storagehArray, $storagehRow);
		}
	}
	else {
		$sql = "SELECT * FROM storageh WHERE storagePosition IN(SELECT storagehID FROM storagep WHERE itemID=" . 
				$_SESSION['itemid'] . " ORDER BY quantity ASC);";
		if(!mysqli_query($conn, $sql)) {
			header("Location: home.php?error=sqlerror");
			exit();
		}
		$result = mysqli_query($conn, $sql);
		$storagehRow = mysqli_fetch_array($result);
		if (mysqli_num_rows($result) > 1) {
			$_SESSION['numsth'] = mysqli_num_rows($result);
			header("Location: withdrawItem.php");
			exit();
		}
	}

	$legalRedirect_WithdrawItem = true;
	require_once 'withdrawItem-mainContent.php';
?>