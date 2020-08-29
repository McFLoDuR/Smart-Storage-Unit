package com.smartstorageunit;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.NumberPicker;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;
import java.util.Timer;

import adapter.ItemDataAdapter;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.widget.Toolbar;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import tables.componentTypes;
import tables.itemData;
import tables.overview;
import tables.references;

public class NewItem extends Fragment{

    private ConstraintLayout Layout;
    private AutoCompleteTextView TxtArticleNum;
    private AutoCompleteTextView TxtItemType;
    private AutoCompleteTextView TxtItemVersion;
    private AutoCompleteTextView TxtReferenceName;
    private AutoCompleteTextView TxtUnit;
    private EditText TxtWebsite;
    private EditText TxtValue;
    private Button BtnAdd;
    private Button BtnDelete;
    private ListView LvItemData;
    private CheckBox ChbAlarm;

    private ItemDataAdapter adapter;
    private List<itemData> ItemDataList = new ArrayList<>();

    private overview NewItem = new overview();

    private String[] ComponentTypeList;
    private String[] ComponentVersionList;
    private String[] ReferenceList;

    private Dialog popMinQuantity=null;
    private Dialog popQuantity=null;
    private Dialog popupScale=null;

    private boolean ScaleInUse=false;
    private boolean ActivityChanged=false;
    private boolean MicroScaleSet=false;

    private Timer TimerCheckWeight;
    private CheckWeight TaskCheckWeight;

