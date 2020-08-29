package adapter;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.smartstorageunit.R;

import java.util.ArrayList;
import java.util.List;

import tables.allStorageBoxPos;
import tables.storageBox;
import tables.storagePosTable;

public class StorageBoxAdapter extends ArrayAdapter<allStorageBoxPos> {

    private List<allStorageBoxPos> BoxList;
    private List<allStorageBoxPos> BoxListCpy;

    public StorageBoxAdapter(@NonNull Context context, @NonNull List<allStorageBoxPos> objects) {
        super(context, 0, objects);

        BoxList=objects;
        BoxListCpy=new ArrayList<>();
        BoxListCpy.addAll(BoxList);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        allStorageBoxPos box = getItem(position);

        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.storagebox_list_layout, parent, false);
        }

        TextView tvStorageID = convertView.findViewById(R.id.txtStorageID);
        TextView tvDiv1 = convertView.findViewById(R.id.txtDivider1);
        TextView tvDiv2 = convertView.findViewById(R.id.txtDivider2);
        TextView tvDiv3 = convertView.findViewById(R.id.txtDivider3);

        tvStorageID.setText(box.getId()+"");
        tvDiv1.setText(box.isFirstPartition()+"");
        tvDiv2.setText(box.isSecondPartition()+"");
        tvDiv3.setText(box.isThirdPartition()+"");

        tvStorageID.setTextColor(Color.GRAY);
        tvDiv1.setTextColor(Color.GRAY);
        tvDiv2.setTextColor(Color.GRAY);
        tvDiv3.setTextColor(Color.GRAY);

        convertView.setBackgroundColor(Color.WHITE);

        return convertView;
    }

    public void filter(String text){
        text = text.toLowerCase();
        BoxList.clear();
        if (text.length() == 0) {
            BoxList.addAll(BoxListCpy);
        }
        else
        {
            for (allStorageBoxPos itm : BoxListCpy)
            {
                List<storagePosTable> posList = itm.getList();
                for(storagePosTable pos:posList){
                    if (pos.getComponentName().toLowerCase().contains(text))
                    {
                        BoxList.add(itm);
                    }
                else if(pos.getArticleNumber().toLowerCase().contains(text)){
                        BoxList.add(itm);
                    }
                }

            }
        }
        notifyDataSetChanged();
    }
}
