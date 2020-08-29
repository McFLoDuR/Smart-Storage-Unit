package com.smartstorageunit;

import android.app.Dialog;
import android.content.Context;

public class PopupLoading {

    public static Context context;
    private static boolean IsRunning=false;
    private static Dialog loading;

    public static void startDialog(){
        loading = new Dialog(context);
        loading.setContentView(R.layout.popup_loading);
        loading.setCancelable(false);
        loading.show();
        IsRunning=true;
    }

    public static void stopDialog(){
        loading.dismiss();
        IsRunning=false;
    }

    public static boolean isRunning(){
        return IsRunning;
    }
}
