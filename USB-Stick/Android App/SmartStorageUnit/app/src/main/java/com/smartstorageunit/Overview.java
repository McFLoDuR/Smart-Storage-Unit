package com.smartstorageunit;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import java.util.List;

import adapter.ItemListAdapter;
import adapter.OverviewAdapter;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;
import tables.itemList;
import tables.overview;

public class Overview extends Fragment {

    private ConstraintLayout layout;
    private EditText LblSearch;
    private TextView TxtNotInStorage;
    private ListView LvOverview;
    private ListView LvItems;
    private SwipeRefreshLayout RefreshOvLayout;
    private SwipeRefreshLayout RefreshItmLayout;

    private List<overview> OverviewList=null;
    private OverviewAdapter adapterOv;

    private List<itemList> ItemList=null;
    private ItemListAdapter adapterItem;

    private boolean overviewListSet=false;
    private boolean itemListSet=false;

    public Overview(){}

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_overview,container,false);
        layout = rootView.findViewById(R.id.constLayoutOverview);
        LblSearch = rootView.findViewById(R.id.lblSearch);
        TxtNotInStorage = rootView.findViewById(R.id.txtItemNotInStorage);
        LvOverview = rootView.findViewById(R.id.lvOverview);
        LvItems = rootView.findViewById(R.id.lvItems);
        RefreshOvLayout = rootView.findViewById(R.id.swipeRefreshOv);
        RefreshItmLayout = rootView.findViewById(R.id.swipeRefreshItems);

        setConstraints();
        setListener();
        fillOverviewList();

        return rootView;
    }
    private void setConstraints(){
        ConstraintSet set = new ConstraintSet();
        set.clone(layout);

        set.connect(LblSearch.getId(),ConstraintSet.LEFT,layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(2));
        set.connect(LblSearch.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(1));

        set.connect(RefreshOvLayout.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(8));

        set.connect(TxtNotInStorage.getId(),ConstraintSet.LEFT,layout.getId(),ConstraintSet.LEFT,ScaleElements.getWidth(2));
        set.connect(TxtNotInStorage.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(10)+RefreshOvLayout.getLayoutParams().height);

        set.connect(RefreshItmLayout.getId(),ConstraintSet.TOP,layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(14)+RefreshOvLayout.getLayoutParams().height);

        set.applyTo(layout);
    }

    private void setListener(){
        RefreshOvLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refresh();
                LblSearch.setText("");
            }
        });

        RefreshItmLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refresh();
                LblSearch.setText("");
            }
        });

        LvOverview.setOnItemClickListener(listClick);
        LvItems.setOnItemClickListener(itemListClick);

        LblSearch.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if(adapterOv!=null) {
                    adapterOv.filter(charSequence.toString());
                }
                if(adapterItem!=null){
                    adapterItem.filter(charSequence.toString());
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private AdapterView.OnItemClickListener listClick = new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView adapterView, View view, int i, long l) {
            clipboard.Overview = (overview) LvOverview.getItemAtPosition(i);

            changeFragment(false);
        }
    };

    private AdapterView.OnItemClickListener itemListClick = new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
            itemList itm = (itemList) LvItems.getItemAtPosition(i);
            overview ov = new overview();
            ov.setItemID(itm.getItemID());
            ov.setTypeID(itm.getTypeID());
            ov.setTypeName(itm.getTypeName());
            ov.setArticleNum(itm.getArticleNum());
            ov.setWeight(itm.getWeight());
            clipboard.Overview = ov;

            changeFragment(true);
        }
    };

    private void changeFragment(boolean state){
        Bundle bundle = new Bundle();
        bundle.putBoolean("newItem",state);
        ItemData data = new ItemData();
        data.setArguments(bundle);
        FragmentManager frgManager=getFragmentManager();
        frgManager.beginTransaction().replace(R.id.windowFrame,data,"ItemData").commit();
        getActivity().setTitle("Item data");
    }

    private void refresh(){
        if(OverviewList!=null){
            adapterOv.clear();
        }
        if(ItemList!=null){
            adapterItem.clear();
        }
        new Thread(new Runnable() {
            @Override
            public void run() {
                OverviewList = DataHandler.getOverviewData();
                ItemList = DataHandler.getItemListData();
                if(OverviewList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterOv = new OverviewAdapter(getContext(),OverviewList);
                            LvOverview.setAdapter(adapterOv);
                        }
                    });
                }
                if(ItemList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterItem = new ItemListAdapter(getContext(),ItemList);
                            LvItems.setAdapter(adapterItem);
                        }
                    });
                }
                RefreshOvLayout.setRefreshing(false);
                RefreshItmLayout.setRefreshing(false);
            }
        }).start();
    }

    private void fillOverviewList(){
        PopupLoading.context=getContext();
        PopupLoading.startDialog();
        new Thread(new Runnable() {
            @Override
            public void run() {
                OverviewList = DataHandler.getOverviewData();
                ItemList = DataHandler.getItemListData();
                if (OverviewList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterOv = new OverviewAdapter(getContext(), OverviewList);
                            LayoutInflater inflater = getLayoutInflater();
                            View ovHeader = inflater.inflate(R.layout.overview_layout, LvOverview, false);
                            LvOverview.addHeaderView(ovHeader, null, false);
                            LvOverview.setAdapter(adapterOv);
                            overviewListSet = true;
                        }
                    });
                }
                if(ItemList!=null){
                    getActivity().runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            adapterItem = new ItemListAdapter(getContext(), ItemList);
                            LayoutInflater inflater = getLayoutInflater();
                            View itmHeader = inflater.inflate(R.layout.item_list_layout, LvItems, false);
                            LvItems.addHeaderView(itmHeader, null, false);
                            LvItems.setAdapter(adapterItem);
                            itemListSet = true;
                        }
                    });
                }
                PopupLoading.stopDialog();
            }
        }).start();
    }

    @Override
    public void onResume() {
        setConstraints();
        if(overviewListSet&&itemListSet) {
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
    }
}
