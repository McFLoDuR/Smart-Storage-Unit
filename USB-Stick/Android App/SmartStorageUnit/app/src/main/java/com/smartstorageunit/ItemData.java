package com.smartstorageunit;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.ListView;
import android.widget.NumberPicker;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;
import java.util.Timer;

import adapter.ItemDataAdapter;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import tables.componentTypes;
import tables.itemData;
import tables.storagePosition;

public class ItemData extends Fragment {

    private ConstraintLayout Layout;
    private TextView TxtTypeName;
    private TextView TxtTypeVersion;
    private TextView TxtArticleNum;
    private TextView TxtVArticleNum;
    private TextView TxtQuantity;
    private TextView TxtQuantityNum;
    private ListView LvItemData;
    private CheckBox ChbSetAlarm;

    private Dialog popupStore;
    private Dialog popupScale;
    private Dialog popupMinQuantity;

    private Button btnQuantityOk;

    private boolean NewItem;
    private int Quantity;
    private boolean ScaleInUse=false;
    private boolean MicroScaleSet=false;
    private boolean ActivityChanged=false;

    private Timer TimerCheckWeight;
    private CheckWeight TaskCheckWeight;

    private List<storagePosition> storageList;

    public ItemData() {}

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_item_data,container,false);
        NewItem = getArguments().getBoolean("newItem",false);

        setHasOptionsMenu(true);

        Layout = rootView.findViewById(R.id.constLayoutItemData);
        TxtTypeName = rootView.findViewById(R.id.txtTypeName);
        TxtTypeVersion = rootView.findViewById(R.id.txtTypeVersion);
        TxtArticleNum = rootView.findViewById(R.id.txtArticleNum);
        TxtVArticleNum = rootView.findViewById(R.id.txtVArticleNum);
        TxtQuantity = rootView.findViewById(R.id.txtQuantity);
        TxtQuantityNum = rootView.findViewById(R.id.txtQuantityNum);
        LvItemData = rootView.findViewById(R.id.lvItemData);
        ChbSetAlarm = rootView.findViewById(R.id.chbSetAlarm);

        setConstraints();
        ChbSetAlarm.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton,final boolean b) {
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        if(!NewItem) {
                            DataHandler.setAlarm(clipboard.Overview.getItemID(), b);
                        }
                        else {
                            clipboard.Overview.setAlarmActive(b);
                        }
                    }
                }).start();
            }
        });
        fillData();
        return rootView;
    }

    private void setConstraints(){
        ConstraintSet set = new ConstraintSet();
        set.clone(Layout);

        set.connect(TxtTypeName.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));
        set.connect(TxtTypeName.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(1));

        set.connect(TxtTypeVersion.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));
        set.connect(TxtTypeVersion.getId(),ConstraintSet.LEFT,TxtTypeName.getId(),ConstraintSet.RIGHT,ScaleElements.getWidth(4));

        set.connect(ChbSetAlarm.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));
        set.connect(ChbSetAlarm.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(70));

        set.connect(TxtVArticleNum.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(5));
        set.connect(TxtVArticleNum.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(1));

        set.connect(TxtArticleNum.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(5));
        set.connect(TxtArticleNum.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(35));

        set.connect(TxtQuantity.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(7));
        set.connect(TxtQuantity.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(1));

        set.connect(TxtQuantityNum.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(7));
        set.connect(TxtQuantityNum.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(35));

        set.connect(LvItemData.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(12));

        set.applyTo(Layout);
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        inflater.inflate(R.menu.menu_item_data,menu);
        if(!clipboard.Permission.isWithdrawItems()||clipboard.Overview.getQuantity()==0){
            if(!NewItem&&clipboard.Overview.getQuantity()==0){
                menu.findItem(R.id.mWithdraw).setVisible(false);
            }
            menu.findItem(R.id.mWithdraw).setVisible(false);
        }
        if(!clipboard.Permission.isStoreItems()){
            menu.findItem(R.id.mStore).setVisible(false);
        }
    }

    private void fillData(){
        PopupLoading.context=getContext();
        PopupLoading.startDialog();
        new Thread(new Runnable() {
            @Override
            public void run() {
                final componentTypes type = DataHandler.getComponentType(clipboard.Overview.getTypeID()).get(0);
                final List<itemData> list = DataHandler.getItemData(clipboard.Overview.getItemID());
                getActivity().runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        TxtArticleNum.setText(clipboard.Overview.getArticleNum());
                        TxtTypeName.setText(type.getTypeName());
                        TxtTypeVersion.setText(type.getTypeVersion());
                        if(!NewItem) {
                            TxtQuantityNum.setText(clipboard.Overview.getQuantity() + "");
                            ChbSetAlarm.setChecked(clipboard.Overview.getAlarmActive());
                        }
                        else{
                            TxtQuantity.setVisibility(View.INVISIBLE);
                            TxtQuantityNum.setVisibility(View.INVISIBLE);
                        }
                        if(list!=null) {
                            ItemDataAdapter adapter = new ItemDataAdapter(getContext(), list);
                            LvItemData.setAdapter(adapter);
                        }
                        PopupLoading.stopDialog();
                    }
                });
            }
        }).start();
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        final NumberPicker nbpQuantity;
        TextView txtHeader;

        switch (item.getItemId()){
            case R.id.mStore:
                popupStore = new Dialog(getContext());
                popupStore.setContentView(R.layout.popup_quantity);
                nbpQuantity = popupStore.findViewById(R.id.nbpQuantity);
                txtHeader = popupStore.findViewById(R.id.txtQuantity);
                btnQuantityOk = popupStore.findViewById(R.id.btnQuantity);
                btnQuantityOk.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        nbpQuantity.setEnabled(false);
                        Quantity = nbpQuantity.getValue();
                        popupStore.dismiss();

                        if(Quantity>=20 && clipboard.Overview.getWeight()==0){
                            useMicroScale();
                        }
                        else {
                            if(clipboard.Overview.getQuantityMin()==0){
                                setMinQuantity();
                            }else {
                                changeActitvity();
                            }
                        }
                    }
                });
                txtHeader.setText("Select amount of items");
                nbpQuantity.setMinValue(1);
                nbpQuantity.setMaxValue(10000);
                popupStore.show();
                break;
            case R.id.mWithdraw:
                popupStore = new Dialog(getContext());
                popupStore.setContentView(R.layout.popup_quantity);
                nbpQuantity = popupStore.findViewById(R.id.nbpQuantity);
                txtHeader = popupStore.findViewById(R.id.txtQuantity);
                btnQuantityOk = popupStore.findViewById(R.id.btnQuantity);
                btnQuantityOk.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        nbpQuantity.setEnabled(false);
                        Quantity = nbpQuantity.getValue();
                        popupStore.dismiss();
                        Intent storageBox = new Intent(getContext(),WithdrawItem.class);
                        storageBox.putExtra("quantity", Quantity);
                        startActivity(storageBox);
                    }
                });
                txtHeader.setText("Select amount of items");
                nbpQuantity.setMinValue(1);
                nbpQuantity.setMaxValue(clipboard.Overview.getQuantity());
                popupStore.show();
                break;
        }
        return true;
    }

    private void useMicroScale(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                ScaleInUse=DataHandler.isScaleInUse();
                getActivity().runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if(ScaleInUse){
                            Toast.makeText(getContext(),"Microscale is used by someone else!",Toast.LENGTH_LONG).show();
                        }
                        else {
                            setMicroScaleState(true, clipboard.User.getId());
                            popupScale = new Dialog(getContext());
                            popupScale.setContentView(R.layout.popup_microscale);
                            popupScale.setCancelable(false);
                            Button btnCancel = popupScale.findViewById(R.id.btnScaleCancel);
                            Button btnOk = popupScale.findViewById(R.id.btnScaleOk);
                            final TextView txtResult = popupScale.findViewById(R.id.txtScaleValue);
                            btnCancel.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    setMicroScaleState(false, clipboard.User.getId());
                                    popupScale.dismiss();
                                    TimerCheckWeight.cancel();
                                    ActivityChanged=true;
                                    changeActitvity();
                                }
                            });
                            btnOk.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    TimerCheckWeight.cancel();

                                    if(Double.parseDouble(txtResult.getText().toString().substring(0,txtResult.length()-1))<2){
                                        new Thread(new Runnable() {
                                            @Override
                                            public void run() {
                                                DataHandler.setWeight(clipboard.Overview.getItemID(),1000);
                                            }
                                        }).start();
                                    }
                                    else {
                                        new Thread(new Runnable() {
                                            @Override
                                            public void run() {
                                                double  weight = Double.parseDouble(txtResult.getText().toString().substring(0,txtResult.length()-1))/20.0;
                                                DataHandler.setWeight(clipboard.Overview.getItemID(),weight);
                                            }
                                        }).start();
                                    }
                                    ActivityChanged=true;
                                    popupScale.dismiss();
                                    changeActitvity();
                                }
                            });
                            popupScale.show();
                            TimerCheckWeight = new Timer();
                            TaskCheckWeight = new CheckWeight(txtResult);
                            TimerCheckWeight.schedule(TaskCheckWeight, 0, 1000);
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

    private void changeActitvity(){
        new Thread(new Runnable() {
            @Override
            public void run() {

                storageList = DataHandler.getStoragePositionData(clipboard.Overview.getItemID());
                int minDiff=getMaxQuantity();

                storagePosition min=null;

                if(storageList!=null) {
                    for (storagePosition stp : storageList) {
                        if (stp.getQuantity() + Quantity <= stp.getQuantityMax()) {
                            if (stp.getQuantityMax() - stp.getQuantity() - Quantity < minDiff) {
                                min = stp;
                                minDiff = stp.getQuantityMax() - stp.getQuantity() - Quantity;
                            }
                        }
                    }
                }
                int addQuantity=0;
                clipboard.StoragePosition = min;
                if(min!=null){
                    addQuantity = min.getQuantity();
                }
                Intent storageBox = new Intent(getContext(),StoreItem.class);
                storageBox.putExtra("quantity",Quantity+addQuantity);
                storageBox.putExtra("scale",MicroScaleSet);
                if(min!=null){
                    storageBox.putExtra("multi",false);
                }
                else {
                    storageBox.putExtra("multi",true);
                }
                startActivity(storageBox);
            }
        }).start();
    }

    private int getMaxQuantity(){
        int maxQuantity=0;

        if(storageList!=null) {
            for (storagePosition stp : storageList) {
                int diff = stp.getQuantityMax() - stp.getQuantity();
                if (maxQuantity < diff) {
                    maxQuantity = diff;
                }
            }
        }
        return maxQuantity;
    }

    private void setMinQuantity(){
        popupMinQuantity = new Dialog(getContext());
        popupMinQuantity.setContentView(R.layout.popup_quantity);
        final NumberPicker nbpQuantity = popupMinQuantity.findViewById(R.id.nbpQuantity);
        TextView txtHeader = popupMinQuantity.findViewById(R.id.txtQuantity);
        btnQuantityOk = popupMinQuantity.findViewById(R.id.btnQuantity);
        btnQuantityOk.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nbpQuantity.setEnabled(false);
                clipboard.Overview.setQuantityMin(nbpQuantity.getValue());
                popupMinQuantity.dismiss();
                changeActitvity();
            }
        });
        txtHeader.setText("Select min quantity");
        nbpQuantity.setMinValue(1);
        nbpQuantity.setMaxValue(10000);
        popupMinQuantity.show();
    }

    @Override
    public void onDestroy() {
        if(MicroScaleSet&&!ActivityChanged){
            setMicroScaleState(false,clipboard.User.getId());
        }
        if(popupStore!=null){
            popupStore.dismiss();
        }
        if(popupScale!=null){
            popupScale.dismiss();
        }
        if(popupMinQuantity!=null){
            popupMinQuantity.dismiss();
        }
        if(TimerCheckWeight!=null){
            TimerCheckWeight.purge();
            TimerCheckWeight.cancel();
        }
        super.onDestroy();
    }
}
