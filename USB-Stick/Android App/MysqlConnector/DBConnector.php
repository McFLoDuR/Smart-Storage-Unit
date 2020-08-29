<?php

$Error1 = "Error1: No database connection";
$Error2 = "Error2: Wrong method!";
$method = $_POST['method'];

switch ($method) {
    case "users":
        $con = getDBConnection();
        getData($con, "SELECT * FROM users");
        break;
    case "checkpass":
        $con = getDBConnection();
        checkPassword($con);
        break;
    case "setSignedIn":
        $con = getDBConnection();
        $id = $_POST['id'];
        $state = $_POST['state'];
        updateData($con, "UPDATE users SET userSignedIn=$state WHERE ID=$id");
        break;
    case "overview":
        $con = getDBConnection();
        getData($con, "SELECT cmpt.typeName, itm.articleNumber, SUM(sp.quantity), SUM(sp.alarmActivated),(SELECT COALESCE(SUM(quantityMin),0) FROM storagep sp WHERE sp.itemID=itm.ID) AS SUMquantityMin, itm.ID, itm.typeID, itm.weight FROM items itm, storagep sp, componenttypes cmpt WHERE (sp.itemID=itm.ID AND itm.typeID = cmpt.ID) GROUP BY sp.itemID ORDER BY SUM(sp.quantity) DESC");
        break;
    case "component":
        $con = getDBConnection();
        $id = $_POST['id'];
        getData($con, "SELECT * FROM componenttypes WHERE id = $id");
        break;
    case "componentTypeList":
        $con = getDBConnection();
        getData($con, "SELECT * FROM componenttypes GROUP BY typeName");
        break;
    case "componentVersionList":
        $con = getDBConnection();
        $type = $_POST['type'];
        getData($con, "SELECT * FROM componenttypes WHERE typeName='$type' GROUP BY typeVersion");
        break;
    case "componentList":
        $con = getDBConnection();
        getData($con, "SELECT * FROM componenttypes");
        break;
    case "itemdata":
        $con = getDBConnection();
        $id = $_POST['id'];
        getData($con, "SELECT ref.name, item.propertyValue, item.unit FROM referencenames ref, itemdata item WHERE item.itemID=$id AND item.referenceID=ref.ID");
        break;
    case "permission":
        $con = getDBConnection();
        $id = $_POST['id'];
        getData($con, "SELECT * FROM permissions WHERE ID=$id");
        break;
    case "storagep":
        $con = getDBConnection();
        $id = $_POST['id'];
        getData($con, "SELECT ID, storagehID, itemID ,insidePosition, quantity, quantityMax FROM storagep WHERE itemID=$id");
        break;
    case "storageh":
        $con = getDBConnection();
        $id = $_POST['id'];
        getData($con, "SELECT * FROM storageh WHERE ID=$id");
        break;
    case "storagehList":
        $con = getDBConnection();
        getData($con, "SELECT * FROM storageh sth WHERE (firstPartition+secondPartition+thirdPartition+1)>(SELECT COUNT(*) FROM storagep stp WHERE stp.storagehID=sth.ID)");
        break;
    case "storagepList":
        $con = getDBConnection();
        $id = $_POST['id'];
        getData($con, "SELECT ID, storagehID, itemID, insidePosition, quantity, quantityMax FROM storagep WHERE storagehID=$id ORDER BY insidePosition");
        break;
    case "activateLED":
        $con = getDBConnection();
        activateLED($con);
        break;
    case "deactivateLED":
        $con = getDBConnection();
        $id = $_POST['id'];
        updateData($con, "UPDATE activeLEDs set stateActivated=false, stateChanged=true WHERE SlotID=$id");
        break;
    case "updateQuantity":
        $con = getDBConnection();
        $id = $_POST['id'];
        $quantity = $_POST['quantity'];
        updateData($con, "UPDATE storagep SET quantity=$quantity WHERE ID=$id");
        break;
    case "updateDividers":
        $con = getDBConnection();
        $id = $_POST['id'];
        $first = $_POST['first'];
        $second = $_POST['second'];
        $third = $_POST['third'];
        updateData($con, "UPDATE storageh SET firstPartition=$first, secondPartition=$second, thirdPartition=$third WHERE ID=$id");
        break;
    case "insertStorageP":
        $con = getDBConnection();
        $storageID = $_POST['storagehId'];
        $itemID = $_POST['itemId'];
        $insidePos = $_POST['insidePos'];
        $quantity = $_POST['quantity'];
        $minQuantity = $_POST['minQuantity'];
        $maxQuantity = $_POST['maxQuantity'];
        $alarmAct = $_POST['alarmAct'];
        updateData($con, "INSERT INTO storagep(storagehID,itemID,insidePosition,quantity,quantityMin,quantityMax,alarmActivated) VALUES($storageID,$itemID,$insidePos,$quantity,$minQuantity,$maxQuantity,$alarmAct)");
        break;
    case "updateStorageP":
        $con = getDBConnection();
        $id = $_POST['id'];
        $insidePos = $_POST['insidePos'];
        $quantity = $_POST['quantity'];
        $maxQuantity = $_POST['maxQuantity'];
        updateData($con, "UPDATE storagep SET insidePosition=$insidePos,quantity=$quantity,quantityMax=$maxQuantity WHERE ID=$id");
        break;
    case "setStateScale":
        $con = getDBConnection();
        $id = $_POST['userID'];
        $state = $_POST['state'];
        updateData($con, "UPDATE stateStorage SET UserID=$id, stateActivated=$state, stateChanged=true WHERE ID=1");
        break;
    case "getScaleValue":
        $con = getDBConnection();
        getScaleValue($con);
        break;
    case "scaleInUse":
        $con = getDBConnection();
        isScaleInUse($con);
        break;
    case "setWeight":
        $con = getDBConnection();
        $id = $_POST['id'];
        $weight = $_POST['weight'];
        updateData($con, "UPDATE items SET weight=$weight WHERE ID=$id");
        break;
    case "reference":
        $con = getDBConnection();
        getData($con, "SELECT * FROM referencenames");
        break;
    case "unitList":
        $con = getDBConnection();
        getData($con, "SELECT unit FROM itemdata GROUP BY unit");
        break;
    case "newComponent":
        $con = getDBConnection();
        $type = $_POST['type'];
        $version = $_POST['version'];
        updateData($con, "INSERT INTO componenttypes(typeName,typeVersion) VALUES('$type','$version')");
        break;
    case "newItem":
        $con = getDBConnection();
        $id = $_POST['type'];
        $num = $_POST['article'];
        $weight = $_POST['weight'];
        $web = $_POST['web'];
        updateData($con, "INSERT INTO items(typeID,articleNumber,weight,weblink) VALUES($id,'$num',$weight,'$web')");
        break;
    case "getItemId":
        $con = getDBConnection();
        ItemId($con);
        break;
    case "newItemData":
        $con = getDBConnection();
        $itemId = $_POST['itemId'];
        $refId = $_POST['refId'];
        $value = $_POST['value'];
        $unit = $_POST['unit'];
        updateData($con, "INSERT INTO itemdata(itemID,referenceID,propertyValue,unit) VALUES($itemId,$refId,'$value','$unit')");
        break;
    case "insertRef":
        $con = getDBConnection();
        $name = $_POST['name'];
        updateData($con, "INSERT INTO referencenames(name) VALUES('$name')");
        break;
    case "getRefId":
        $con = getDBConnection();
        RefId($con);
        break;
    case "itemList":
        $con = getDBConnection();
        getData($con, "SELECT articleNumber FROM items");
        break;
    case "setAlarm":
        $con = getDBConnection();
        $id = $_POST['id'];
        $state = $_POST['state'];
        updateData($con, "UPDATE storagep set alarmActivated=$state WHERE itemID=$id");
        break;
    case "itemListData":
        $con = getDBConnection();
        getData($con, "SELECT cmpt.typeName, itm.articleNumber, itm.ID, itm.typeID, itm.weight, cmpt.typeVersion FROM items itm, componenttypes cmpt WHERE itm.typeID = cmpt.ID AND NOT itm.ID IN (SELECT itemID FROM storagep)");
        break;
    case "deleteStoragep":
        $con = getDBConnection();
        $posID = $_POST['posId'];
        updateData($con, "DELETE FROM storagep where ID=$posID");
        break;
    case "allStoragep":
        $con = getDBConnection();
        getData($con, "SELECT cmpt.typeName, itm.articleNumber, sp.quantity, sp.ID, sp.storagehID, sp.insidePosition, sp.quantityMax FROM items itm, storagep sp, componenttypes cmpt WHERE (sp.itemID=itm.ID AND itm.typeID = cmpt.ID) ORDER BY sp.itemID");
        break;
    case "allStorageBoxes":
        $con = getDBConnection();
        getData($con, "SELECT * FROM storageh");
        break;
    case "updateInsidePos":
        $con = getDBConnection();
        $id = $_POST['id'];
        $insidePos = $_POST['insidePos'];
        updateData($con, "UPDATE storagep set insidePosition=$insidePos WHERE ID=$id");
        break;
    case "report":
        $id = $_POST['id'];
        $mode = $_POST['mode'];
        shell_exec("python3 /home/ssu/Desktop/PDF-Creator/PDF_Creator.py --mode $mode --userID $id");
        break;
    default:
        die($Error2);
        break;
}

