<?php

//Hashes the given password ($pwd) 5 times with the sha256 method and returns the last hash
function hashPwd($pwd) {
    for ($i=0; $i < 5; $i++) { 
        $pwd = strtoupper(hash("sha256", $pwd));
    }
    return $pwd;
}

/*
Returns true if colorA in range of colorB (range defined by $diff)
$colorA and $colorB are strings (pattern: #xxxxxx with x being a hex digit (0-F))
*/
function colorComp($colorA, $colorB) {
    $diff = 100;
    $colorA = strtoupper($colorA);
    $colorB = strtoupper($colorB);
    $r_str = hexdec(substr($colorA, 1, 2)) - hexdec(substr($colorB, 1, 2));
    $g_str = hexdec(substr($colorA, 3, 2)) - hexdec(substr($colorB, 3, 2));
    $b_str = hexdec(substr($colorA, 5, 2)) - hexdec(substr($colorB, 5, 2));
    $r = (int)$r_str;
    $g = (int)$g_str;
    $b = (int)$b_str;

    $retVal = ((($r*$r) + ($g*$g) + ($b*$b)) <= ($diff*$diff)) ? true : false;
    return $retVal;
}

/*
Echoes the ending of the correct img file with the correct marked area 
representing the storage slot and position
*/
function withdrawItemStorageSlotImg($storagehRow, $storagepRow) {
    echo $storagehRow['firstPartition'] . $storagehRow['secondPartition'] . $storagehRow['thirdPartition'] . "_";
    $amountPartitions = $storagehRow['firstPartition'] + $storagehRow['secondPartition'] + $storagehRow['thirdPartition'];
    if($amountPartitions == 0) {
        echo "1111";
    }
    elseif ($amountPartitions < 3) {
        if ($storagehRow['firstPartition']) {
            if($storagehRow['secondPartition']) {
                if($storagepRow['insidePosition'] == 1) {
                    echo "1000";
                }
                elseif($storagepRow['insidePosition'] == 2) {
                    echo "0100";
                }
                elseif($storagepRow['insidePosition'] == 3) {
                    echo "0011";
                }
            }
            elseif($storagehRow['thirdPartition']) {
                if($storagepRow['insidePosition'] == 1) {
                    echo "1000";
                }
                elseif($storagepRow['insidePosition'] == 2) {
                    echo "0110";
                }
                elseif($storagepRow['insidePosition'] == 3) {
                    echo "0001";
                }
            }
            else {
                if($storagepRow['insidePosition'] == 1) {
                    echo "1000";
                }
                else {
                    echo "0111";
                }
            }
        }
        elseif ($storagehRow['secondPartition']) {
            if ($storagehRow['thirdPartition']) {
                if($storagepRow['insidePosition'] == 1) {
                    echo "1100";
                }
                elseif($storagepRow['insidePosition'] == 2) {
                    echo "0010";
                }
                elseif($storagepRow['insidePosition'] == 3) {
                    echo "0001";
                }
            }
            else {
                if($storagepRow['insidePosition'] == 1) {
                    echo "1100";
                }
                else {
                    echo "0011";
                }
            }
        }
        elseif($storagehRow['thirdPartition']) {
            if($storagepRow['insidePosition'] == 1) {
                echo "1110";
            }
            else {
                echo "0001";
            }
        }
    }
    elseif ($amountPartitions == 3) {
        if($storagepRow['insidePosition'] == 1) {
            echo "1000";
        }
        elseif($storagepRow['insidePosition'] == 2) {
            echo "0100";
        }
        elseif($storagepRow['insidePosition'] == 3) {
            echo "0010";
        }
        elseif($storagepRow['insidePosition'] == 4) {
            echo "0001";
        }
    }
}

/*
Echoes the correct part of the instruction text depending on the amount of items to withdraw
*/
function withdrawInstructionAmount($withdrawQuantity, $storagepQuantity) {
    if($withdrawQuantity >= $storagepQuantity) {
        echo "all items";
        return $withdrawQuantity-$storagepQuantity;
    }
    elseif($withdrawQuantity > 1) {
        echo $withdrawQuantity . " items";
        return 0;
    }
    else {
        echo "one item";
        return 0;
    }
}

/*
Routine of checking the userSignedIn column in the users table
(logout script:)Logs out and redirects to login.php?error=busy when userSignedIn=1, exits the script
If userSignedIn=0, the function does nothing and lets the followed code execute, does not exit the script
$logoutphpLocation: the path to the logout-inc.php file relative to the file the function is called in
$sessionId: the $_SESSION['ID'] variable of active session
*/
function checkIfSignedIn ($logoutphpLoc) {              //TODO: debug, because it still doesn't work (probably because of dbh conn)
    $legalRedirect_dbh = true;
    require 'dbh-inc.php';
    
    if (isset($_SESSION['userID'])) {
        $sql = "SELECT * FROM users WHERE ID=" . $_SESSION['userID'];
        $result = mysqli_query($conn, $sql);
        if(!$result) {
            header("Location: login.php?error=sqlerror");
            exit();
        }
        else {
            $row = mysqli_fetch_array($result);
            $userSignedIn = $row['userSignedIn'];
            if(!$userSignedIn) {                         //idk why i had to negate the value. if i didnt do it it didnt work
                header("Location: $logoutphpLoc?busy=true");
                exit();
            }
        }
    }
}

?>