    public NewItem(){}

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_new_item,container,false);

        setHasOptionsMenu(true);

        Layout = rootView.findViewById(R.id.constLayoutNewItem);
        TxtArticleNum = rootView.findViewById(R.id.actxtArticleNum);
        TxtItemType = rootView.findViewById(R.id.actxtType);
        TxtItemVersion = rootView.findViewById(R.id.actxtItemVersion);
        TxtReferenceName = rootView.findViewById(R.id.actxtReferenceName);
        TxtUnit = rootView.findViewById(R.id.actxtUnit);
        TxtWebsite = rootView.findViewById(R.id.txtWebsite);
        TxtValue = rootView.findViewById(R.id.txtValue);
        BtnAdd = rootView.findViewById(R.id.btnAdd);
        BtnDelete = rootView.findViewById(R.id.btnDelete);
        LvItemData = rootView.findViewById(R.id.lvItemReferences);
        ChbAlarm = rootView.findViewById(R.id.chbAlarmActive);

        setConstraints();

        PopupLoading.context=getContext();
        PopupLoading.startDialog();

        BtnDelete.setEnabled(false);
        BtnDelete.setOnClickListener(btnDeleteClicked);
        BtnAdd.setOnClickListener(btnAddClicked);

        adapter = new ItemDataAdapter(getContext(),ItemDataList);
        LvItemData.setAdapter(adapter);
        LvItemData.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                itemData itm = (itemData) adapterView.getItemAtPosition(i);
                TxtReferenceName.setText(itm.getRefName());
                TxtValue.setText(itm.getValue());
                TxtUnit.setText(itm.getUnit());
                BtnDelete.setEnabled(true);
            }
        });

        ChbAlarm.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                NewItem.setAlarmActive(b);
            }
        });

        AutocompleteSettings();
        setAutocomplete();

        return rootView;
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        inflater.inflate(R.menu.menu_new_item,menu);
    }

    private void setConstraints(){
        ConstraintSet set = new ConstraintSet();
        set.clone(Layout);

        set.connect(TxtArticleNum.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));
        set.connect(TxtArticleNum.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(4));

        set.connect(ChbAlarm.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(2));
        set.connect(ChbAlarm.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(60));

        set.connect(TxtItemType.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(7));
        set.connect(TxtItemType.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(4));

        set.connect(TxtItemVersion.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(7));
        set.connect(TxtItemVersion.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(60));

        set.connect(TxtWebsite.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(13));

        set.connect(TxtReferenceName.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(19));
        set.connect(TxtReferenceName.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(4));

        set.connect(TxtValue.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(19));
        set.connect(TxtValue.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(55));

        set.connect(TxtUnit.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(19));
        set.connect(TxtUnit.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(74));

        set.connect(BtnDelete.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(25));
        set.connect(BtnDelete.getId(),ConstraintSet.LEFT,Layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(7));

        set.connect(BtnAdd.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(25));
        set.connect(BtnAdd.getId(),ConstraintSet.RIGHT,Layout.getId(),ConstraintSet.RIGHT,ScaleElements.getWidth(7));

        set.connect(LvItemData.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(35));

        set.applyTo(Layout);
    }

    private void AutocompleteSettings(){
        TxtArticleNum.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b) {
                    TxtArticleNum.showDropDown();
                }
            }
        });
        TxtArticleNum.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TxtArticleNum.showDropDown();
            }
        });
        TxtItemType.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
                    TxtItemType.showDropDown();
                }
            }
        });
        TxtItemType.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TxtItemType.showDropDown();
            }
        });
        TxtItemVersion.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
                    if(!TextUtils.isEmpty(TxtItemType.getText())) {
                        new Thread(new Runnable() {
                            @Override
                            public void run() {
                                List<componentTypes> compVersionList = DataHandler.getComponentVersionList(TxtItemType.getText().toString());
                                if(compVersionList!=null) {
                                    ComponentVersionList = new String[compVersionList.size()];
                                    int counter = 0;
                                    for (componentTypes comp : compVersionList) {
                                        ComponentVersionList[counter++] = comp.getTypeVersion();
                                    }

                                    getActivity().runOnUiThread(new Runnable() {
                                        @Override
                                        public void run() {
                                            TxtItemVersion.setAdapter(new ArrayAdapter<>(getContext(), android.R.layout.simple_list_item_1, ComponentVersionList));
                                            TxtItemVersion.showDropDown();
                                        }
                                    });
                                }
                            }
                        }).start();
                    }
                }
            }
        });
        TxtItemVersion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TxtItemVersion.showDropDown();
            }
        });
        TxtReferenceName.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
                    TxtReferenceName.showDropDown();
                }
            }
        });
        TxtReferenceName.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TxtReferenceName.showDropDown();
            }
        });
        TxtUnit.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
                    TxtUnit.showDropDown();
                }
            }
        });
        TxtUnit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TxtUnit.showDropDown();
            }
        });
    }

    private void setAutocomplete(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                List<componentTypes> compList = DataHandler.getComponentTypeList();
                List<references> refList = DataHandler.getReferenceList();
                final List<String> unitList = DataHandler.getUnitList();
                ComponentTypeList = new String[compList.size()];
                ReferenceList = new String[refList.size()];
                int counter=0;
                for(componentTypes comp :compList){
                    ComponentTypeList[counter++] = comp.getTypeName();
                }
                counter=0;
                for(references ref:refList){
                    ReferenceList[counter++]=ref.getName();
                }
                getActivity().runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        TxtItemType.setAdapter(new ArrayAdapter<>(getContext(),android.R.layout.simple_list_item_1,ComponentTypeList));
                        TxtReferenceName.setAdapter(new ArrayAdapter<>(getContext(),android.R.layout.simple_list_item_1,ReferenceList));
                        TxtUnit.setAdapter(new ArrayAdapter<>(getContext(),android.R.layout.simple_list_item_1,unitList));
                        PopupLoading.stopDialog();
                    }
                });
            }
        }).start();
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if(item.getItemId()==R.id.mSaveItem){
            if(checkFields()){
                PopupLoading.startDialog();
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        if(checkArticleNum()){
                            checkComponent();
                            DataHandler.insertItem(NewItem.getTypeID(),NewItem.getArticleNum(),0,TxtWebsite.getText().toString());
                            NewItem.setItemID(DataHandler.getItemId(NewItem.getArticleNum()));
                            checkReference();
                            PopupLoading.stopDialog();
                            getActivity().runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    popMinQuantity = new Dialog(getContext());
                                    popMinQuantity.setContentView(R.layout.popup_quantity);
                                    popMinQuantity.setCancelable(false);
                                    final NumberPicker nbpQuantity = popMinQuantity.findViewById(R.id.nbpQuantity);
                                    TextView txtHeader = popMinQuantity.findViewById(R.id.txtQuantity);
                                    Button btnQuantityOk = popMinQuantity.findViewById(R.id.btnQuantity);
                                    btnQuantityOk.setOnClickListener(new View.OnClickListener() {
                                        @Override
                                        public void onClick(View view) {
                                            nbpQuantity.setEnabled(false);
                                            NewItem.setQuantityMin(nbpQuantity.getValue());
                                            popMinQuantity.dismiss();
                                            popQuantity = new Dialog(getContext());
                                            popQuantity.setContentView(R.layout.popup_quantity);
                                            popQuantity.setCancelable(false);
                                            final NumberPicker nbpQuantity = popQuantity.findViewById(R.id.nbpQuantity);
                                            TextView txtHeader = popQuantity.findViewById(R.id.txtQuantity);
                                            Button btnQuantityOk = popQuantity.findViewById(R.id.btnQuantity);
                                            btnQuantityOk.setOnClickListener(new View.OnClickListener() {
                                                @Override
                                                public void onClick(View view) {
                                                    nbpQuantity.setEnabled(false);
                                                    NewItem.setQuantity(nbpQuantity.getValue());
                                                    popQuantity.dismiss();
                                                    clipboard.Overview = NewItem;
                                                    if(NewItem.getQuantity()>20){
                                                        useMicroScale();
                                                    }
                                                    else{
                                                        changeActivity();
                                                    }
                                                }
                                            });
                                            txtHeader.setText("Select quantity");
                                            nbpQuantity.setMinValue(1);
                                            nbpQuantity.setMaxValue(10000);
                                            popQuantity.show();
                                        }
                                    });
                                    txtHeader.setText("Select min quantity");
                                    nbpQuantity.setMinValue(1);
                                    nbpQuantity.setMaxValue(10000);
                                    popMinQuantity.show();
                                }
                            });
                        }
                        else{
                            getActivity().runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    PopupLoading.stopDialog();
                                    Toast.makeText(getContext(),"Item already exists!",Toast.LENGTH_SHORT).show();
                                }
                            });
                        }
                    }
                }).start();
            }
        }
        return true;
    }

    private boolean checkFields(){
        if(TextUtils.isEmpty(TxtArticleNum.getText())){
            TxtArticleNum.setError("Required");
            return false;
        }
        else if(TextUtils.isEmpty(TxtItemType.getText())){
            TxtItemType.setError("Required");
            return false;
        }
        else if(TextUtils.isEmpty(TxtItemVersion.getText())){
            TxtItemVersion.setError("Required");
            return false;
        }
        else if(TextUtils.isEmpty(TxtWebsite.getText())){
            TxtWebsite.setError("Required");
            return false;
        }
        else if(adapter.isEmpty()){
            Toast.makeText(getContext(),"You have to add at least one Reference",Toast.LENGTH_LONG).show();
            return false;
        }

        return true;
    }

    private boolean checkArticleNum(){
        List<String> itmList = DataHandler.getItemList();
        for (String itm:itmList){
            if(itm.equals(TxtArticleNum.getText().toString())){
                return false;
            }
        }
        NewItem.setArticleNum(TxtArticleNum.getText().toString());
        return true;
    }

    private void checkComponent(){
        boolean existing=false;
        List<componentTypes> compList=DataHandler.getComponentList();
        for(componentTypes comp :compList){
            if(comp.getTypeName().equals(TxtItemType.getText().toString())){
                if(comp.getTypeVersion().equals(TxtItemVersion.getText().toString())){
                    NewItem.setTypeID(comp.getId());
                    NewItem.setTypeName(comp.getTypeName());
                    existing=true;
                    break;
                }
            }
        }
        if(!existing){
            DataHandler.insertComponent(TxtItemType.getText().toString(),TxtItemVersion.getText().toString());
            NewItem.setTypeName(TxtItemType.getText().toString());
            compList=DataHandler.getComponentList();
            for(componentTypes comp :compList){
                if(comp.getTypeName().equals(TxtItemType.getText().toString())){
                    NewItem.setTypeID(comp.getId());
                    break;
                }
            }
        }
    }

    private void checkReference(){
        List<references> refList = DataHandler.getReferenceList();
        boolean existing;
        for(int i=0;i<adapter.getCount();i++){
            existing=false;
            itemData itm = adapter.getItem(i);
            for (references ref:refList){
                if(ref.getName().equals(itm.getRefName())){
                    DataHandler.insertItemData(NewItem.getItemID(),ref.getId(),itm.getValue(),itm.getUnit());
                    existing=true;
                    break;
                }
            }
            if(!existing){
                DataHandler.insertReference(itm.getRefName());
                DataHandler.insertItemData(NewItem.getItemID(),DataHandler.getRefId(itm.getRefName()),itm.getValue(),itm.getUnit());
            }
        }
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
                            ActivityChanged=true;
                            changeActivity();
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
                                    changeActivity();
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
                                                DataHandler.setWeight(NewItem.getItemID(),1000);
                                            }
                                        }).start();
                                    }
                                    else {
                                        new Thread(new Runnable() {
                                            @Override
                                            public void run() {
                                                DataHandler.setWeight(NewItem.getItemID(),Double.parseDouble(txtResult.getText().toString().substring(0,txtResult.length()-1)));
                                            }
                                        }).start();
                                    }
                                    ActivityChanged=true;
                                    popupScale.dismiss();
                                    changeActivity();
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

    private void changeActivity(){
        Intent storageBox = new Intent(getContext(),StoreItem.class);
        storageBox.putExtra("quantity",NewItem.getQuantity());
        storageBox.putExtra("multi",true);
        storageBox.putExtra("scale",MicroScaleSet);
        startActivity(storageBox);
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

    private View.OnClickListener btnAddClicked = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            if(checkReferencesContent()) {
                boolean contains=false;
                for (int i=0;i<adapter.getCount();i++){
                    itemData itm = adapter.getItem(i);
                    if(itm.getRefName().equals(TxtReferenceName.getText().toString()) && itm.getValue().equals(TxtValue.getText().toString()) && itm.getUnit().equals(TxtUnit.getText().toString())){
                        contains=true;
                    }
                    else if(itm.getRefName().equals(TxtReferenceName.getText().toString())){
                        adapter.remove(itm);
                    }
                }
                if(!contains) {
                    adapter.add(new itemData(TxtReferenceName.getText().toString(), TxtValue.getText().toString(), TxtUnit.getText().toString()));
                    TxtReferenceName.setText("");
                    TxtValue.setText("");
                    TxtUnit.setText("");
                    BtnDelete.setEnabled(false);
                }
                else{
                    Toast.makeText(getContext(),"Already added!",Toast.LENGTH_SHORT).show();
                }
            }
        }
    };

    private View.OnClickListener btnDeleteClicked = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            if(checkReferencesContent()){
                for (int i=0;i<adapter.getCount();i++) {
                    itemData itm = adapter.getItem(i);
                    adapter.remove(itm);
                }
                TxtReferenceName.setText("");
                TxtValue.setText("");
                TxtUnit.setText("");
                BtnDelete.setEnabled(false);
            }
        }
    };

    private boolean checkReferencesContent(){
        if(TextUtils.isEmpty(TxtReferenceName.getText())){
            TxtReferenceName.setError("Required");
            return false;
        }
        else if(TextUtils.isEmpty(TxtValue.getText())){
            TxtValue.setError("Required");
            return false;
        }
        else if(TextUtils.isEmpty(TxtUnit.getText())){
            TxtUnit.setError("Required");
            return false;
        }
        else{
            TxtReferenceName.setError(null);
            TxtValue.setError(null);
            TxtUnit.setError(null);
        }
        return true;
    }

    @Override
    public void onDestroy() {
        if(MicroScaleSet&&!ActivityChanged){
            setMicroScaleState(false,clipboard.User.getId());
        }
        if(popMinQuantity!=null){
            popMinQuantity.dismiss();
        }
        if(popQuantity!=null){
            popQuantity.dismiss();
        }
        if(popupScale!=null){
            popupScale.dismiss();
        }
        if(TimerCheckWeight!=null){
            TimerCheckWeight.purge();
            TimerCheckWeight.cancel();
        }
        super.onDestroy();
    }
}
