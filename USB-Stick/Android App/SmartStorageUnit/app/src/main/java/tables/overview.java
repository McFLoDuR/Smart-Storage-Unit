package tables;

import java.io.Serializable;

public class overview implements Serializable {
    private String TypeName;
    private String ArticleNum;
    private int Quantity;
    private boolean AlarmActive;
    private int QuantityMin;
    private int ItemID;
    private int TypeID;
    private double Weight;

    public overview() {
    }

    public overview(String typeName, String articleNum, int quantity, boolean alarmActive, int quantityMin, int itemID, int typeID, double weight) {
        TypeName = typeName;
        ArticleNum = articleNum;
        Quantity = quantity;
        AlarmActive = alarmActive;
        QuantityMin = quantityMin;
        ItemID = itemID;
        TypeID = typeID;
        Weight = weight;
    }

    public int getItemID() {
        return ItemID;
    }

    public void setItemID(int itemID) {
        ItemID = itemID;
    }

    public int getTypeID() {
        return TypeID;
    }

    public void setTypeID(int typeID) {
        TypeID = typeID;
    }

    public boolean getAlarmActive() {
        return AlarmActive;
    }

    public void setAlarmActive(boolean alarmActive) {
        AlarmActive = alarmActive;
    }

    public int getQuantityMin() {
        return QuantityMin;
    }

    public void setQuantityMin(int quantityMin) {
        QuantityMin = quantityMin;
    }

    public String getTypeName() {
        return TypeName;
    }

    public void setTypeName(String typeName) {
        TypeName = typeName;
    }

    public String getArticleNum() {
        return ArticleNum;
    }

    public void setArticleNum(String articleNum) {
        ArticleNum = articleNum;
    }

    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int quantity) {
        Quantity = quantity;
    }

    public double getWeight() {
        return Weight;
    }

    public void setWeight(double weight) {
        Weight = weight;
    }
}
