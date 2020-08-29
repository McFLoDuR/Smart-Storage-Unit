<?php
    session_start();
    $legalRedirect_dbh = true;
    require_once 'dbh-inc.php';

    if (!isset($_SESSION['username'])) {
        header("Location: ../login.php?redir=ect");
        exit();
    }

    $sql = "UPDATE activeLEDs SET stateActivated=0, stateChanged=1 WHERE SlotID = " . $_SESSION['prevSTHID'];
    if(!mysqli_query($conn, $sql)) {
      header("Location: ../home.php?error=sqlerror");
      exit();
    }
    if(isset($_SESSION['numsth'])) {
        $sql = "SELECT * FROM storagep WHERE itemID=" . $_SESSION['itemid'] . " ORDER BY quantity ASC";
        if(!mysqli_query($conn, $sql)) {
            header("Location: ../home.php?error=sqlerror");
            exit();
        }
        $result = mysqli_query($conn, $sql);
        $quant = $_SESSION['quantityWithdrawn'];
        $sthcounter = 1;
        while(($row = mysqli_fetch_array($result)) && $quant > 0) {
            if(($_SESSION['numsth'] == $sthcounter) || ($row['quantity'] > $quant)) {
                $sql = "UPDATE storagep SET quantity =" . ($row['quantity']-$quant) . " WHERE ID=" . $row['ID'];
                $quant = 0;
            }
            elseif($row['quantity'] <= $quant) {
                $sql = "DELETE FROM storagep WHERE ID=" . $row['ID'];
                $quant -= $row['quantity'];
            }
            if(!mysqli_query($conn, $sql)) {
                header("Location: ../home.php?error=sqlerror");
                exit();
            }
            $sthcounter++;
        }
    }
    else {
        $sql = "SELECT * FROM storagep WHERE itemID=" . $_SESSION['itemid'] . " ORDER BY quantity ASC";
        if(!mysqli_query($conn, $sql)) {
            header("Location: ../home.php?error=sqlerror");
            exit();
        }
        $result = mysqli_query($conn, $sql);
        $row = mysqli_fetch_array($result);

        if($row['quantity'] <= $_SESSION['quantityWithdrawn']) {
            $sql = "UPDATE storagep SET quantity = 0 WHERE ID=" . $row['ID'];
        }
        else {
            $sql = "UPDATE storagep SET quantity =" . ($row['quantity']-$_SESSION['quantityWithdrawn']) . " WHERE ID=" . $row['ID'];
        }
        if(!mysqli_query($conn, $sql)) {
            header("Location: ../home.php?error=sqlerror");
            exit();
        }
    }

    header("Location: ../home.php?success=withdraw");
    exit();
?>