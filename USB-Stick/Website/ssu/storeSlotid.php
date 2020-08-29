<?php 
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
	}

	if(isset($_POST['quantity'])) {
		$_SESSION['storeQuantity'] = $_POST['quantity'];
	}

	$sql = "SELECT cmpt.typeName, itm.articleNumber FROM componenttypes cmpt, items itm " .
			"WHERE (itm.ID=".$_SESSION['itemid'].") AND (cmpt.ID=itm.typeID);";
	if(!mysqli_query($conn, $sql)) {
		header("Location: home.php?error=sqlerror");
		exit();
	}
	$result = mysqli_query($conn, $sql);
	$row = mysqli_fetch_array($result);
	$itemType = $row['typeName'];
	$itemArtNo = $row['articleNumber'];

	$sql = "SELECT * FROM storagep";
	if(!mysqli_query($conn, $sql)) {
		header("Location: home.php?error=sqlerror");
		exit();
	}
	$result = mysqli_query($conn, $sql);

	$legalRedirect_storeSlotId = true;
	require_once 'storeSlotid-mainContent.php';
?>