mysqli_close($con);

function updateData($con, $sql_stmt) {
    mysqli_query($con, $sql_stmt);
}

function RefId($con) {
    $name = $_POST['name'];
    $sql_stmt = "SELECT ID FROM referencenames WHERE name='$name'";
    $result = mysqli_query($con, $sql_stmt);
    $content = mysqli_fetch_assoc($result);
    echo $content['ID'];
}

function ItemId($con) {
    $num = $_POST['article'];

    $sql_stmt = "SELECT ID FROM items WHERE articleNumber='$num'";
    $result = mysqli_query($con, $sql_stmt);
    $content = mysqli_fetch_assoc($result);
    echo $content['ID'];
}

function activateLED($con) {
    $id = $_POST['id'];
    $color = $_POST['color'];
    $speed = $_POST['speed'];
    $activ = $_POST['activ'];
    $change = $_POST['change'];

    $sql_stmt = "INSERT INTO activeLEDs VALUES($id,'$color',$speed,$activ,$change)";

    $result = mysqli_query($con, $sql_stmt);

    if ($result == null) {
        die('false');
    }
    echo 'true';
}

function getScaleValue($con) {
    $sql_stmt = "SELECT stateValue FROM stateStorage WHERE ID=1";

    $result = mysqli_query($con, $sql_stmt);
    $content = mysqli_fetch_assoc($result);
    echo $content['stateValue'];
}

