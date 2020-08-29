<?php
  if (!isset($legalRedirect_WithdrawQuantity)) {
    header("Location: home.php");
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
      <main id="withdrawQuantityMain">
        <div id="itemData">
          <p>Item Data of <?php echo $itemType; ?>:</p>
          <p><?php echo $itemArtNo; ?></p>
          <?php if ($noItemData) {echo "<p style='text-align: center; color: red; font-size: 20px;'><b>No item data.</b></p>";} 
                else {echo "
          <table>
            <tr>
              <th scope='col'>#</th>
              <th scope='col'>Reference Name</th>
              <th scope='col'>Value</th>
              <th scope='col'>Unit</th>
            </tr>";}
          ?>
            <?php 
              $i = 1;
              while($itemDataRow = mysqli_fetch_array($result))
              {
                $refname = $itemDataRow["name"];
                $propValue = $itemDataRow["propertyValue"];
                $propUnit = $itemDataRow["unit"];
              
                echo "<tr>";
                echo "<th scope='row'>$i</th>";
                echo "<td>$refname</td>";
                echo "<td>$propValue</td>";
                if ($propUnit == "none") {
                  echo "<td>-</td>";
                }
                else {
                  echo "<td>$propUnit</td>";
                }
                echo "</tr>";
            
                $i++;
              }
              if(!$noItemData) {echo "</table>";}
            ?>
        </div>
        <div id="chooseQuantity">
          <form action="withdrawItem.php" method="post">
            <label for="quantity">Select amount to withdraw</label><br><br>
            <select name="quantity" size="5" required>
              <?php
                for ($i=1; $i <= $_SESSION['itemQuantity']; $i++) { 
                  echo "<option value='$i'>$i</option>";
                }
              ?>
            </select>
            <br><br>
            <input type="submit" name="quantity-submit" value="Withdraw">
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