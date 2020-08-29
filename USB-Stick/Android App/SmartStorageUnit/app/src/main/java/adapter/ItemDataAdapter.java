package adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import com.smartstorageunit.R;

import java.util.List;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import tables.itemData;

public class ItemDataAdapter extends ArrayAdapter<itemData> {

    public ItemDataAdapter(Context context, List<itemData> list){
        super(context,0,list);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        itemData iData = getItem(position);

        if(convertView==null){
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.item_data_list_layout,parent,false);
        }

        TextView txtName = convertView.findViewById(R.id.txtRefName);
        TextView txtValue = convertView.findViewById(R.id.txtValue);
        TextView txtUnit = convertView.findViewById(R.id.txtUnit);

        txtName.setText(iData.getRefName());
        txtValue.setText(iData.getValue());
        txtUnit.setText(iData.getUnit());

        return convertView;
    }
}
