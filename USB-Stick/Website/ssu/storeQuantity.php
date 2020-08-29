<?php 
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
	}

	if(isset($_GET['itemid']))
	{
		$_SESSION['itemid'] = $_GET['itemid'];
		header("Location: storeQuantity.php");
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

	$sql = "SELECT refnm.name, itmdt.propertyValue, itmdt.unit FROM referencenames refnm, itemdata itmdt WHERE " . 
			"(itmdt.itemID=".$_SESSION['itemid'].") AND (refnm.ID=itmdt.referenceID)";
	if(!mysqli_query($conn, $sql)) {
		header("Location: home.php?error=sqlerror");
		exit();
	}
	$result = mysqli_query($conn, $sql);
	$noItemData = false;
	if (!mysqli_num_rows($result)) {
		$noItemData = true;
	}

	$legalRedirect_storeQuantity = true;
	require_once 'storeQuantity-mainContent.php';
?>