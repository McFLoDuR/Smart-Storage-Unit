package com.smartstorageunit;

import android.widget.Button;
import android.widget.TextView;

import java.util.TimerTask;

public class CheckWeight extends TimerTask {

    private TextView TxtResult;
    private TextView TxtCount;
    private Button BtnOk;
    private int MaxCount=0;
    private double ItemWeight=0;

    public CheckWeight(TextView txt) {
        TxtResult=txt;
    }

    public CheckWeight(TextView txtResult, TextView txtCount, Button btnOk, int maxCount, double itemWeight) {
        TxtResult = txtResult;
        TxtCount = txtCount;
        BtnOk = btnOk;
        MaxCount = maxCount;
        ItemWeight = itemWeight;
    }

    @Override
    public void run() {
        final String result = DataHandler.getScaleValue();
        final double weight = Double.parseDouble(result);
        final int count;
        if(MaxCount != 0){
            count = (int)(weight/ItemWeight);
        }
        else {
            count=0;
        }
        TxtResult.post(new Runnable() {
            @Override
            public void run() {
                TxtResult.setText(result+"g");
                if(MaxCount!=0){
                    TxtCount.setText(count+"/"+MaxCount+" Items");
                    if(count==MaxCount){
                        BtnOk.setEnabled(true);
                    }
                    else {
                        BtnOk.setEnabled(false);
                    }
                }
            }
        });
    }
}
