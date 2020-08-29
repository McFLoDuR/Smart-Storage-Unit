<?php
	if (!isset($legalRedirect_Store)) {
		header("Location: login.php?redir=ect");
		exit();
  }
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Smart Storage Unit</title>
    <link rel="stylesheet" type="text/css" href="includes/ssu.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
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
      <main id="storeMain">
        <div id="instructions">
          <div id="instructionText">
            <p>
            Please store 
              <?php
                echo "<b>".$_SESSION['storeQuantity'] ."</b> item";
                if ($_SESSION['storeQuantity'] > 1) {
                  echo "s";
                }
                
                if (isset($_SESSION['sthfound'])) {
                  echo " in position  <select name='position' form='storeForm'>".
                  "<option value='$insidePosition'>$insidePosition</option></select>".
                  "<br>from the storage slot with the lit up LED with the color below!";
                }
                else {
                  echo " in position <select name='position' form='storeForm'><option value='1'>1</option>".
                    "<option value='2'>2</option><option value='3'>3</option><option value='4'>4</option></select>,".
                    "<br>from the storage slot with the lit up LED with the color below!";
                }
              ?>
            </p>
            <div id="userColor" 
            style="margin: auto;width:20%;height: 80px; border: 2px solid black;background-color: <?php echo '#' . $_SESSION['color'] . ';'; ?>">
            </div>
          </div>
          <br>
          <form action="includes/store-inc.php" method="post" id="storeForm">
            <?php if(isset($_SESSION['sthfound'])) { echo "<span style='color:red;'>(Do not change)</span><br><br>"; } ?>
            <label for="divider">Dividers:</label>
            <input type="checkbox" name="divider1" value="1" <?php if($firstDivider){echo "checked ";} ?>>1
            <input type="checkbox" name="divider2" value="1" <?php if($secondDivider){echo "checked ";} ?>>2
            <input type="checkbox" name="divider3" value="1" <?php if($thirdDivider){echo "checked ";} ?>>3
            <br>
            <label for="quantityMin">Min. Quantity:</label>
            <input type="number" name="quantityMin" <?php if(!isset($_SESSION['sthfound'])) {echo "min='0' ";}
            else {echo "min='".$minquant."' max='".$minquant."' "; echo "value='$minquant'";} ?> required>
            <br>
            <label for="quantityMax">Max. Quantity:</label>
            <input type="number" name="quantityMax" <?php if(!isset($_SESSION['sthfound'])) { echo "min='".$_SESSION['storeQuantity']."' ";} 
            else {echo "min='".$maxquant."' max='".$maxquant."' "; echo "value='$maxquant'";}?> required>
            <br>
            <label for="alarmactivated">Alarm Activated:</label>
            <input type="checkbox" name="alarmactivated" value="1" <?php if(isset($alarmactivated)){echo "checked";} ?>>
            <br><br>
            <button name="sbtnfinish" class="withdrawstoreButton" id="storeButtonNext">
              Finish
            </button>
          </form>
        </div>
        <script>
          document.addEventListener("DOMContentLoaded", () => {
            let microscaleonbtn = document.getElementById("microscaleonbtn");
            let microscaleoffbtn = document.getElementById("microscaleoffbtn");
            let refreshvaluebtn = document.getElementById("refreshvalue");

            let onoroff = "";
            microscaleonbtn.addEventListener("click", function(event) {
              onoroff = "on";
              $("#microscaleDiv").load("includes/microscale-inc.php", {
                onoroff: onoroff
              });
            });

            microscaleoffbtn.addEventListener("click", function(event) {
              onoroff = "off";
              $("#microscaleDiv").load("includes/microscale-inc.php", {
                onoroff: onoroff
              });
            });

            refreshvaluebtn.addEventListener("click", function(event) {
              $("#microscalevalueDiv").load("includes/loadscaleval-inc.php");
            });
          });
        </script>
        <div id="microscaleDiv">
          <button id="microscaleonbtn" class="withdrawstoreButton">Extend Micro Scale</button>
          <button id="microscaleoffbtn" class="withdrawstoreButton">Hide Micro Scale</button><br><br>
          <button id="refreshvalue" class="withdrawstoreButton">Refresh Values</button><br>
          <div id="microscalevalueDiv">
                
          </div>
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