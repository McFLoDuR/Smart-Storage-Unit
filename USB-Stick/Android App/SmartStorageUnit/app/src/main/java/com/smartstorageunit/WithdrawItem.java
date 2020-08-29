package com.smartstorageunit;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import tables.storageBox;
import tables.storagePosition;

import android.app.Dialog;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.NumberPicker;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Timer;

public class WithdrawItem extends AppCompatActivity {

    Toolbar TbStorageBox;
    ImageView IvStorageBox;
    ImageView IvColor;
    TextView TxtLabel;
    TextView TxtColor;
    TextView TxtPosition;
    Button BtnWithdraw;
    Button BtnPrev;
    Button BtnNext;
    Spinner SpPosition;
    ConstraintLayout Layout;
    CheckBox[] CbDivider = new CheckBox[3];
    TextView[] ItemArea=null;

    Timer TimerCheckWeight;
    CheckWeight TaskCheckWeight;

    boolean MicroScaleSet=false;
    boolean ActivityChanged=false;
    boolean DeleteLastPos=true;
    boolean NextClicked=false;
    boolean PrevClicked=false;
    boolean ScaleInUse=false;
    int Quantity;
    int LastPosQuantity;
    int MaxBoxCounter;
    int BoxCounter=0;
    int ItemAreaPos=0;

    float x1,x2,dx;

    int[] sectors;

    Dialog PopupMicorscale = null;
    Dialog PopupInfo = null;

