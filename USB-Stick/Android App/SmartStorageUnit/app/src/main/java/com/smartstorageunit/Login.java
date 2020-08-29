package com.smartstorageunit;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import tables.users;

import android.app.Dialog;
import android.content.Intent;
import android.graphics.Point;
import android.os.Bundle;
import android.text.TextUtils;
import android.text.method.PasswordTransformationMethod;
import android.view.Display;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

public class Login extends AppCompatActivity {
    boolean FingerprintAdded = false;
    boolean PasswordState = false;
    boolean ActivityChanged = false;
    users actUser = null;
    Dialog Popup = null;

    ConstraintLayout mainlayout;
    ConstraintLayout layout;
    TextView TxtTitle;
    TextView TxtLogin;
    TextView TxtUsername;
    TextView TxtPassword;
    TextView LblUsername;
    TextView LblPassword;
    TextView txtErrorMsg;
    CheckBox ChbShowPassword;
    TextView TxtWrongUP;
    Button BtnLogin;
    Button btnOk;
    ImageView ivLogo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_layout);

        PopupLoading.context = this;

        Point point = new Point();
        Display display = getWindowManager().getDefaultDisplay();
        display.getSize(point);
        ScaleElements.setHeight(point.y);
        ScaleElements.setWidth(point.x);

        mainlayout = findViewById(R.id.loginLayout);

        View userlogin = LayoutInflater.from(this).inflate(R.layout.content_user_login, null);
        mainlayout.addView(userlogin);
        layout = findViewById(R.id.userLoginLayout);
        layout.setMinHeight(ScaleElements.getHeight(100));
        layout.setMinWidth(ScaleElements.getWidth(100));

        TxtTitle = findViewById(R.id.txtTitleUser);
        TxtLogin = findViewById(R.id.txtLogin);
        TxtUsername = findViewById(R.id.txtUsername);
        TxtPassword = findViewById(R.id.txtPassword);
        LblUsername = findViewById(R.id.lbl_Username);
        LblPassword = findViewById(R.id.lbl_Password);
        ChbShowPassword = findViewById(R.id.chB_showPasswd);
        TxtWrongUP = findViewById(R.id.txtWrongUP);
        BtnLogin = findViewById(R.id.btnLogin_user);
        ivLogo = findViewById(R.id.ivLogo);

        setUserConstraints();
    }

    private void setUserConstraints() {
        ConstraintSet set = new ConstraintSet();
        set.clone(layout);

        set.connect(ivLogo.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(13));

        set.connect(TxtTitle.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(6));

        set.connect(TxtLogin.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(30));   //+10
        set.connect(TxtLogin.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(TxtUsername.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(40));
        set.connect(TxtUsername.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(LblUsername.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(44));
        set.connect(LblUsername.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(TxtPassword.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(55));
        set.connect(TxtPassword.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(LblPassword.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(59));
        set.connect(LblPassword.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(ChbShowPassword.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(65));
        set.connect(ChbShowPassword.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(TxtWrongUP.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(70));
        set.connect(TxtWrongUP.getId(), ConstraintSet.LEFT, layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));

        set.connect(BtnLogin.getId(), ConstraintSet.TOP, layout.getId(), ConstraintSet.TOP, ScaleElements.getHeight(87));

        set.applyTo(layout);
    }

    public void btnLoginUserClicked(View view) {
        TxtWrongUP.setVisibility(View.INVISIBLE);

        if (TextUtils.isEmpty(LblUsername.getText())) {
            LblUsername.setError("Username required!");
        }
        if (TextUtils.isEmpty(LblPassword.getText())) {
            LblPassword.setError("Password required!");
        } else {
            PopupLoading.startDialog();
            new Thread() {
                @Override
                public void run() {
                    List<users> list = DataHandler.getUsersData();
                    if (list == null) {
                        PopupLoading.stopDialog();
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Toast.makeText(Login.this, "Please try again!", Toast.LENGTH_SHORT).show();
                            }
                        });
                        return;
                    }
                    for (users u : list) {
                        if (u.getUsername().contentEquals(LblUsername.getText())) {
                            actUser = u;
                            clipboard.User = actUser;
                            clipboard.Permission = DataHandler.getPermission(actUser.getPermissionID()).get(0);
                            break;
                        }
                    }
                    if (actUser != null) {
                        if (DataHandler.checkPassword(actUser.getId(), LblPassword.getText().toString())) {
                            if (!actUser.isUserSignedIn()) {
                                LoginComplete();
                            } else {
                                PopupLoading.stopDialog();
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        showPopup();
                                    }
                                });
                            }
                        } else {
                            displayWrongUP();
                        }
                    } else {
                        displayWrongUP();
                    }
                }
            }.start();
        }
    }

    private void displayWrongUP() {
        PopupLoading.stopDialog();
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                TxtWrongUP.setVisibility(View.VISIBLE);
                LblPassword.setText("");
                LblUsername.setText("");
            }
        });
    }

    private void showPopup() {
        Popup = new Dialog(this);
        Popup.setContentView(R.layout.popup_already_login);
        txtErrorMsg = Popup.findViewById(R.id.txtErrorMsg);
        txtErrorMsg.setText("You're already logged in somewhere else!");
        btnOk = Popup.findViewById(R.id.btnOk);
        btnOk.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Popup.dismiss();
            }
        });
        Popup.setCancelable(false);
        Popup.show();
    }

    public void onChbShowPasswordClicked(View view) {
        if (!PasswordState) {
            LblPassword.setTransformationMethod(null);
        } else {
            LblPassword.setTransformationMethod(new PasswordTransformationMethod());
        }
        PasswordState = !PasswordState;
    }

    private void LoginComplete() {
        PopupLoading.stopDialog();
        ActivityChanged = true;
        new Thread() {
            @Override
            public void run() {
                DataHandler.setSignedIn(actUser.getId(),true);
            }
        }.start();
        Intent overview = new Intent(this, WindowController.class);
        startActivity(overview);
        finish();
    }

    @Override
    public void onBackPressed() {
        ActivityChanged = true;
        super.onBackPressed();
    }

    @Override
    protected void onDestroy() {
        if (!ActivityChanged) {
            PopupLoading.stopDialog();
        }
        if (Popup != null) {
            Popup.dismiss();
        }
        super.onDestroy();
    }

}
