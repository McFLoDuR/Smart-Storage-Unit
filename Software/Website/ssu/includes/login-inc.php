<?php
	if(isset($_POST['login-submit']))
	{
		session_start();
		require_once 'lib-inc.php';
		$legalRedirect_dbh = true;
		require_once 'dbh-inc.php';

		//checkIfSignedIn("logout-inc.php");
		
		$username = $_POST['usernm'];
		$password = $_POST['pwd'];

		$sql = "SELECT * FROM users WHERE username=? AND password=? LIMIT 1";
		$stmt = mysqli_stmt_init($conn);

		if (!mysqli_stmt_prepare($stmt, $sql)) {
			header("Location: ../login.php?error=sqlerror");
			exit();
		}
		else {
			mysqli_stmt_bind_param($stmt, "ss", $username, hashPwd($password));
			mysqli_stmt_execute($stmt);
			$result = mysqli_stmt_get_result($stmt);
			if ($row = mysqli_fetch_array($result)) {			
				if($row['userSignedIn']) {
					header("Location: ../login.php?error=busy");
					exit();
				}
				$_SESSION['userID'] = $row['ID'];
				$_SESSION['username'] = $row['username'];
				$_SESSION['email'] = $row['email'];
				$_SESSION['color'] = $row['color'];
				$_SESSION['mNotif'] = $row['monthlyNotification'];
				$_SESSION['signedIn'] = $row['userSignedIn'];
				$_SESSION['permID'] = $row['permissionID'];

				$sql = "SELECT * FROM permissions WHERE ID=" . $_SESSION['permID'];
				if (!$result = mysqli_query($conn, $sql)) {
					header("Location: ../login.php?error=sqlerror");
					exit();
				}
				if (!$row = mysqli_fetch_array($result)) {
					header("Location: ../login.php?error=sqlerror");
					exit();
				}
				$_SESSION['permName'] = $row['permissionName'];

				$sql = "UPDATE users SET userSignedIn=1 WHERE ID=" . $_SESSION['userID'];
				if (!mysqli_query($conn, $sql)) {
					header("Location: ../login.php?error=sqlerror");
					exit();
				}
				
				mysqli_commit($conn);
				mysqli_close($conn);

				header("Location: ../home.php");
				exit();
			}
			else {
				header("Location: ../login.php?error=invalid");
				exit();	
			}
		}
	}
	else
	{
		header("Location: ../login.php?redir=ect");
		exit();
	}