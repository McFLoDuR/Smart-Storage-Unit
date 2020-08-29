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

import tables.overview;

public class OverviewAdapter extends ArrayAdapter<overview> {

    private List<overview> ovList=null;
    private List<overview> ovCopy;

    public OverviewAdapter(Context context, List<overview> overview) {
        super(context,0, overview);
        ovList=overview;
        ovCopy=new ArrayList<>();
        ovCopy.addAll(ovList);
    }
    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        overview ov = getItem(position);

        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.overview_layout, parent, false);
        }

        TextView tvType = convertView.findViewById(R.id.tvComponentName);
        TextView tvArticleNum = convertView.findViewById(R.id.tvArticleNum);
        TextView tvQuantity = convertView.findViewById(R.id.tvQuantity);

        tvType.setText(ov.getTypeName());
        tvArticleNum.setText(ov.getArticleNum());
        tvQuantity.setText(ov.getQuantity()+"");

        tvType.setTextColor(Color.GRAY);
        tvArticleNum.setTextColor(Color.GRAY);
        tvQuantity.setTextColor(Color.GRAY);

        convertView.setBackgroundColor(Color.WHITE);

        if(ov.getAlarmActive()){
            if(ov.getQuantity()<ov.getQuantityMin()) {
                convertView.setBackgroundColor(Color.YELLOW);
            }
            if(ov.getQuantity()==0){
                convertView.setBackgroundColor(Color.RED);
            }
        }

        return convertView;
    }

    public void filter(String text){
        text = text.toLowerCase();
        ovList.clear();
        if (text.length() == 0) {
            ovList.addAll(ovCopy);
        }
        else
        {
            for (overview ov : ovCopy)
            {
                if (ov.getTypeName().toLowerCase().contains(text))
                {
                    ovList.add(ov);
                }
                else if(ov.getArticleNum().toLowerCase().contains(text)){
                    ovList.add(ov);
                }
            }
        }
        notifyDataSetChanged();
    }

}
