<?php
    session_start();
    if(isset($_POST['profile-save'])) {
        require_once 'lib-inc.php';

        $legalRedirect_dbh = true;
        require_once 'dbh-inc.php';
        
        $username = $_SESSION['username'];
        $userID = $_SESSION['userID'];
        $oldEmail = $_SESSION['email'];
		$oldColor = $_SESSION['color'];
		$mNotif = $_SESSION['mNotif'];
		$signedIn = $_SESSION['signedIn'];
        $permID = $_SESSION['permID'];
        
        $pwd = $_POST['oldPwd'];
        $newpwd = $_POST['newPwd'];
        $newpwd_repeat = $_POST['newPwd-repeat'];
        $newColor = $_POST['ledColor'];
        $newEmail = $_POST['newEmail'];
        $newMonthNotif = ($_POST['notif'] == "yes") ? 1 : 0 ;
        
        $sql = "SELECT * FROM users WHERE username=? AND password=? LIMIT 1";
        $stmt = mysqli_stmt_init($conn);
        if (mysqli_stmt_prepare($stmt, $sql)) {
            $hashedPwd = hashPwd($pwd);
            mysqli_stmt_bind_param($stmt, "ss", $username, $hashedPwd);
            mysqli_stmt_execute($stmt);
            $result = mysqli_stmt_get_result($stmt);
            if (mysqli_fetch_array($result)) {
                //
                //New Password
                //
                if(!empty($newpwd) && empty($newpwd_repeat)) {
                    header("Location: ../profile.php?error=repeatpwd");
                    exit();
                }
                elseif (empty($newpwd) && !empty($newpwd_repeat)) {
                    header("Location: ../profile.php?error=repeatpwd");
                    exit();
                }
                elseif(!empty($newpwd) && !empty($newpwd_repeat)) {
                    if($newpwd == $newpwd_repeat)
                    {
                        $sql = "UPDATE users SET password='" . hashPwd($newpwd) . "' WHERE ID=" . (int)$userID;
                        if(!mysqli_query($conn, $sql)) {
                            header("Location: ../profile.php?error=sqlerror");
                            exit();
                        }
                    }
                    else {
                        header("Location: ../profile.php?error=invalidRepeat");
                        exit();
                    }
                }

                //
                //New Email
                //
                if(!empty($newEmail)) {
                    $sql = "UPDATE users SET email=? WHERE ID=?";
                    $stmt = mysqli_stmt_init($conn);

                    if (!mysqli_stmt_prepare($stmt, $sql)) {
                        header("Location: ../profile.php?error=sqlerror");
                        exit();
                    }
                    else {
                        $userID_int = (int)$userID;
                        mysqli_stmt_bind_param($stmt, "si", $newEmail, $userID_int);
                        if(!mysqli_stmt_execute($stmt)) {
                            header("Location: ../profile.php?error=sqlerror");
                            exit();
                        }
                        $_SESSION['email'] = $newEmail;
                    }
                }

                //
                //New LED-Color
                //
                $sql = "SELECT * FROM users ORDER BY ID";
                if(!mysqli_query($conn, $sql)) {
                    header("Location: ../profile.php?error=sqlerror");
                    exit();
                }
                else {
                    $colortaken = false;
                    $result = mysqli_query($conn, $sql);
                    $numRows =  mysqli_num_rows($result);
                    for ($i=1; $i <= $numRows; $i++) { 
                        $loopSql = "SELECT * FROM users WHERE ID=$i";
                        $loopResult =  mysqli_query($conn, $loopSql);
                        
                        if(!$loopResult) {
                            header("Location: ../profile.php?error=sqlerror");
                            exit();
                        }
                        else {
                            $row = mysqli_fetch_array($loopResult);
                            if(colorComp($newColor, $row['color']) && $i != $userID) {
                                $colortaken = true;
                            }
                        }
                    }
                    if($colortaken == true) {
                        header("Location: ../profile.php?error=colortaken");
                        exit();
                    }
                    $setColor = strtoupper(substr($newColor, 1));
                    $sql = "UPDATE users SET color='$setColor' WHERE ID=" . (int)$userID;
                    if(!mysqli_query($conn, $sql)) {
                        header("Location: ../profile.php?error=sqlerror");
                        exit();
                    }
                    $_SESSION['color'] = $setColor;
                }

                //
                //Monthly Notification
                //
                $sql = "UPDATE users SET monthlyNotification=" . $newMonthNotif . " WHERE ID=" . (int)$userID;
                if (!mysqli_query($conn, $sql)) {
                    header("Location: ../profile.php?error=sqlerror");
                    exit();
                }
                $_SESSION['mNotif'] = $newMonthNotif;
                header("Location: ../profile.php?success=ful");
                exit();
            }
            else {
                header("Location: ../profile.php?error=invalid");
                exit();
            }
        }
        else {
            header("Location: ../profile.php?error=sqlerror");
            exit();
        }
    }
    else {
        header("Location ../profile.php");
        exit();
    }