function isScaleInUse($con) {
    $sql_stmt = "SELECT UserID FROM stateStorage WHERE ID=1";

    $result = mysqli_query($con, $sql_stmt);
    $row = mysqli_fetch_assoc($result);
    if ($row['UserID'] != '0') {
        echo true;
    } else {
        echo false;
    }
}

function checkPassword($con) {
    $id = $_POST['id'];
    $password = hashPwd($_POST['password']);

    $sql_stmt = "SELECT * FROM users WHERE ID=? AND password=?";
    $stmt = mysqli_stmt_init($con);
    if (!mysqli_stmt_prepare($stmt, $sql_stmt)) {
        die("false");
    }
    mysqli_stmt_bind_param($stmt, "is", $id, $password);
    mysqli_stmt_execute($stmt);
    $result = mysqli_stmt_get_result($stmt);
    if ($row = mysqli_fetch_assoc($result)) {
        die("true");
    } else {
        die("false");
    }
}

function getData($con, $sql_stmt) {
    $result = mysqli_query($con, $sql_stmt);
    $data = array();
    while ($row = mysqli_fetch_assoc($result)) {
        array_push($data, $row);
    }

    foreach ($data as $indexRow) {
        foreach ($indexRow as $col) {
            echo $col;
            echo '|';
        }
        echo ';';
    }
}

function getDBConnection() {
    global $Error1;
    $host = "localhost";
    $user = "ssu_db";
    $pass = "ssu_FRS";
    $db = "ssu";

    $con = @mysqli_connect($host, $user, $pass, $db);

    if ($con == null) {
        die($Error1);
    }
    return $con;
}

function hashPwd($pwd) {
    for ($i = 0; $i < 5; $i++) {
        $pwd = strtoupper(hash("sha256", $pwd));
    }
    return $pwd;
}
