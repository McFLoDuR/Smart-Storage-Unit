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
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.NumberPicker;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class StoreItem extends AppCompatActivity {

    Toolbar TbStorageBox;
    ImageView IvStorageBox;
    ImageView IvColor;
    TextView TxtLabel;
    TextView TxtColor;
    TextView TxtPosition;
    Button BtnStore;
    Button BtnPrev;
    Button BtnNext;
    Spinner SpPosition;
    ConstraintLayout Layout;
    CheckBox[] CbDivider = new CheckBox[3];
    TextView[] ItemArea=null;
    TextView[] PosNum=null;

    boolean MicroScaleSet=false;
    boolean ActivityChanged=false;
    boolean IsFull=false;
    boolean started = false;
    boolean Minimised=false;
    boolean NextClicked=true;
    boolean PrevClicked = false;
    int Quantity;
    int AddedItems=0;
    int MaxBoxCounter;
    int BoxCounter=0;
    int WallCount=0;
    int wall=0;
    int ItemAreaPos=0;
    int InsidePosition=0;

    storageBox StorageBoxData=null;
    storagePosition ItemData=null;
    List<storageBox> StorageBoxList=null;
    List<storagePosition> StoragePositionList=null;

    Dialog PopupMaxQuantity = null;

    int[] sectors;
    int[] box;
    List<Integer> posTextView =new ArrayList<>();
    boolean[] Partitions=new boolean[3];

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.storage_box);

        Quantity = getIntent().getIntExtra("quantity",0);
        IsFull = getIntent().getBooleanExtra("multi",false);
        MicroScaleSet = getIntent().getBooleanExtra("scale",false);

        TbStorageBox = findViewById(R.id.tbStorageBoxSW);
        IvStorageBox = findViewById(R.id.ivStorageBox);
        IvColor = findViewById(R.id.ivColor);
        TxtColor = findViewById(R.id.txtStorageBoxColor);
        TxtLabel = findViewById(R.id.txtStorageBoxTitle);
        TxtPosition = findViewById(R.id.txtPostition);
        Layout = findViewById(R.id.layoutStorageBox);
        BtnStore = findViewById(R.id.btnStore);
        BtnPrev = findViewById(R.id.btnPrev);
        BtnNext = findViewById(R.id.btnNext);
        SpPosition = findViewById(R.id.spPosition);
        CbDivider[0] = findViewById(R.id.cbDiv1);
        CbDivider[1] = findViewById(R.id.cbDiv2);
        CbDivider[2] = findViewById(R.id.cbDiv3);

        TbStorageBox.setTitleTextColor(Color.WHITE);

        IvColor.setColorFilter(Color.parseColor("#"+clipboard.User.getColor()));

        if(!IsFull){
            BtnNext.setVisibility(View.INVISIBLE);
            BtnPrev.setVisibility(View.INVISIBLE);
            for(CheckBox cb:CbDivider){
                cb.setEnabled(false);
            }
            TbStorageBox.setTitle("Location of items");
        }
        else if(IsFull){
            BtnPrev.setEnabled(false);
            TbStorageBox.setTitle("Select a box");
            TxtLabel.setText("The marked space is already occupied");
        }

        setSupportActionBar(TbStorageBox);
        TbStorageBox.setNavigationIcon(R.drawable.back_arrow);
        TbStorageBox.setNavigationOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ActivityChanged=true;
                setMicroScale();
                deactivateLED();
                finish();
            }
        });

        SpPosition.setVisibility(View.INVISIBLE);
        TxtPosition.setVisibility(View.INVISIBLE);

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

        set.connect(BtnStore.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(80));

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
                if(!IsFull) {
                    StorageBoxList = DataHandler.getStorageBoxData(clipboard.StoragePosition.getStorageID());
                }
                else if (IsFull&&!started){
                    started=true;
                    StorageBoxList = DataHandler.getStorageBoxList();
                    if(StorageBoxList==null){
                        PopupLoading.stopDialog();
                        return;
                    }
                    List<storagePosition> storagePositionList = DataHandler.getStoragePositionData(clipboard.Overview.getItemID());
                    if(storagePositionList!=null) {
                        for (storagePosition p : storagePositionList) {
                            List<storagePosition> pos = DataHandler.getStoragePositionList(p.getStorageID());
                            storageBox boxData = DataHandler.getStorageBoxData(p.getStorageID()).get(0);
                            int[] dividers = {boxData.isFirstPartition()?1:0,boxData.isSecondPartition()?1:0,boxData.isThirdPartition()?1:0};
                            int sumDividers=0;
                            for (int d:dividers){
                                if(d==1){
                                    sumDividers++;
                                }
                            }
                            boolean spacefree = true;
                            if (pos.size() == 1 && pos.get(0).getInsidePosition() == 1 && sumDividers==0) {
                                spacefree = false;
                            } else {
                                for (storagePosition pBox : pos) {
                                    if (p.getItemID() != pBox.getItemID()) {
                                        if ((Math.abs(pBox.getInsidePosition() - p.getInsidePosition())) == 1) {
                                            spacefree = false;
                                        }
                                    }
                                }
                            }
                            if (spacefree) {
                                if (StorageBoxList.get(0).getId() != boxData.getId()) {
                                    for(int i=0;i<StorageBoxList.size();i++){
                                        if(StorageBoxList.get(i).getId()==boxData.getId()){
                                            StorageBoxList.remove(i);
                                            break;
                                        }
                                    }
                                    StorageBoxList.add(0, boxData);
                                }
                                AddedItems++;
                            }
                        }
                    }
                    MaxBoxCounter = StorageBoxList.size();
                }
                btnCheck();

                StorageBoxData = StorageBoxList.get(BoxCounter);

                clipboard.StorageBox=StorageBoxData;

                Partitions[0] = StorageBoxData.isFirstPartition();
                Partitions[1] = StorageBoxData.isSecondPartition();
                Partitions[2] = StorageBoxData.isThirdPartition();

                Minimised=false;
                StoragePositionList = DataHandler.getStoragePositionList(StorageBoxData.getId());

                PopupLoading.stopDialog();
                if(!DataHandler.activateLED(StorageBoxData.getStoragePosition(),clipboard.User.getColor(),0,true,true)){
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if(!IsFull) {
                                ActivityChanged = true;
                                Toast.makeText(StoreItem.this, "Please wait! Someone else is using the storage slot!", Toast.LENGTH_LONG).show();
                                finish();
                            }
                            else if (IsFull){
                                if(NextClicked){
                                    BoxCounter++;
                                    NextClicked=false;
                                }
                                else if(PrevClicked){
                                    BoxCounter--;
                                    PrevClicked=false;
                                }
                                btnCheck();
                                initializeStorageBox();
                            }
                        }
                    });
                }
                else {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            setDividers();
                            if(BoxCounter<AddedItems || !IsFull){
                                TxtLabel.setText("Put your items in the marked space");
                            }
                            else{
                                TxtLabel.setText("The marked space is already occupied");
                            }

                            setIvStorageBox();
                        }
                    });
                }
            }
        }).start();
    }

    private void btnCheck(){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                if((MaxBoxCounter-1)==BoxCounter){
                    BtnNext.setEnabled(false);
                }
                if(BoxCounter==0){
                    BtnPrev.setEnabled(false);
                }
            }
        });
    }

    private void setDividers(){
        int counter=0, wallCounter=0, sumWalls=0, includesBoxes=0;
        int[] wallPlace=new int[3];
        int[] partitions = {StorageBoxData.isFirstPartition()?1:0,StorageBoxData.isSecondPartition()?1:0,StorageBoxData.isThirdPartition()?1:0};
        int[][] posToBox;

        box=new int[5];

        CbDivider[0].setChecked(1==partitions[2]);
        CbDivider[1].setChecked(1==partitions[1]);
        CbDivider[2].setChecked(1==partitions[0]);

        for (int i:partitions){
            if(i==1){
                sumWalls++;
            }
        }
        WallCount=sumWalls;
        if(partitions[0]==1){
            wallPlace[0]=1;
        }
        if(partitions[1]==1){
            wallPlace[1]=2;
        }
        if(partitions[2]==1){
            wallPlace[2]=3;
        }

        posToBox=new int[sumWalls+1][];

        for(int i=0;i<sumWalls;i++){
            for(int w=wallCounter;w<wallPlace.length;w++){
                if(wallPlace[w]!=0){
                    break;
                }
                else{
                    wallCounter++;
                }
            }

            if(i>0){
                int boxes=0;
                for(int box=0;box<i;box++){
                    boxes+=posToBox[box].length;
                }
                counter = wallPlace[wallCounter++] - boxes;
            }
            else{
                counter = wallPlace[wallCounter++];
            }
            posToBox[i] = new int[counter];
            includesBoxes+=counter;
        }

        if(sumWalls==0){
            posToBox[0] = new int[4];
        }
        if(sumWalls!=0){
            posToBox[sumWalls]=new int[4-includesBoxes];
        }

        if(StoragePositionList!=null) {

            for (storagePosition p : StoragePositionList) {
                for (int i = 0; i < posToBox[p.getInsidePosition()-1].length; i++) {
                    posToBox[p.getInsidePosition()-1][i] = p.getItemID();
                }
            }
            counter=1;
            for(int[] pos:posToBox){
                for(int i:pos){
                    box[counter++]=i;
                }
            }
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    if(IsFull) {
                        for (int i = 1; i < (box.length-1); i++) {
                            int cbIndex = CbDivider.length - i;
                            if (box[i] != 0 && box[i+1]==0&&box[i]!=clipboard.Overview.getItemID()) {
                                CbDivider[cbIndex].setEnabled(false);
                            } else if (box[i] == 0 && box[i + 1] != 0 &&box[i+1]!=clipboard.Overview.getItemID()) {
                                CbDivider[cbIndex].setEnabled(false);
                            } else if(box[i]!=0&&box[i+1]!=0){
                                CbDivider[cbIndex].setEnabled(false);
                            } else
                            {
                                CbDivider[cbIndex].setEnabled(true);
                            }
                        }
                    }
                }
            });
        }
        else {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    for(CheckBox chb : CbDivider){
                        chb.setEnabled(true);
                    }
                }
            });
        }
    }

    private void setIvStorageBox(){
        int[] partitions = {StorageBoxData.isFirstPartition()?1:0,StorageBoxData.isSecondPartition()?1:0,StorageBoxData.isThirdPartition()?1:0};
        String source = "storage_slot"+partitions[0]+partitions[1]+partitions[2];
        int id = getResources().getIdentifier(source,"mipmap",getPackageName());
        IvStorageBox.setImageResource(id);

        int sumPartitions=0;
        for(int p:partitions){
            if(p==1){
                sumPartitions++;
            }
        }

        if(StoragePositionList!=null) {
            for(int i=wall;i<box.length;i++) {
                for (storagePosition p : StoragePositionList) {
                    if (box[i] == p.getItemID()) {
                        if(WallCount>sumPartitions){
                            p.setInsidePosition(p.getInsidePosition() - 1);
                        }
                        else if(WallCount<sumPartitions){
                            p.setInsidePosition(p.getInsidePosition() + 1);
                        }
                        for(int w=(i+1);w<box.length;w++){
                            if(box[w]!=p.getItemID()){
                                break;
                            }
                            i++;
                        }
                    }
                }
            }
        }
        WallCount=sumPartitions;
        setMarkArea();
    }

    private void setMarkArea(){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                int insidePos=1;
                int height=0;
                List<Integer> areaList = new ArrayList<>();

                areaList.add(sectors[0]);

                if(StorageBoxData.isThirdPartition()){
                    insidePos+=1;
                    areaList.add(sectors[1]+sectors[0]);
                    areaList.add(sectors[2]+sectors[0]);
                    height+=sectors[1];
                }
                if(StorageBoxData.isSecondPartition()){
                    insidePos+=1;
                    areaList.add(sectors[3]+sectors[0]);
                    areaList.add(sectors[4]+sectors[0]);
                    height+=sectors[3];
                }
                if(StorageBoxData.isFirstPartition()){
                    insidePos+=1;
                    areaList.add(sectors[5]+sectors[0]);
                    areaList.add(sectors[6]+sectors[0]);
                    height+=sectors[5];
                }

                areaList.add(sectors[7]+sectors[0]);
                posTextView.clear();
                posTextView.addAll(areaList);

                if(!IsFull) {
                    ItemArea = new TextView[1];
                    insidePos -= clipboard.StoragePosition.getInsidePosition();

                    insidePos*=2;
                    setMultiMark(areaList.get(insidePos),areaList.get(insidePos+1)-areaList.get(insidePos));
                }
                else if(IsFull){
                    if(StoragePositionList!=null){
                        boolean itemInBox=false;
                        for(storagePosition p:StoragePositionList){
                            if (p.getItemID() == clipboard.Overview.getItemID()) {
                                ItemData=p;
                                itemInBox=true;
                                int numPos=insidePos;
                                ItemArea = new TextView[1];
                                insidePos -= p.getInsidePosition();

                                insidePos*=2;
                                setMultiMark(areaList.get(insidePos),areaList.get(insidePos+1)-areaList.get(insidePos));

                                SpPosition.setVisibility(View.INVISIBLE);
                                TxtPosition.setVisibility(View.INVISIBLE);
                                deletePosTextViews();
                            }
                        }
                        if(!itemInBox) {
                            ItemData=null;
                            ItemArea = new TextView[StoragePositionList.size()];
                            for (int i = 0; i < StoragePositionList.size(); i++) {
                                int pos = insidePos; //3
                                pos -= StoragePositionList.get(i).getInsidePosition();
                                pos*=2;
                                setMultiMark(areaList.get(pos),areaList.get(pos+1)-areaList.get(pos));
                                posTextView.remove(pos);
                                posTextView.remove(pos);
                                ItemAreaPos++;
                            }
                            setPositionTextViews();
                        }
                    }
                    else {
                        ItemData=null;
                        setPositionTextViews();
                        if(ItemArea != null) {
                            for (TextView iv : ItemArea) {
                                if (iv != null) {
                                    iv.setVisibility(View.INVISIBLE);
                                }
                            }
                        }
                    }
                }
            }
        });
    }

    private void setMultiMark(int startPos, int height){
        ItemArea[ItemAreaPos] = new TextView(StoreItem.this);
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

    private void deletePosTextViews(){
        if(PosNum!=null) {
            for (TextView view : PosNum) {
                Layout.removeView(view);
                Layout.requestLayout();
            }
        }
    }

    private void setPositionTextViews(){
        SpPosition.setVisibility(View.VISIBLE);
        TxtPosition.setVisibility(View.VISIBLE);
        int sumPartitions=0;
        int sumPos=0;
        int[] partitions = {StorageBoxData.isFirstPartition()?1:0,StorageBoxData.isSecondPartition()?1:0,StorageBoxData.isThirdPartition()?1:0};
        for(int p:partitions){
            if(p==1){
                sumPartitions++;
            }
        }
        if(StoragePositionList!=null){
            sumPos=StoragePositionList.size();
        }
        String[] positions=new String[sumPartitions+1-sumPos];
        int posCounter=0;
        for (int i = 0; i < (sumPartitions+1); i++) {
            boolean count=true;
            if(StoragePositionList!=null) {
                for(storagePosition p : StoragePositionList){
                    if(p.getInsidePosition()==(i+1)){
                        count=false;
                    }
                }
            }
            if(count){
                positions[posCounter++] = (i + 1) + "";
            }
        }
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this,android.R.layout.simple_spinner_dropdown_item,positions);
        SpPosition.setAdapter(adapter);
        deletePosTextViews();
        PosNum = new TextView[positions.length];
        int height = IvStorageBox.getLayoutParams().height/positions.length;
        for(int i=0;i<positions.length;i++){
            PosNum[i] =new TextView(this);
            PosNum[i].setId(View.generateViewId());
            PosNum[i].setText(positions[i]);
            PosNum[i].setLayoutParams(new ViewGroup.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT));
            Layout.addView(PosNum[i]);
            int x = positions.length - 1 - i;
            ConstraintSet set = new ConstraintSet();
            set.clone(Layout);
            set.connect(PosNum[i].getId(), ConstraintSet.TOP, Layout.getId(), ConstraintSet.TOP, posTextView.get(x*2)+(posTextView.get(x*2+1)-posTextView.get(x*2))/2);
            set.connect(PosNum[i].getId(), ConstraintSet.LEFT, Layout.getId(), ConstraintSet.LEFT, ScaleElements.getWidth(10));
            set.applyTo(Layout);
        }
    }

    public void btnStoreClicked(View view){
        new Thread(new Runnable() {
            @Override
            public void run() {
                ActivityChanged=true;
                if(!IsFull) {
                    DataHandler.updateQuantity(clipboard.StoragePosition.getID(), Quantity);
                    DataHandler.deactivateLED(clipboard.StorageBox.getStoragePosition());
                    finish();
                }
                else if(IsFull){
                    if(StoragePositionList!=null) {
                        for (storagePosition pos : StoragePositionList) {
                            DataHandler.updateInsidePos(pos.getID(), pos.getInsidePosition());
                        }
                    }
                    DataHandler.updateDividers(StorageBoxData.getId(),StorageBoxData.isFirstPartition(),StorageBoxData.isSecondPartition(),StorageBoxData.isThirdPartition());
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            PopupMaxQuantity = new Dialog(StoreItem.this);
                            PopupMaxQuantity.setCancelable(false);
                            PopupMaxQuantity.setContentView(R.layout.popup_quantity);
                            TextView txtLabel = PopupMaxQuantity.findViewById(R.id.txtQuantity);
                            txtLabel.setText("Please select max Quantity");
                            final NumberPicker nbpMaxQuantity = PopupMaxQuantity.findViewById(R.id.nbpQuantity);
                            nbpMaxQuantity.setMaxValue(10000);
                            if(ItemData!=null){
                                nbpMaxQuantity.setMinValue(Quantity+ItemData.getQuantity());
                            }
                            else{
                                nbpMaxQuantity.setMinValue(Quantity);
                            }
                            Button btnOk = PopupMaxQuantity.findViewById(R.id.btnQuantity);
                            btnOk.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    nbpMaxQuantity.setEnabled(false);
                                    new Thread(new Runnable() {
                                        @Override
                                        public void run() {
                                            if(BoxCounter>=AddedItems) {
                                                InsidePosition = Integer.parseInt(SpPosition.getSelectedItem().toString());
                                                DataHandler.insertStorageP(StorageBoxData.getId(), clipboard.Overview.getItemID(), InsidePosition, Quantity, clipboard.Overview.getQuantityMin(), nbpMaxQuantity.getValue(), clipboard.Overview.getAlarmActive());
                                            }
                                            else{
                                                DataHandler.updateStorageP(ItemData.getID(),ItemData.getInsidePosition(),Quantity+ItemData.getQuantity(),nbpMaxQuantity.getValue());
                                            }
                                            PopupMaxQuantity.dismiss();
                                            DataHandler.deactivateLED(clipboard.StorageBox.getStoragePosition());
                                            finish();
                                        }
                                    }).start();
                                }
                            });
                            PopupMaxQuantity.show();
                        }
                    });
                }
            }
        }).start();
    }

    public void btnNextClicked(View view){
        NextClicked=true;
        BoxCounter++;
        BtnPrev.setEnabled(true);
        StorageBoxData.setFirstPartition(Partitions[0]);
        StorageBoxData.setSecondPartition(Partitions[1]);
        StorageBoxData.setThirdPartition(Partitions[2]);
        deleteMarkAreas();
        deactivateLED();
        initializeStorageBox();
    }

    public void btnPrevClicked(View view){
        PrevClicked=true;
        BoxCounter--;
        BtnNext.setEnabled(true);
        StorageBoxData.setFirstPartition(Partitions[0]);
        StorageBoxData.setSecondPartition(Partitions[1]);
        StorageBoxData.setThirdPartition(Partitions[2]);
        deleteMarkAreas();
        deactivateLED();
        initializeStorageBox();
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

    private void deactivateLED(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                DataHandler.deactivateLED(clipboard.StorageBox.getStoragePosition());
            }
        }).start();
    }

    public void cbDivider1Change(View view){
        if(CbDivider[0].isChecked()){
            StorageBoxData.setThirdPartition(true);
        }
        else{
            StorageBoxData.setThirdPartition(false);
        }
        wall=4;
        deleteMarkAreas();
        setIvStorageBox();
    }

    public void cbDivider2Change(View view){
        if(CbDivider[1].isChecked()){
            StorageBoxData.setSecondPartition(true);
        }
        else{
            StorageBoxData.setSecondPartition(false);
        }
        wall=3;
        deleteMarkAreas();
        setIvStorageBox();
    }

    public void cbDivider3Change(View view){
        if(CbDivider[2].isChecked()){
            StorageBoxData.setFirstPartition(true);
        }
        else{
            StorageBoxData.setFirstPartition(false);
        }
        wall=2;
        deleteMarkAreas();
        setIvStorageBox();
    }

    @Override
    public void onBackPressed() {
        ActivityChanged=true;
        setMicroScale();
        deactivateLED();
        super.onBackPressed();
    }

    private void setMicroScale(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                if(MicroScaleSet) {
                    DataHandler.setStateMicroScale(clipboard.User.getId(), false);
                }
            }
        }).start();
    }

    @Override
    protected void onDestroy() {
        setMicroScale();
        if(!ActivityChanged){
            PopupLoading.stopDialog();
            deactivateLED();
        }
        if(PopupMaxQuantity!=null){
            PopupMaxQuantity.dismiss();
        }
        super.onDestroy();
    }
}
