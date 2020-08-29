<?php
  if (!isset($legalRedirect_WithdrawItem)) {
    header("Location: home.php");
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
      <main id="withdrawMain">
        <div id="instructions">
          <div id="instructionText">
            <p>
            Please take 
              <?php
              if (isset($_SESSION['numsth'])) {
                if(!isset($_SESSION['i'])) {
                  $_SESSION['i'] = 0;
                }
                if(isset($_POST['wbtnnext'])) {
                  $_SESSION['i']++;
                }
                $sql = "SELECT * FROM storagep WHERE storagehID=". $storagehArray[($_SESSION['numsth'] - $_SESSION['i']  - 1)]['ID'] ." AND itemID=".$_SESSION['itemid'];
                if(!mysqli_query($conn, $sql)) {
                  header("Location: home.php?error=sqlerror");
                  exit();
                }
              }
              else {
                $sql = "SELECT * FROM storagep WHERE storagehID=". $storagehRow['ID'] ." AND itemID=".$_SESSION['itemid'];
                if(!mysqli_query($conn, $sql)) {
                  header("Location: home.php?error=sqlerror");
                  exit();
                }
              }
              $result = mysqli_query($conn, $sql);
              $storagepRow = mysqli_fetch_array($result);
              $withdrawQuantity = $_SESSION['quantity'];
              if (isset($_POST['wbtnnext'])) {
                $sql = "UPDATE activeLEDs SET stateActivated=0, stateChanged=1 WHERE SlotID = " . $_SESSION['prevSTHID'];
                if(!mysqli_query($conn, $sql)) {
                  header("Location: home.php?error=sqlerror");
                  exit();
                }
              }
              $sql = "INSERT INTO activeLEDs (SlotID, color, speed, stateActivated, stateChanged) " .
                      "VALUES (" . $storagepRow['storagehID'] . ", '" . $_SESSION['color'] . "', 3, 1, 1)";
              if(!mysqli_query($conn, $sql)) {
                header("Location: home.php?error=sqlerror");
                exit();
              }
              $_SESSION['prevSTHID'] = $storagepRow['storagehID'];
              $_SESSION['quantity'] = withdrawInstructionAmount($withdrawQuantity, $storagepRow['quantity']);
              ?>
            out of the area marked on the right, from the storage slot blinking with the color below!
            </p>
            <div id="userColor" 
            style="margin: auto;width:30%;height: 100px; border: 2px solid black;background-color: <?php echo '#' . $_SESSION['color'] . ';'; ?>">
            </div>
          </div>
          <div id="storageH">
            <img src="img/storageSlot/storageSlot<?php
              if(isset($_SESSION['numsth'])) {
                $sql = "SELECT * FROM storagep WHERE storagehID=". $storagehArray[($_SESSION['numsth'] - $_SESSION['i']  - 1)]['ID'] ." AND itemID=".$_SESSION['itemid'];
                if(!mysqli_query($conn, $sql)) {
                  header("Location: home.php?error=sqlerror");
                  exit();
                }
                $result = mysqli_query($conn, $sql);
                $storagepRow = mysqli_fetch_array($result);
                withdrawItemStorageSlotImg($storagehArray[($_SESSION['numsth'] - $_SESSION['i']  - 1)], $storagepRow);
              }
              else {
                $sql = "SELECT * FROM storagep WHERE storagehID=". $storagehRow['ID'] ." AND itemID=".$_SESSION['itemid'];
                if(!mysqli_query($conn, $sql)) {
                  header("Location: home.php?error=sqlerror");
                  exit();
                }
                $result = mysqli_query($conn, $sql);
                $storagepRow = mysqli_fetch_array($result);
                withdrawItemStorageSlotImg($storagehRow, $storagepRow);
              }
            ?>.png" alt="SSU Storage Slot">
            <form action="<?php 
            if(isset($_SESSION['i'])) {if(($_SESSION['i'] + 1) == $_SESSION['numsth'] || $_SESSION['quantity'] == 0) {echo "includes/withdraw-inc.php";}} elseif (!isset($_SESSION['numsth'])) {echo "includes/withdraw-inc.php";} else { echo "withdrawItem.php";}
            ?>" method="post">
              <button name="wbtnnext" class="withdrawstoreButton" id="withdrawButtonNext"><?php 
                if(isset($_SESSION['i'])) {if(($_SESSION['i'] + 1) == $_SESSION['numsth'] || $_SESSION['quantity'] == 0){echo "Finish";} else{echo "Next";}} 
                else{if (!isset($_SESSION['numsth'])) {echo "Finish";} else{echo "Next";}}?>
              </button>
            </form>
          </div>
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