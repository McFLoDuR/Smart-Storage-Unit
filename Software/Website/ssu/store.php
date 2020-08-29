<?php 
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
	}
	if((!isset($_POST['slotid-submit'])) && (!isset($_SESSION['storagehslot']))) {
		header("Location: login.php?redir=ect");
		exit();
	}
	if(!isset($_SESSION['storagehslot'])) {
		$_SESSION['storagehslot'] = $_POST['storagehslot'];
		header("Location: store.php");
		exit();
	}

	if(isset($_SESSION['sthfound'])) {
		$sql="SELECT * FROM storagep WHERE storagehID=".$_SESSION['storagehslot']." AND itemID=".$_SESSION['itemid'];
		if(!mysqli_query($conn, $sql)) {
			header("Location: home.php?error=sqlerror");
			exit();
		}
		$result = mysqli_query($conn, $sql);
		$row = mysqli_fetch_array($result);
		$_SESSION['quantityStored'] = $row['quantity'];
		$alarmactivated = $row['alarmActivated'];
		$insidePosition = $row['insidePosition'];
		$minquant = $row['quantityMin'];
		$maxquant = $row['quantityMax'];
	}

	$sql="SELECT * FROM storageh WHERE storagePosition=" . $_SESSION['storagehslot'];
	if(!mysqli_query($conn, $sql)) {
		header("Location: home.php?error=sqlerror");
		exit();
	}
	$result = mysqli_query($conn, $sql);
	$row = mysqli_fetch_array($result);
	$firstDivider=$row['firstPartition'];
	$secondDivider=$row['secondPartition'];
	$thirdDivider=$row['thirdPartition'];

	$sql = "INSERT INTO activeLEDs (SlotID, color, speed, stateActivated, stateChanged) ".
			"VALUES (".$_SESSION['storagehslot'].", '".$_SESSION['color']."', 0, 1, 1)";
	if(!mysqli_query($conn, $sql)) {
		header("Location: home.php?error=sqlerror");
		exit();
	}

	$legalRedirect_Store = true;
	require_once 'store-mainContent.php';
?>