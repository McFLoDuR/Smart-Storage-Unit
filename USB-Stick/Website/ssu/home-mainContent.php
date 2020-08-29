<?php
	if (!isset($legalRedirect_Home)) {
		header("Location: login.php?redir=ect");
		exit();
	}
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Smart Storage Unit</title>
    <link rel="stylesheet" type="text/css" href="includes/ssu.css" />
    <script type="text/javascript">
      var itemID = 0;

      function getRow(id) {
        let btnWithdrawItem = document.getElementById("btnWithdrawItem");
        let row = document.getElementById(id);

        row.style.backgroundColor = "#6d75b9";
        btnWithdrawItem.innerHTML = "Withdraw Item";
        btnWithdrawItem.disabled = false;

        try {
          if (itemID != id) {
            let rowBefore = document.getElementById(itemID);
            rowBefore.style.backgroundColor = "#adb2e0";
          }
        } catch {}
        itemID = id;

        window.tableRowID = id;
      }
    </script>
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
      <main id="homeMain">
      <?php 
        if(isset($_GET['logout'])) {
          if($_GET['logout'] == "failed") {
            echo "<p style='text-align: center; color: red; font-size: 20px;'><b>Logout failed.</b></p>";
          }
        }
        if(isset($_GET['item'])) {
          if ($_GET['item'] == "notinstorage") {
            echo "<p style='text-align: center; color: red; font-size: 20px;'><b>Not in storage.</b></p>";
          }
        }
        if (isset($_GET['error'])) {
          if ($_GET['error'] == "invalidpos") {
            echo "<p style='text-align: center; color: red; font-size: 20px;'><b>Invalid position.</b></p>";
          }
          elseif($_GET['error'] == "insufficientperms") {
            echo "<p style='text-align: center; color: red; font-size: 20px;'><b>Insufficient permissions.</b></p>";
          }
          elseif ($_GET['error'] == "sqlerror") {
            echo "<p style='text-align: center; color: red; font-size: 20px;'><b>Database error.<br>Item list cannot be displayed.</b></p>";
          }
        }
        if(isset($_GET['success'])) {
          if ($_GET['success'] == "withdraw") {
            echo "<p style='text-align: center; color: green; font-size: 20px;'><b>Successfully withdrawn.</b></p>";
          }
          elseif ($_GET['success'] == "store") {
            echo "<p style='text-align: center; color: green; font-size: 20px;'><b>Successfully stored.</b></p>";
          }
          elseif ($_GET['success'] == "report") {
            echo "<p style='text-align: center; color: green; font-size: 20px;'><b>Report successfully created.</b></p>";
          }
        }
      ?>
        <div id="itemList" >
          <?php 
            if(isset($_GET['error'])) {
              if ($_GET['error'] == "noitems") {
                echo "<p style='text-align: center; color: red; font-size: 20px;'><b>No items in the table.<br>Item list cannot be displayed.</b></p>";
              }
            }
            else
              require_once 'includes/itemList-inc.php';
          ?>
          <script type="text/javascript">
            document.addEventListener("DOMContentLoaded", () => {
              let btnReport = document.getElementById("btnReport");
              let btnStoreItem = document.getElementById("btnStoreItem");
              let btnWithdrawItem = document.getElementById("btnWithdrawItem");
              let btnNewItem = document.getElementById("btnNewItem");

              btnReport.disabled = false;
              btnStoreItem.disabled = false;
              btnNewItem.disabled = false;
              btnWithdrawItem.disabled = true;

              //Button Clicked
              btnReport.addEventListener("click", function(event) {
                window.location.replace("chooseReport.php");
              });
              btnStoreItem.addEventListener("click", function(event) {
                window.location.replace("storeItem.php");
              });
              btnWithdrawItem.addEventListener("click", function(event) {
                window.location.replace("withdrawQuantity.php?itemid=" + tableRowID);
              });
              btnNewItem.addEventListener("click", function(event) {
                alert("Coming soon!");
              });
            });
          </script>
        </div>
        <nav id="homeNav">
          <ul id="navList1">
            <li><button class="navButton" id="btnNewItem">New Item</button></li>
            <li><button class="navButton" id="btnReport">Create Report</button></li>
          </ul>
          <ul id="navList2">
            <li><button class="navButton" id="btnStoreItem">Store Item</button></li>
            <li><button class="navButton" id="btnWithdrawItem">Choose an Item to Withdraw</button></li>
          </ul>
        </nav>
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