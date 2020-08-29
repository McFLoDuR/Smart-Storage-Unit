<?php
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
	}
	elseif(isset($_SESSION['username'])){
		
		unset($_SESSION['sthfound']);
		unset($_SESSION['itemid']);
		unset($_SESSION['storeQuantity']);
		unset($_SESSION['storagehslot']);
		unset($_SESSION['quantity']);
		unset($_SESSION['quantityWithdrawn']);
		unset($_SESSION['numsth']);
		unset($_SESSION['i']);
		$legalRedirect_Home = true;
		require_once 'home-mainContent.php';
	}
?>