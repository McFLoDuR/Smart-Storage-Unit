<?php
    if(isset($legalRedirect_Profile)) {
      $sql = "SELECT * FROM users WHERE username ='" . $_SESSION['username'] . "'";
      if(!mysqli_query($conn, $sql)) {
          header("Location: profile.php?error=sqlerror");
          exit();
      }
      $result = mysqli_query($conn, $sql);
      $row = mysqli_fetch_array($result);
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
      <main id="profileMain">
        <h2 class="profileHeading">Manage Profile</h2>
        <h4 class="profileHeading">Change Password/Email/Personal-Color</h4>
        <hr>
        <form id="profileForm" action="includes/profile-inc.php" method="post">
          <div>
            <?php
              if($changed) {echo "<span class='feedbackMsg'>Successfully changed.</span>";}
              elseif($repeatPwd) {echo "<span class='feedbackMsg'>Please repeat the new password.</span>";}
              elseif($invalidRepeat) {echo "<span class='feedbackMsg'>Repeated password did not match new password.</span>";}
              elseif($sqlerror) {echo "<span class='feedbackMsg'>There was a database error.</span>";}
              elseif($invalid) {echo"<span class='feedbackMsg'>Old password incorrect.</span>";}
              elseif ($colortaken) {echo"<span class='feedbackMsg'>This colour is already taken.</span>";}
            ?>
            <table>
            <tr>
              <td><span>Old Password:</span></td>
              <td><input type="password" name="oldPwd" required></td>
            </tr>
            <tr>
              <td><span>New Password:</span></td>
              <td><input type="password" name="newPwd" minlength="8" maxlength="16" ><br></td>
            </tr>
            <tr>
              <td><span>Repeat New Password:</span></td>
              <td><input type="password" name="newPwd-repeat"><br></td>
            </tr>
            <tr>
              <td><span>New Email Address:</span></td>
              <td><input type="email" name="newEmail" maxLength="80"><br></td>
            </tr>
            <tr>
              <td><span>Personal Colour:</span></td>
              <td><input type="color" name="ledColor" value="<?php echo "#" . $row['color']; ?>"></td>
            </tr>
            <tr>
              <td><span>Monthly inventory report:</span></td>
              <td id="radiotd">
                Yes<input class="radbtn" type="radio" name="notif" value="yes" <?php if($row['monthlyNotification']) { echo "checked"; } ?>>
                <input class="radbtn" type="radio" name="notif" value="no" <?php if(!$row['monthlyNotification']) { echo "checked"; } ?>>No
              </td>
            </tr>
              <tr>
                <td><button type="submit" formaction="home.php" form="logoutForm">Cancel</button></td>
                <td><input type="submit" name="profile-save" value="Save"></td>
              </tr>
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
        header("Location: ../home.php");
		exit();
    }
?>