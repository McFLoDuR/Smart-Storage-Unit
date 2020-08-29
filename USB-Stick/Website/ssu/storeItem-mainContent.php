<?php
	if (!isset($legalRedirect_storeItem)) {
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
        let btnStoreSubmitItem = document.getElementById("btnStoreSubmitItem");
        let row = document.getElementById(id);

        row.style.backgroundColor = "#6d75b9";
        btnStoreSubmitItem.innerHTML = "Next";
        btnStoreSubmitItem.disabled = false;

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
      <main id="storeItemMain">
        <div id="storeItemList" >
          <?php 
            $showAllItems = true;
            require_once 'includes/itemList-inc.php';
          ?>
          <script type="text/javascript">
            document.addEventListener("DOMContentLoaded", () => {
              let btnStoreSubmitItem = document.getElementById("btnStoreSubmitItem");

              btnStoreSubmitItem.disabled = true;

              //Button Clicked
              btnStoreSubmitItem.addEventListener("click", function(event) {
                window.location.replace("storeQuantity.php?itemid=" + tableRowID);
              });
            });
          </script>
        </div>
        <nav id="storeItemNav">
          <button class="navButton" id="btnStoreSubmitItem">Choose an Item to Store</button>
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