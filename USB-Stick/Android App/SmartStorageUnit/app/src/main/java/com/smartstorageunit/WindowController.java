package com.smartstorageunit;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

import java.io.Serializable;

public class WindowController extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {

    Toolbar ToolOverview;
    DrawerLayout Drawer;
    ActionBarDrawerToggle Toggle;
    NavigationView NavView;

    boolean started=false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.window_controller);

        ToolOverview = findViewById(R.id.tbWindowCon);
        Drawer = findViewById(R.id.ovDrawerLayout);
        NavView = findViewById(R.id.nav_view);

        setSupportActionBar(ToolOverview);
        getSupportActionBar().setDisplayShowHomeEnabled(true);
        getSupportActionBar().setDisplayHomeAsUpEnabled(false);
        getSupportActionBar().setHomeButtonEnabled(true);

        Toggle = new ActionBarDrawerToggle(this,Drawer,ToolOverview,R.string.navigation_drawer_open,R.string.navigation_drawer_close){
            @Override
            public void onDrawerSlide(View drawerView, float slideOffset) {
                if(slideOffset!=0){
                    InputMethodManager imm = (InputMethodManager) WindowController.this.getSystemService(Activity.INPUT_METHOD_SERVICE);
                    View view = WindowController.this.getCurrentFocus();
                    if(view==null){
                        view = new View(WindowController.this);
                    }
                    imm.hideSoftInputFromWindow(view.getWindowToken(),0);
                }
                super.onDrawerSlide(drawerView, slideOffset);
            }
        };
        Drawer.addDrawerListener(Toggle);
        Toggle.syncState();

        ToolOverview.setTitleTextColor(Color.WHITE);

        NavView.setNavigationItemSelectedListener(this);

        NavView.setCheckedItem(R.id.mOverview);
        onNavigationItemSelected(NavView.getCheckedItem());
        checkPermissions();
    }


    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        Fragment fragment = null;
        String tag=null;
        switch (menuItem.getItemId()){
            case R.id.mOverview:
                fragment = new Overview();
                tag="overview";
                break;
            case R.id.mNewItem:
                fragment = new NewItem();
                tag="newItem";
                break;
            case R.id.mCorrectQuantity:
                fragment = new CorrectQuantity();
                tag="correctQuantity";
                break;
            case R.id.mDeleteStoragePos:
                fragment =new DeleteStorageSlot();
                tag="deleteStoragePos";
                break;
            case R.id.mInventoryReport:
                fragment = new InventoryReport();
                tag="inventoryReport";
                break;
        }
        if(fragment!=null){
            loadFragment(fragment,tag);
            setTitle(menuItem.getTitle());
            menuItem.setChecked(true);
            Drawer.closeDrawers();
        }
        return true;
    }

    private void loadFragment(Fragment fragment, String tag){
        FragmentManager frgManager=getSupportFragmentManager();
        frgManager.beginTransaction().replace(R.id.windowFrame,fragment,tag).commit();
    }

    @Override
    protected void onPostCreate(@Nullable Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);
        Toggle.syncState();
    }

    @Override
    protected void onDestroy() {
        if(PopupLoading.isRunning()){
            PopupLoading.stopDialog();
        }
        super.onDestroy();
    }

    @Override
    public void onBackPressed() {
        Fragment homeFragment = getSupportFragmentManager().findFragmentByTag("overview");
        if(Drawer.isDrawerOpen(GravityCompat.START)){
            Drawer.closeDrawer(GravityCompat.START);
        }
        else if(homeFragment==null||!homeFragment.isVisible()){
            NavView.setCheckedItem(R.id.mOverview);
            onNavigationItemSelected(NavView.getCheckedItem());
        }
        else {
            super.onBackPressed();
        }
    }

    private void checkPermissions(){
        Menu navMenu = NavView.getMenu();
        if(!clipboard.Permission.isStoreItems()){
            navMenu.findItem(R.id.mNewItem).setEnabled(false);
        }
        if(!clipboard.Permission.isCorrectQuantity()){
            navMenu.findItem(R.id.mCorrectQuantity).setEnabled(false);
        }
        if(!clipboard.Permission.isDeleteStorageSlot()){
            navMenu.findItem(R.id.mDeleteStoragePos).setEnabled(false);
        }
        if(!clipboard.Permission.isCreateInventoryReport()){
            navMenu.findItem(R.id.mInventoryReport).setEnabled(false);
        }
    }

    @Override
    public void onAttachFragment(Fragment fragment) {
        if(fragment.getTag().equals("overview")){
            MenuItem menu = NavView.getMenu().findItem(R.id.mOverview);
            NavView.setCheckedItem(menu);
            setTitle(menu.getTitle());
        }
        super.onAttachFragment(fragment);
    }

    @Override
    protected void onResume() {
        if(!started){
            started=true;
        }
        else {
            MenuItem menu = NavView.getMenu().findItem(R.id.mOverview);
            NavView.setCheckedItem(menu);
            onNavigationItemSelected(menu);
        }
        super.onResume();
    }

    public void txtLogoutClicked(View view){
        finish();
        Intent startScreen = new Intent(this,Login.class);
        startActivity(startScreen);
    }
}