    List<storagePosition> WithdrawList=new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.storage_box);

        Quantity = getIntent().getIntExtra("quantity",0);

        TbStorageBox = findViewById(R.id.tbStorageBoxSW);
        IvStorageBox = findViewById(R.id.ivStorageBox);
        IvColor = findViewById(R.id.ivColor);
        TxtColor = findViewById(R.id.txtStorageBoxColor);
        TxtLabel = findViewById(R.id.txtStorageBoxTitle);
        TxtPosition = findViewById(R.id.txtPostition);
        Layout = findViewById(R.id.layoutStorageBox);
        BtnWithdraw = findViewById(R.id.btnStore);
        BtnPrev = findViewById(R.id.btnPrev);
        BtnNext = findViewById(R.id.btnNext);
        SpPosition = findViewById(R.id.spPosition);
        CbDivider[0] = findViewById(R.id.cbDiv1);
        CbDivider[1] = findViewById(R.id.cbDiv2);
        CbDivider[2] = findViewById(R.id.cbDiv3);

        TbStorageBox.setTitleTextColor(Color.WHITE);

        IvColor.setColorFilter(Color.parseColor("#"+clipboard.User.getColor()));

        TbStorageBox.setTitle("Location of items");
        setSupportActionBar(TbStorageBox);
        TbStorageBox.setNavigationIcon(R.drawable.back_arrow);
        TbStorageBox.setNavigationOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ActivityChanged=true;
                deactivateLED();
                finish();
            }
        });

        for(CheckBox cb:CbDivider){
            cb.setEnabled(false);
        }

        SpPosition.setVisibility(View.INVISIBLE);
        TxtPosition.setVisibility(View.INVISIBLE);
        BtnWithdraw.setText("Withdraw");

        setConstraints();
        initSectors();
        initializeStorageBox();
    }

    private void setConstraints(){
        ConstraintSet set = new ConstraintSet();
        set.clone(Layout);

        set.connect(TxtLabel.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));

        set.connect(TxtColor.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(4));

        set.connect(IvColor.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(8));

        set.connect(IvStorageBox.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT);
        set.connect(IvStorageBox.getId(),ConstraintSet.RIGHT,Layout.getId(),ConstraintSet.RIGHT);
        set.connect(IvStorageBox.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP);
        set.connect(IvStorageBox.getId(),ConstraintSet.BOTTOM,Layout.getId(),ConstraintSet.BOTTOM);

        set.connect(BtnWithdraw.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(80));

        set.connect(BtnPrev.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(1));
        set.connect(BtnPrev.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(70));

        set.connect(BtnNext.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(82));
        set.connect(BtnNext.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(70));

        set.connect(CbDivider[0].getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(32));
        set.connect(CbDivider[0].getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(75));

        set.connect(CbDivider[1].getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(41));
        set.connect(CbDivider[1].getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(75));

        set.connect(CbDivider[2].getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(51));
        set.connect(CbDivider[2].getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(75));

        set.connect(TxtPosition.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(76));
        set.connect(TxtPosition.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(30));

        set.connect(SpPosition.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(76));
        set.connect(SpPosition.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(50));

        set.applyTo(Layout);

    }

    private void initSectors(){
        sectors = new int[8];
        sectors[0] = ScaleElements.getHeight(19);
        sectors[1] = ScaleElements.getHeight(14);
        sectors[2] = ScaleElements.getHeight(1)+sectors[1];
        sectors[3] = ScaleElements.getHeight(9)+sectors[2];
        sectors[4] = ScaleElements.getHeight(1)+sectors[3];
        sectors[5] = ScaleElements.getHeight(8)+sectors[4];
        sectors[6] = ScaleElements.getHeight(1)+sectors[5];
        sectors[7] = ScaleElements.getHeight(14)+sectors[6];
    }

    private void initializeStorageBox(){
        PopupLoading.context=this;
        PopupLoading.startDialog();
        new Thread(new Runnable() {
            @Override
            public void run() {
                int quantityCpy = Quantity;
                final List<storagePosition> storagepList = DataHandler.getStoragePositionData(clipboard.Overview.getItemID());
                Collections.sort(storagepList,new Comparator<storagePosition>(){
                    @Override
                    public int compare(storagePosition storagePosition, storagePosition t1) {
                        return Integer.compare(storagePosition.getQuantity(),t1.getQuantity());
                    }
                });
                for(storagePosition pos : storagepList){
                    quantityCpy-=pos.getQuantity();
                    LastPosQuantity = quantityCpy+pos.getQuantity();
                    WithdrawList.add(pos);
                    if(quantityCpy<=0){
                        break;
                    }
                }
                MaxBoxCounter = WithdrawList.size();
                if(WithdrawList.size()==storagepList.size()){
                    DeleteLastPos=false;
                }
                else {
                    DeleteLastPos=true;
                }
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if(MaxBoxCounter==1){
                            BtnNext.setVisibility(View.INVISIBLE);
                            BtnPrev.setVisibility(View.INVISIBLE);
                        }
                        else {
                            BtnWithdraw.setEnabled(false);
                            BtnPrev.setEnabled(false);
                        }
                    }
                });
                updateStorageBox();
                PopupLoading.stopDialog();
            }
        }).start();
    }

    private void updateStorageBox(){
        storageBox boxData = DataHandler.getStorageBoxData(WithdrawList.get(BoxCounter).getStorageID()).get(0);
        clipboard.StorageBox = boxData;
        clipboard.StoragePosition = WithdrawList.get(BoxCounter);
        final int[] partitions = {boxData.isFirstPartition()?1:0,boxData.isSecondPartition()?1:0,boxData.isThirdPartition()?1:0};
        String source = "storage_slot"+partitions[0]+partitions[1]+partitions[2];
        final int id = getResources().getIdentifier(source,"mipmap",getPackageName());

        if(!DataHandler.activateLED(clipboard.StorageBox.getStoragePosition(),clipboard.User.getColor(),3,true,true)){
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    if(MaxBoxCounter==1) {
                        ActivityChanged = true;
                        Toast.makeText(WithdrawItem.this, "Please wait! Someone else is using the storage slot!", Toast.LENGTH_LONG).show();
                        finish();
                    }
                    else {
                        if(NextClicked){
                            BoxCounter--;
                            NextClicked=false;
                        }
                        else if(PrevClicked){
                            BoxCounter++;
                            PrevClicked=false;
                        }
                    }
                }
            });
        }
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                IvStorageBox.setImageResource(id);

                CbDivider[0].setChecked(1==partitions[2]);
                CbDivider[1].setChecked(1==partitions[1]);
                CbDivider[2].setChecked(1==partitions[0]);
                if(BoxCounter!=(MaxBoxCounter-1)&&MaxBoxCounter!=1){
                    TxtLabel.setText("Please empty the marked space");
                }
                else if(LastPosQuantity>=20&&clipboard.Overview.getWeight()!=0&&clipboard.Overview.getWeight()!=1000){
                    TxtLabel.setText("Please press WITHDRAW to use the microscale");
                }
                else {
                    TxtLabel.setText("Please take "+LastPosQuantity+" item(s) out");
                }
                setMarkArea();
            }
        });
    }

    private void setMarkArea(){
        int insidePos=1;
        int height=0;
        List<Integer> areaList = new ArrayList<>();

        areaList.add(sectors[0]);

        if(clipboard.StorageBox.isThirdPartition()){
            insidePos+=1;
            areaList.add(sectors[1]+sectors[0]);
            areaList.add(sectors[2]+sectors[0]);
            height+=sectors[2];
        }
        if(clipboard.StorageBox.isSecondPartition()){
            insidePos+=1;
            areaList.add(sectors[3]+sectors[0]);
            areaList.add(sectors[4]+sectors[0]);
            height+=sectors[3];
        }
        if(clipboard.StorageBox.isFirstPartition()){
            insidePos+=1;
            areaList.add(sectors[5]+sectors[0]);
            areaList.add(sectors[6]+sectors[0]);
            height+=sectors[6];
        }
        areaList.add(sectors[7]+sectors[0]);

        ItemArea = new TextView[1];
        insidePos -= clipboard.StoragePosition.getInsidePosition();

        insidePos*=2;
        setMultiMark(areaList.get(insidePos),areaList.get(insidePos+1)-areaList.get(insidePos));        //2 3

    }

    private void setMultiMark(int startPos, int height){
        ItemArea[ItemAreaPos] = new TextView(WithdrawItem.this);
        ItemArea[ItemAreaPos].setId(View.generateViewId());
        ItemArea[ItemAreaPos].setForeground(new ColorDrawable(Color.parseColor("#A8cc0000")));
        ItemArea[ItemAreaPos].setLayoutParams(new ViewGroup.LayoutParams(IvStorageBox.getLayoutParams().width-80, height));
        Layout.addView(ItemArea[ItemAreaPos]);
        ConstraintSet set = new ConstraintSet();
        set.clone(Layout);
        set.connect(ItemArea[ItemAreaPos].getId(), ConstraintSet.TOP, Layout.getId(), ConstraintSet.TOP, startPos);
        set.connect(ItemArea[ItemAreaPos].getId(), ConstraintSet.LEFT, Layout.getId(), ConstraintSet.LEFT);
        set.connect(ItemArea[ItemAreaPos].getId(), ConstraintSet.RIGHT, Layout.getId(), ConstraintSet.RIGHT);
        set.applyTo(Layout);
    }

    private void deactivateLED(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                DataHandler.deactivateLED(clipboard.StorageBox.getStoragePosition());
            }
        }).start();
    }

    private void btnCheck(){
        if(BoxCounter==0){
            BtnPrev.setEnabled(false);
        }
        else if(BoxCounter==(MaxBoxCounter-1)){
            BtnNext.setEnabled(false);
            BtnWithdraw.setEnabled(true);
        }
        else {
            BtnNext.setEnabled(true);
            BtnPrev.setEnabled(true);
            BtnWithdraw.setEnabled(false);
        }
    }

    private void deleteMarkAreas(){
        ItemAreaPos=0;
        if(ItemArea != null) {
            for(TextView iv:ItemArea) {
                if (iv != null) {
                    Layout.removeView(iv);
                }
            }
        }
    }

    public void btnStoreClicked(View view){
        if(LastPosQuantity>=20&&clipboard.Overview.getWeight()!=0&&clipboard.Overview.getWeight()!=1000){
            useMicroScale();
        }
        else {
            updateDatabase();
        }
    }

    private void useMicroScale(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                ScaleInUse=DataHandler.isScaleInUse();
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if(ScaleInUse){
                            Toast.makeText(WithdrawItem.this,"Microscale is used by someone else!",Toast.LENGTH_LONG).show();
                        }
                        else {
                            setMicroScaleState(true, clipboard.User.getId());
                            PopupMicorscale = new Dialog(WithdrawItem.this);
                            PopupMicorscale.setContentView(R.layout.popup_microscale);
                            PopupMicorscale.setCancelable(false);
                            Button btnCancel = PopupMicorscale.findViewById(R.id.btnScaleCancel);
                            Button btnOk = PopupMicorscale.findViewById(R.id.btnScaleOk);
                            TextView txtResult = PopupMicorscale.findViewById(R.id.txtScaleValue);
                            TextView txtItemCount = PopupMicorscale.findViewById(R.id.txtItems);
                            btnCancel.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    setMicroScaleState(false, clipboard.User.getId());
                                    PopupMicorscale.dismiss();
                                    TimerCheckWeight.cancel();
                                }
                            });
                            btnOk.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    TimerCheckWeight.cancel();
                                    PopupMicorscale.dismiss();
                                    PopupInfo = new Dialog(WithdrawItem.this);
                                    PopupInfo.setContentView(R.layout.popup_info);
                                    PopupInfo.setCancelable(false);
                                    Button btnInfo = PopupInfo.findViewById(R.id.btnInfo);
                                    btnInfo.setOnClickListener(new View.OnClickListener() {
                                        @Override
                                        public void onClick(View view) {
                                            PopupInfo.dismiss();
                                            setMicroScaleState(false,clipboard.User.getId());
                                            updateDatabase();
                                        }
                                    });
                                    PopupInfo.show();
                                }
                            });
                            PopupMicorscale.show();
                            TimerCheckWeight = new Timer();
                            TaskCheckWeight = new CheckWeight(txtResult,txtItemCount,btnOk,LastPosQuantity,clipboard.Overview.getWeight());
                            TimerCheckWeight.schedule(TaskCheckWeight, 0, 1000);
                            btnOk.setEnabled(false);
                        }
                    }
                });
            }
        }).start();
    }

    private void setMicroScaleState(final boolean state, final int userId){
        if(state) {
            MicroScaleSet = true;
        }
        else {
            MicroScaleSet =false;
        }
        new Thread(new Runnable() {
            @Override
            public void run() {
                DataHandler.setStateMicroScale(userId,state);
            }
        }).start();
    }

    private void updateDatabase(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                ActivityChanged=true;
                DataHandler.deactivateLED(clipboard.StorageBox.getStoragePosition());
                for(int i=0;i<WithdrawList.size();i++){
                    if(i==(MaxBoxCounter-1)) {
                        if (DeleteLastPos) {
                            DataHandler.deleteStoragePos(WithdrawList.get(i).getID());
                        } else {
                            DataHandler.updateQuantity(WithdrawList.get(i).getID(), WithdrawList.get(i).getQuantity() - LastPosQuantity);
                        }
                    }else {
                        DataHandler.deleteStoragePos(WithdrawList.get(i).getID());
                    }
                }
                finish();
            }
        }).start();
    }

    public void btnNextClicked(View view){
        BoxCounter++;
        NextClicked=true;
        PrevClicked=false;
        BtnPrev.setEnabled(true);
        buttonClicked();
    }

    public void btnPrevClicked(View view){
        BoxCounter--;
        PrevClicked=true;
        NextClicked=false;
        BtnNext.setEnabled(true);
        buttonClicked();
    }

    private void buttonClicked(){
        btnCheck();
        deleteMarkAreas();
        deactivateLED();
        new Thread(new Runnable() {
            @Override
            public void run() {
                updateStorageBox();
            }
        }).start();
    }

    @Override
    public void onBackPressed() {
        ActivityChanged=true;
        deactivateLED();
        super.onBackPressed();
    }

    @Override
    protected void onDestroy() {
        if(!ActivityChanged){
            PopupLoading.stopDialog();

        }
        if(PopupMicorscale!=null){
            PopupMicorscale.dismiss();
        }
        if (PopupInfo!=null){
            PopupInfo.dismiss();
        }
        if(MicroScaleSet){
            setMicroScaleState(false,clipboard.User.getId());
        }
        super.onDestroy();
    }
}
