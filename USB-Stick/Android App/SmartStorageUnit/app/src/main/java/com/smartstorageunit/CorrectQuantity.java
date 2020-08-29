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
import android.widget.NumberPicker;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import java.util.List;

import adapter.StoragePosAdapter;
import adapter.ItemListAdapter;
import adapter.OverviewAdapter;
import tables.storagePosTable;
import tables.itemList;
import tables.overview;
import tables.storageBox;

public class CorrectQuantity extends Fragment {

    private ConstraintLayout layout;
    private EditText LblSearch;
    private ListView LvCorQuantity;
    private SwipeRefreshLayout RefreshCorQuantityLayout;

    private List<storagePosTable> CorQuantityList=null;
    private StoragePosAdapter adapterCorQuantity;

    private boolean CorQuantityListSet=false;

    private Dialog PopupQuantity=null;

    private storageBox StorageBox;

    private AdapterView.OnItemClickListener listClick = new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView adapterView, View view, int i, long l) {
            storagePosTable corQuantity = (storagePosTable) LvCorQuantity.getItemAtPosition(i);
            updateQuantity(corQuantity);
        }
    };

    public CorrectQuantity() {
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
        LvCorQuantity = rootView.findViewById(R.id.lvOverview);
        RefreshCorQuantityLayout = rootView.findViewById(R.id.swipeRefreshOv);
        RefreshItmLayout = rootView.findViewById(R.id.swipeRefreshItems);

        RefreshItmLayout.setVisibility(View.INVISIBLE);
        TxtNotInStorage.setVisibility(View.INVISIBLE);

        setConstraints();
        setListener();
        fillOverviewList();

        return rootView;
    }

    private void setConstraints(){
        ConstraintLayout.LayoutParams params = (ConstraintLayout.LayoutParams) RefreshCorQuantityLayout.getLayoutParams();
        RefreshCorQuantityLayout.setLayoutParams(new ConstraintLayout.LayoutParams(params.width,ScaleElements.getHeight(78)));

        ConstraintSet set = new ConstraintSet();
        set.clone(layout);

        set.connect(LblSearch.getId(),ConstraintSet.LEFT,layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(2));
        set.connect(LblSearch.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));

        set.connect(RefreshCorQuantityLayout.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(8));
        set.connect(RefreshCorQuantityLayout.getId(),ConstraintSet.LEFT,layout.getId(),ConstraintSet.LEFT);
        set.connect(RefreshCorQuantityLayout.getId(),ConstraintSet.RIGHT,layout.getId(),ConstraintSet.RIGHT);

        set.applyTo(layout);
    }

    private void fillOverviewList(){
        PopupLoading.context=getContext();
        PopupLoading.startDialog();
        new Thread(new Runnable() {
            @Override
            public void run() {
                CorQuantityList = DataHandler.getAllStoragep();
                if (CorQuantityList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterCorQuantity = new StoragePosAdapter(getContext(), CorQuantityList);
                            LayoutInflater inflater = getLayoutInflater();
                            View ovHeader = inflater.inflate(R.layout.overview_layout, LvCorQuantity, false);
                            LvCorQuantity.addHeaderView(ovHeader, null, false);
                            LvCorQuantity.setAdapter(adapterCorQuantity);
                            CorQuantityListSet = true;
                        }
                    });
                }
                PopupLoading.stopDialog();
            }
        }).start();
    }

    private void setListener(){
        RefreshCorQuantityLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refresh();
                LblSearch.setText("");
            }
        });

        LvCorQuantity.setOnItemClickListener(listClick);

        LblSearch.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if(adapterCorQuantity!=null) {
                    adapterCorQuantity.filter(charSequence.toString());
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private void refresh(){
        LblSearch.setText("");
        if(CorQuantityList!=null){
            adapterCorQuantity.clear();
        }
        new Thread(new Runnable() {
            @Override
            public void run() {
                CorQuantityList = DataHandler.getAllStoragep();
                if(CorQuantityList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterCorQuantity = new StoragePosAdapter(getContext(),CorQuantityList);
                            LvCorQuantity.setAdapter(adapterCorQuantity);
                        }
                    });
                }
                RefreshCorQuantityLayout.setRefreshing(false);
            }
        }).start();
    }

    private void updateQuantity(final storagePosTable list){
        new Thread(new Runnable() {
            @Override
            public void run() {
                StorageBox = DataHandler.getStorageBoxData(list.getStoragehId()).get(0);
                if(!DataHandler.activateLED(StorageBox.getStoragePosition(),clipboard.User.getColor(),0,true,true)){
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
                            PopupQuantity = new Dialog(getContext());
                            PopupQuantity.setContentView(R.layout.popup_quantity);
                            TextView txtTitle = PopupQuantity.findViewById(R.id.txtQuantity);
                            final NumberPicker nbpQuantity = PopupQuantity.findViewById(R.id.nbpQuantity);
                            Button btnOk = PopupQuantity.findViewById(R.id.btnQuantity);

                            txtTitle.setText("Position of item: "+list.getInsidePos());
                            nbpQuantity.setMinValue(0);
                            nbpQuantity.setMaxValue(list.getMaxQuantity());
                            nbpQuantity.setValue(list.getQuantity());

                            PopupQuantity.setOnCancelListener(new DialogInterface.OnCancelListener() {
                                @Override
                                public void onCancel(DialogInterface dialogInterface) {
                                    new Thread(new Runnable() {
                                        @Override
                                        public void run() {
                                            DataHandler.deactivateLED(StorageBox.getStoragePosition());
                                        }
                                    }).start();
                                }
                            });

                            btnOk.setOnClickListener(new View.OnClickListener() {
                                @Override
                                public void onClick(View view) {
                                    PopupQuantity.dismiss();
                                    nbpQuantity.setEnabled(false);
                                    new Thread(new Runnable() {
                                        @Override
                                        public void run() {
                                            DataHandler.updateQuantity(list.getId(),nbpQuantity.getValue());
                                            DataHandler.deactivateLED(StorageBox.getStoragePosition());
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

                            PopupQuantity.show();
                        }
                    });
                }
            }
        }).start();

    }

    @Override
    public void onResume() {
        setConstraints();
        if(CorQuantityListSet) {
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
        if(PopupQuantity!=null){
            PopupQuantity.dismiss();
        }
    }
}
