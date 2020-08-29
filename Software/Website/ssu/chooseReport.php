<?php
	session_start();
	$legalRedirect_dbh = true;
	require_once 'includes/dbh-inc.php';

	if (!isset($_SESSION['username'])) {
		header("Location: login.php?redir=ect");
		exit();
  }
  
  $sql = "SELECT * FROM permissions WHERE ID=".$_SESSION['permID'];
  if(!mysqli_query($conn, $sql)) {
    header("Location: home.php?error=sqlerror");
    exit();
  }
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_array($result);
  if($row['createInventoryReport'] == 0) {
    header("Location: home.php?error=insufficientperms");
    exit();
  }
  
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Smart Storage Unit</title>
    <link rel="stylesheet" type="text/css" href="includes/ssu.css" />
  </head>
  <body>
    <div id="container">
      <header>
        <div id="heading">
          <img src="img/SSU_Logo.PNG" alt="SSU Logo" />
          <a href="home.php">SMART STORAGE UNIT</a>
        </div>
        <div id="headerForms">
          <form id="searchForm" action="results.php" method="post">
            <input type="text" name="search" placeholder="Search for an item" />
            <button type="submit" name="search-submit">Search</button>
		      </form>
		      <form id="logoutForm" action="includes/logout-inc.php" method="post">
		  	    <p>
              Logged In as:<br />
              <?php 
                echo "<b><a href='profile.php'>" . strtoupper($_SESSION['username']) . "</a></b><br>";
                echo "<b><a href='permissions.php'>(" . strtoupper($_SESSION['permName']) . ")</a></b>";
              ?>
            </p>
            <input type="submit" name="logout-submit" value="Log Out" />
          </form>
        </div>
      </header>
      <main id="reportMain">
        <b>All Items that are:</b>
        <form action="includes/invreport-inc.php" method="post" id="invreportForm">
        <div id="mode12Div">
          <div id="mode1Div">
            <input type="submit" class="navButton" name="1" value="currently stored">
          </div>
          <div id="mode2Div">
            <input type="submit" class="navButton" name="2" value="in the database">
          </div>
        </div>
          <div id="mode3Div">
            <input type="submit" class="navButton" name="3" value="low in quantity">
          </div>
        </form>
      </main>
      <footer>
        <div id="watermark">
          <p>
			Copyright &copy; Diploma Thesis 2019/2020 by Migirov Rudolf, Reiner Fabian, Zauper Stefan
          </p>
        </div>
      </footer>
    </div>
  </div>
</html>