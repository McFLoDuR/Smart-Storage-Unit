package adapter;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import com.smartstorageunit.R;

import java.util.ArrayList;
import java.util.List;

import tables.storagePosTable;
import tables.overview;

public class StoragePosAdapter extends ArrayAdapter<storagePosTable> {

    private List<storagePosTable> List;
    private List<storagePosTable> CpyList;

    public StoragePosAdapter(@NonNull Context context, @NonNull List<storagePosTable> objects) {
        super(context, 0, objects);
        List = objects;
        CpyList = new ArrayList<>();
        CpyList.addAll(List);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        storagePosTable corQuantity = getItem(position);

        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.overview_layout, parent, false);
        }

        TextView tvType = convertView.findViewById(R.id.tvComponentName);
        TextView tvArticleNum = convertView.findViewById(R.id.tvArticleNum);
        TextView tvQuantity = convertView.findViewById(R.id.tvQuantity);

        tvType.setText(corQuantity.getComponentName());
        tvArticleNum.setText(corQuantity.getArticleNumber());
        tvQuantity.setText(corQuantity.getQuantity()+"");

        tvType.setTextColor(Color.GRAY);
        tvArticleNum.setTextColor(Color.GRAY);
        tvQuantity.setTextColor(Color.GRAY);

        convertView.setBackgroundColor(Color.WHITE);

        return convertView;
    }

    public void filter(String text){
        text = text.toLowerCase();
        List.clear();
        if (text.length() == 0) {
            List.addAll(CpyList);
        }
        else
        {
            for (storagePosTable corQuantity : CpyList)
            {
                if (corQuantity.getComponentName().toLowerCase().contains(text))
                {
                    List.add(corQuantity);
                }
                else if(corQuantity.getArticleNumber().toLowerCase().contains(text)){
                    List.add(corQuantity);
                }
            }
        }
        notifyDataSetChanged();
    }
}
