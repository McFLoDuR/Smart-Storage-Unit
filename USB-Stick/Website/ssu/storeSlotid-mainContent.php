<?php
	if (!isset($legalRedirect_storeSlotId)) {
		header("Location: login.php?redir=ect");
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
      <main id="storeSlotidMain">
        <div id="itemData">
          <p>Store <?php echo $itemType; ?>: <?php echo $itemArtNo; ?></p>
          <p>Quantity: <?php echo $_SESSION['storeQuantity'];?></p>
        </div>
        <div id="chooseSlot">
          <form action="store.php" method="post">
            <label for="storagehslot">Storage slot:</label><br>
            <select name="storagehslot" size="5" required>
              <?php
                while ($row = mysqli_fetch_array($result)) {
                  if ($row['itemID'] == $_SESSION['itemid']) {
                    if($_SESSION['storeQuantity'] <= ($row['quantityMax'] - $row['quantity'])) {
                      echo "<option value='" . $row['storagehID'] . "'>" . $row['storagehID'] . "</option>";
                      $_SESSION['sthfound'] = true;
                    }
                  }
                }
                if (!isset($_SESSION['sthfound'])) {
                  for ($i=1; $i <= 240; $i++) {
                    $free = false;
                    $sql = "SELECT * FROM storageh sth WHERE (firstPartition+secondPartition+thirdPartition+1)>(SELECT COUNT(*) FROM storagep stp WHERE stp.storagehID=sth.storagePosition)";
                    if(!mysqli_query($conn, $sql)) {
                      header("Location: home.php?error=sqlerror");
                      exit();
                    }
                    $result = mysqli_query($conn, $sql);
                    while ($row = mysqli_fetch_array($result)) {
                      if ($i == $row['storagePosition']) {
                        $free = true;
                      }
                    }
                    if($free) {
                      echo "<option value='$i'>$i</option>";
                    }
                  }
                }
              ?>
            </select>
            <br><br>
            <input name="slotid-submit" type="submit" value="Next">
          </form>
        </div>
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