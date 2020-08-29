package com.smartstorageunit;

import androidx.constraintlayout.widget.ConstraintLayout;

public class ScaleElements {

    private static int Width;
    private static int Height;

    public static void setWidth(int width){Width=width;}
    public static void setHeight(int height){Height=height;}


    public static int getWidth(int percent) {
        return Width*percent/100;
    }
    public static int getHeight(int percent){
        return Height*percent/100;
    }
}
