<?php
	session_start();

	if (isset($_SESSION['username'])) {
		header("Location: home.php");
		exit();
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<title>Smart Storage Unit</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="includes/ssuLogin.css">
	</head>
	<body>
		<img id="logo" src="img/SSU_Logo.PNG" height="15%" width="15%" alt="SSU Logo"  />
		<p id="loginTitle"><b>Smart Storage Unit</b></p>
		<?php
			if (isset($_GET['error'])) {
				if ($_GET['error'] == "invalid") {
					echo "<p id='error'><b>Username or Password incorrect. Please retry!</b></p>";
				}
				elseif ($_GET['error'] == "sqlerror") {
					echo "<p id='error'><b>There was an error with the database.</b></p>";
				}
				elseif ($_GET['error'] == "busy") {
					echo "<p id='error'><b>User already logged in.</b></p>";
				}
			}
			if (isset($_GET['redir'])) {
				if($_GET['redir'] == "ect") {
					echo "<p id='error'><b>You have to log in first!</b></p>";
				}
			}
		?>
		<div id="formDiv">
			<form id="loginForm" action="includes/login-inc.php" method="post">
				<span>Username:</span>
				<br>
				<input id="usnm" type="text" name="usernm" placeholder="Username..." required>
				<br><br>
				<span>Password:</span>
				<br>
				<input id="pwd" type="password" name="pwd" placeholder="Password..." required>
				<br><br>
				<input type="submit" name="login-submit" value="Log In">
			</form>
		</div>
	</body>
	<footer>
		<div id="watermark">
			<p>
			Copyright &copy;
			Diploma Thesis 2019/2020 by Migirov Rudolf, Reiner Fabian, Zauper Stefan				
			</p>
		</div>
	</footer>
</html>