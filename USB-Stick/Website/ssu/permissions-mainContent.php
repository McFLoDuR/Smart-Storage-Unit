<?php
    if(isset($legalRedirect_Permissions)) {
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
      <main id="permissionsMain">
        <h2 id="permissionsHeading">User Permissions</h2>
        <hr>
        <form id="permissionsForm">
          <div>
            <?php
              if($changed) {echo "<span class='feedbackMsg'>Successfully changed.</span>";}
              elseif($sqlerror){echo "<span class='feedbackMsg'>Error.</span>";}
            ?>
            <table id="permTable2">
              <tbody id="permTbody_1">
                <tr>
                  <td><span>Manage Users</span></td>
                  <td><input type="checkbox" name="manageUsers" disabled <?php if($row['manageUsers']) { echo "checked"; } ?>></td>
                </tr>
                <tr>
                  <td><span>Manage Partitions</span></td>
                  <td><input type="checkbox" name="managePartitions" disabled <?php if($row['managePartitions']) { echo "checked"; } ?>></td>
                </tr>
                <tr>
                  <td><span>Correct Quantity</span></td>
                  <td><input type="checkbox" name="correctQuantity" disabled <?php if($row['correctQuantity']) { echo "checked"; } ?>></td>
                </tr>
                <tr>
                  <td><span>Create Inventory Report</span></td>
                  <td><input type="checkbox" name="createInventoryReport" disabled <?php if($row['createInventoryReport']) { echo "checked"; } ?>></td>
                </tr>
              </tbody>
              <tbody id="permTbody_2">
                <tr>
                  <td><span>Store Items</span></td>
                  <td><input type="checkbox" name="storeItems" disabled <?php if($row['storeItems']) { echo "checked"; } ?>></td>
                </tr>
                <tr>
                  <td><span>Withdraw Items</span></td>
                  <td><input type="checkbox" name="withdrawItems" disabled <?php if($row['withdrawItems']) { echo "checked"; } ?>></td>
                </tr>
                <tr>
                  <td><span>Delete Storage Slot</span></td>
                  <td><input type="checkbox" name="deleteStorageSlot" disabled <?php if($row['deleteStorageSlot']) { echo "checked"; } ?>></td>
                </tr>
                <tr>
                  <td><span>Move Storage Slot</span></td>
                  <td><input type="checkbox" name="moveStorageSlot" disabled <?php if($row['moveStorageSlot']) { echo "checked"; } ?>></td>
                </tr>
              </tbody>
            </table>
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

<?php
    }
    else {
      header("Location: home.php");
		  exit();
    }
?>