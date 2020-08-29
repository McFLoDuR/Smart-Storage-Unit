package adapter;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import com.smartstorageunit.R;

import java.util.ArrayList;
import java.util.List;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import tables.itemList;

public class ItemListAdapter extends ArrayAdapter<itemList> {

    private List<itemList> ItemList;
    private List<itemList> ItemListCopy;

    public ItemListAdapter(@NonNull Context context, @NonNull List<itemList> objects) {
        super(context, 0, objects);
        ItemList=objects;
        ItemListCopy =new ArrayList<>();
        ItemListCopy.addAll(ItemList);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        itemList itm= getItem(position);

        if(convertView==null){
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.item_list_layout,parent,false);
        }

        TextView txtComponent = convertView.findViewById(R.id.txtItemListComponent);
        TextView txtType = convertView.findViewById(R.id.txtItemListType);
        TextView txtArticle = convertView.findViewById(R.id.txtItemListArticle);

        txtComponent.setText(itm.getTypeName());
        txtType.setText(itm.getTypeVersion());
        txtArticle.setText(itm.getArticleNum());

        txtComponent.setTextColor(Color.GRAY);
        txtArticle.setTextColor(Color.GRAY);
        txtType.setTextColor(Color.GRAY);

        return convertView;
    }

    public void filter(String text){
        text = text.toLowerCase();
        ItemList.clear();
        if (text.length() == 0) {
            ItemList.addAll(ItemListCopy);
        }
        else
        {
            for (itemList item : ItemListCopy)
            {
                if (item.getTypeName().toLowerCase().contains(text))
                {
                    ItemList.add(item);
                }
                else if(item.getArticleNum().toLowerCase().contains(text)){
                    ItemList.add(item);
                }
            }
        }
        notifyDataSetChanged();
    }
}
