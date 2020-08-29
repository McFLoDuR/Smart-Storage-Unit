<?php

if ((!isset($legalRedirect_Home)) && (!isset($legalRedirect_storeItem)) && (!isset($legitRedirect_Results))) {
	header("Location: ../login.php?redir=ect");
	exit();
}
else {
    $legalRedirect_dbh = true;
    require_once 'dbh-inc.php';

    $sql = "SELECT itm.ID, cmpt.typeName, cmpt.typeVersion, itm.articleNumber, SUM(sp.quantity) AS quantity
			FROM items itm, storagep sp, componenttypes cmpt
			WHERE (sp.itemID = itm.ID AND itm.typeID = cmpt.ID)
			GROUP BY sp.itemID
			ORDER BY SUM(sp.quantity) DESC, cmpt.typeName ASC, itm.articleNumber ASC";
	if (isset($resultspage)) {
		$sql = "SELECT itm.ID, cmpt.typeName, cmpt.typeVersion, itm.articleNumber, SUM(sp.quantity) AS quantity " .
				"FROM items itm, storagep sp, componenttypes cmpt " .
				"WHERE (sp.itemID = itm.ID AND itm.typeID = cmpt.ID) AND " .
				"(cmpt.typeName LIKE '$searchString%' OR itm.articleNumber LIKE '$searchString%' OR cmpt.typeVersion LIKE '$searchString%')" .
				"GROUP BY sp.itemID ORDER BY SUM(sp.quantity) DESC, cmpt.typeName ASC, itm.articleNumber ASC";
	}
	if(isset($showAllItems)) {
		$sql = "SELECT itm.ID, " .
				"(SELECT COALESCE(SUM(sp.alarmActivated), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS alarmActivated, " .
				"(SELECT COALESCE(SUM(sp.quantityMin), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS quantityMin, " .
				"cmpt.typeName, cmpt.typeVersion, itm.articleNumber, " .
				"(SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID) AS quantity " .
				"FROM items itm, componenttypes cmpt " .
				"WHERE itm.typeID = cmpt.ID " .
				"GROUP BY itm.ID " .
				"ORDER BY (SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID) DESC, itm.articleNumber ASC";
	}
    
    if(!$result = mysqli_query($conn, $sql)) {
        header("Location: ../home.php?error=sqlerror");
        exit();
    }
    else {
		if (mysqli_num_rows($result) == 0) {
			header("Location: ../home.php?error=noitems");
			exit();
		}
		else {
			echo "<table>";
			echo "<tr>
			  <th scope='col'>#</th>
			  <th scope='col'>Component</th>
			  <th scope='col'>Type</th>
			  <th scope='col'>Article No.</th>
			  <th scope='col'>Quantity</th>
			  </tr>";
			
			$i = 1;
			while ($row = mysqli_fetch_array($result)) {
				
				$itemID = $row["ID"];
				$itemTypeName = $row["typeName"];
				$itemTypeVersion = $row["typeVersion"];
				$itemArtNo = $row["articleNumber"];
				$itemQuantity = $row["quantity"];
			
				echo "<tr id='$itemID' onClick='getRow(this.id)'>";
				echo "<th scope='row'>$i</th>";
				echo "<td>$itemTypeName</td>";
				echo "<td>$itemTypeVersion</td>";
				echo "<td>$itemArtNo</td>";
				echo "<td>$itemQuantity</td>";
				echo "</tr>";
				
				$i++;
			}
			echo "</table>";
		}
	}
}

?>