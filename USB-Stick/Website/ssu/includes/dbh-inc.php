<?php 
if(isset($legalRedirect_dbh))
{
	$servernm = "localhost";
	$dbUid = "ssu_db";
	$dbPwd = "ssu_FRS";
	$dbUid = "root";		//For the testing local server
	$dbPwd = "";			//For the testing local server
	$dbName = "ssu";

	$conn = mysqli_connect($servernm, $dbUid, $dbPwd, $dbName);
	
	if(!$conn)
	{
		die("Connection failed: " . mysqli_connect_error());
    }
}
else {
	header("Location: ../login.php?error=sqlerror");
	exit();
}