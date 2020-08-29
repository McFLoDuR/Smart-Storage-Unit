package com.smartstorageunit;

import android.app.Dialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import java.util.ArrayList;
import java.util.List;

import adapter.StorageBoxAdapter;
import adapter.StoragePosAdapter;
import tables.allStorageBoxPos;
import tables.storageBox;
import tables.storagePosTable;
import tables.storagePosition;

public class DeleteStorageSlot extends Fragment {

    private ConstraintLayout layout;
    private EditText LblSearch;
    private ListView LvStorageSlot;
    private SwipeRefreshLayout RefreshStorageSlotLayout;

    private List<allStorageBoxPos> BoxItemList=null;
    private List<storagePosTable> ItmPosList=null;
    private List<storageBox> BoxList=null;
    private StorageBoxAdapter adapterStorageSlot;

    private boolean BoxListSet=false;

    private Dialog PopupDeleteSlot=null;

    private AdapterView.OnItemClickListener listClick = new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView adapterView, View view, int i, long l) {
            allStorageBoxPos boxData = (allStorageBoxPos) LvStorageSlot.getItemAtPosition(i);
            deleteStorageSlot(boxData);
        }
    };

    public DeleteStorageSlot() {
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_overview,container,false);

        TextView TxtNotInStorage;
        SwipeRefreshLayout RefreshItmLayout;

        layout = rootView.findViewById(R.id.constLayoutOverview);
        LblSearch = rootView.findViewById(R.id.lblSearch);
        TxtNotInStorage = rootView.findViewById(R.id.txtItemNotInStorage);
        LvStorageSlot = rootView.findViewById(R.id.lvOverview);
        RefreshStorageSlotLayout = rootView.findViewById(R.id.swipeRefreshOv);
        RefreshItmLayout = rootView.findViewById(R.id.swipeRefreshItems);

        RefreshItmLayout.setVisibility(View.INVISIBLE);
        TxtNotInStorage.setVisibility(View.INVISIBLE);

        setConstraints();
        setListener();
        setBoxItemList();

        return rootView;
    }

    private void setConstraints(){
        ConstraintLayout.LayoutParams params = (ConstraintLayout.LayoutParams) RefreshStorageSlotLayout.getLayoutParams();
        RefreshStorageSlotLayout.setLayoutParams(new ConstraintLayout.LayoutParams(params.width,ScaleElements.getHeight(78)));

        ConstraintSet set = new ConstraintSet();
        set.clone(layout);

        set.connect(LblSearch.getId(),ConstraintSet.LEFT,layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(2));
        set.connect(LblSearch.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));

        set.connect(RefreshStorageSlotLayout.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(8));
        set.connect(RefreshStorageSlotLayout.getId(),ConstraintSet.LEFT,layout.getId(),ConstraintSet.LEFT);
        set.connect(RefreshStorageSlotLayout.getId(),ConstraintSet.RIGHT,layout.getId(),ConstraintSet.RIGHT);

        set.applyTo(layout);
    }

    private void setListener(){
        RefreshStorageSlotLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refresh();
                LblSearch.setText("");
            }
        });

        LvStorageSlot.setOnItemClickListener(listClick);

        LblSearch.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if(adapterStorageSlot!=null) {
                    adapterStorageSlot.filter(charSequence.toString());
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private void setBoxItemList(){
        PopupLoading.context=getContext();
        PopupLoading.startDialog();
        new Thread(new Runnable() {
            @Override
            public void run() {
                BoxList = DataHandler.getAllStorageBoxes();
                ItmPosList = DataHandler.getAllStoragep();

                BoxItemList=new ArrayList<>();
                for (storageBox box:BoxList){
                    List<storagePosTable> list=new ArrayList<>();
                    for(storagePosTable pos:ItmPosList){
                        if(box.getId()==pos.getStoragehId()){
                           list.add(pos);
                        }
                    }
                    BoxItemList.add(new allStorageBoxPos(box.getId(),box.getStoragePosition(),box.isFirstPartition(),box.isSecondPartition(),box.isThirdPartition(),list));
                }
                getActivity().runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        fillOverviewList();
                    }
                });
                PopupLoading.stopDialog();
            }
        }).start();
    }

    private void fillOverviewList(){
        if (BoxItemList!=null){
            adapterStorageSlot = new StorageBoxAdapter(getContext(), BoxItemList);
            LayoutInflater inflater = getLayoutInflater();
            View ovHeader = inflater.inflate(R.layout.storagebox_list_layout, LvStorageSlot, false);
            LvStorageSlot.addHeaderView(ovHeader, null, false);
            LvStorageSlot.setAdapter(adapterStorageSlot);
            BoxListSet = true;
        }
    }

    private void refresh(){
        LblSearch.setText("");
        if(BoxList!=null){
            adapterStorageSlot.clear();
        }
        new Thread(new Runnable() {
            @Override
            public void run() {
                BoxList = DataHandler.getAllStorageBoxes();
                ItmPosList = DataHandler.getAllStoragep();

                BoxItemList=new ArrayList<>();
                for (storageBox box:BoxList){
                    List<storagePosTable> list=new ArrayList<>();
                    for(storagePosTable pos:ItmPosList){
                        if(box.getId()==pos.getStoragehId()){
                            list.add(pos);
                        }
                    }
                    BoxItemList.add(new allStorageBoxPos(box.getId(),box.getStoragePosition(),box.isFirstPartition(),box.isSecondPartition(),box.isThirdPartition(),list));
                }
                if(BoxList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterStorageSlot = new StorageBoxAdapter(getContext(),BoxItemList);
                            LvStorageSlot.setAdapter(adapterStorageSlot);
                        }
                    });
                }
                RefreshStorageSlotLayout.setRefreshing(false);
            }
        }).start();
    }

    private void deleteStorageSlot(final allStorageBoxPos boxPos){
        new Thread(new Runnable() {
            @Override
            public void run() {
                if(!DataHandler.activateLED(boxPos.getStoragePosition(),clipboard.User.getColor(),0,true,true)){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(getContext(), "Please wait! Someone else is using the storage slot!", Toast.LENGTH_LONG).show();
                        }
                    });
                }
                else {
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            StoragePosAdapter adapter = new StoragePosAdapter(getContext(),boxPos.getList());
                            PopupDeleteSlot = new Dialog(getContext());
                            PopupDeleteSlot.setContentView(R.layout.popup_box_data);
                            ListView lvPos=PopupDeleteSlot.findViewById(R.id.lvItemPos);
                            View vHeader = getLayoutInflater().inflate(R.layout.overview_layout,lvPos,false);
                            lvPos.addHeaderView(vHeader,null,false);
                            lvPos.setAdapter(adapter);
                            PopupDeleteSlot.setOnCancelListener(new DialogInterface.OnCancelListener() {
                                @Override
                                public void onCancel(DialogInterface dialogInterface) {
                                    new Thread(new Runnable() {
                                        @Override
                                        public void run() {
                                            DataHandler.deactivateLED(boxPos.getStoragePosition());
                                        }
                                    }).start();
                                }
                            });
                            Button btnDelete = PopupDeleteSlot.findViewById(R.id.btnDeleteStorageSlot);
                            btnDelete.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    PopupDeleteSlot.dismiss();
                                    new Thread(new Runnable() {
                                        @Override
                                        public void run() {
                                            DataHandler.deactivateLED(boxPos.getStoragePosition());
                                            List<storagePosTable> posList = boxPos.getList();
                                            DataHandler.updateDividers(boxPos.getId(),false,false,false);
                                            for (storagePosTable pos:posList){
                                                DataHandler.deleteStoragePos(pos.getId());
                                            }
                                            getActivity().runOnUiThread(new Runnable() {
                                                @Override
                                                public void run() {
                                                    refresh();
                                                }
                                            });
                                        }
                                    }).start();
                                }
                            });

                            PopupDeleteSlot.show();
                        }
                    });
                }
            }
        }).start();
    }

    @Override
    public void onResume() {
        setConstraints();
        if(BoxListSet) {
            refresh();
        }
        super.onResume();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if(PopupLoading.isRunning()){
            PopupLoading.stopDialog();
        }
        if(PopupDeleteSlot!=null){
            PopupDeleteSlot.dismiss();
        }
    }
}
