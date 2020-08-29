<?php
    session_start();
    $legalRedirect_dbh = true;
    require_once 'dbh-inc.php';

    if (!isset($_SESSION['username'])) {
        header("Location: ../login.php?redir=ect");
        exit();
    }

    if((!isset($_POST['divider1'])) && (!isset($_POST['divider2'])) && (!isset($_POST['divider3']))) {
        $sql="UPDATE storageh SET firstPartition=0, secondPartition=0, thirdPartition=0 WHERE storagePosition=".$_SESSION['storagehslot'];
    }
    else{
        if(isset($_POST['divider1'])) {
            $sql="UPDATE storageh SET firstPartition=1 WHERE storagePosition=".$_SESSION['storagehslot'];
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
        }
        else {
            $sql="UPDATE storageh SET firstPartition=0 WHERE storagePosition=".$_SESSION['storagehslot'];
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
        }
        if(isset($_POST['divider2'])) {
            $sql="UPDATE storageh SET secondPartition=1 WHERE storagePosition=".$_SESSION['storagehslot'];
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
        }
        else {
            $sql="UPDATE storageh SET secondPartition=0 WHERE storagePosition=".$_SESSION['storagehslot'];
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
        }
        if(isset($_POST['divider3'])) {
            $sql="UPDATE storageh SET thirdPartition=1 WHERE storagePosition=".$_SESSION['storagehslot'];
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
        }
        else {
            $sql="UPDATE storageh SET thirdPartition=0 WHERE storagePosition=".$_SESSION['storagehslot'];
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
        }
    }

    $sql="SELECT * FROM storageh WHERE storagePosition=".$_SESSION['storagehslot'];
    if(!mysqli_query($conn, $sql)) {
        header("Location: ../home.php?error=sqlerror");
        exit();
    }
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_array($result);
    $dividersum = $row['firstPartition'] + $row['secondPartition'] + $row['thirdPartition'];
    if($dividersum == 0 && $_POST['position']>1) {
        header("Location: ../home.php?error=invalidpos");
        exit();
    }
    elseif ($dividersum == 1 && $_POST['position']>2) {
        header("Location: ../home.php?error=invalidpos");
        exit();
    }
    elseif ($dividersum == 2 && $_POST['position']>3) {
        header("Location: ../home.php?error=invalidpos");
        exit();
    }

    if(isset($_SESSION['sthfound'])) {
        $newquant = $_SESSION['storeQuantity'] + $_SESSION['quantityStored'];
        $sql = "UPDATE storagep SET alarmactivated=".$_POST['alarmactivated'].", quantityMin=".$_POST['quantityMin'].
        ", quantityMax=".$_POST['quantityMax'].", quantity=$newquant WHERE storagehID=".$_SESSION['storagehslot'].
        " AND itemID=".$_SESSION['itemid']." AND insidePosition=".$_POST['position'];
    }
    else {
        $sql = "INSERT INTO storagep (storagehID, itemID, insidePosition, quantity, quantityMin, quantityMax, alarmActivated) ".
            "VALUES (".$_SESSION['storagehslot'].", ".$_SESSION['itemid'].", ".$_POST['position'].", ".
            $_SESSION['storeQuantity'].", ".$_POST['quantityMin'].", ".$_POST['quantityMax'].", ".$_POST['alarmactivated'].")";
    }
    if(!mysqli_query($conn, $sql)) {
        header("Location: ../home.php?error=sqlerror");
        exit();
    }

    $sql = "UPDATE activeLEDs SET stateActivated=0, stateChanged=1 WHERE SlotID = " . $_SESSION['storagehslot'];
    if(!mysqli_query($conn, $sql)) {
      header("Location: ../home.php?error=sqlerror");
      exit();
    }

    header("Location: ../home.php?success=store");
    exit();
?>