package com.smartstorageunit;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

public class InventoryReport extends Fragment {

    ConstraintLayout Layout;
    Button BtnMode1;
    Button BtnMode2;
    Button BtnMode3;
    TextView TxtEmailText;
    TextView TxtEmail;

    public InventoryReport() {
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_report,container,false);

        Layout = rootView.findViewById(R.id.constFragLayout);
        BtnMode1 = rootView.findViewById(R.id.btnMode1);
        BtnMode2 = rootView.findViewById(R.id.btnMode2);
        BtnMode3 = rootView.findViewById(R.id.btnMode3);
        TxtEmailText = rootView.findViewById(R.id.txtReport);
        TxtEmail = rootView.findViewById(R.id.txtEmailAddress);

        setConstraints();
        setListener();

        TxtEmail.setText(clipboard.User.getEmail());

        return rootView;
    }

    private void setConstraints(){
        ConstraintSet set = new ConstraintSet();
        set.clone(Layout);

        set.connect(BtnMode1.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(30));

        set.connect(BtnMode2.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(40));

        set.connect(BtnMode3.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(50));

        set.connect(TxtEmailText.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(5));

        set.connect(TxtEmail.getId(),ConstraintSet.TOP,Layout.getId(),ConstraintSet.TOP,ScaleElements.getHeight(10));

        set.applyTo(Layout);
    }

    private void setListener(){
        BtnMode1.setOnClickListener(btnMode1Clicked);
        BtnMode2.setOnClickListener(btnMode2Clicked);
        BtnMode3.setOnClickListener(btnMode3Clicked);
    }

    private View.OnClickListener btnMode1Clicked = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            createInvetoryReport(1);
        }
    };

    private View.OnClickListener btnMode2Clicked= new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            createInvetoryReport(2);
        }
    };

    private View.OnClickListener btnMode3Clicked= new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            createInvetoryReport(3);
        }
    };

    private void createInvetoryReport(final int mode){
        disableButtons();
        new Thread(new Runnable() {
            @Override
            public void run() {
                DataHandler.createInventoryReport(clipboard.User.getId(),mode);
                getActivity().runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(getContext(),"Your report will be send shortly!",Toast.LENGTH_LONG).show();
                        changeFragment();
                    }
                });
            }
        }).start();
    }

    private void changeFragment(){
        Overview overview = new Overview();
        FragmentTransaction fragmentTransaction = getActivity().getSupportFragmentManager().beginTransaction();
        fragmentTransaction.replace(R.id.windowFrame, overview,"overview");
        fragmentTransaction.commit();
    }

    public void disableButtons(){
        BtnMode1.setEnabled(false);
        BtnMode2.setEnabled(false);
        BtnMode3.setEnabled(false);
    }

    @Override
    public void onResume() {
        setConstraints();
        super.onResume();
    }
}
