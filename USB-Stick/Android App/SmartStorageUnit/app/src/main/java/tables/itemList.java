package tables;

public class itemList {

    private String TypeName;
    private String ArticleNum;
    private int ItemID;
    private int TypeID;
    private double Weight;
    private String TypeVersion;

    public itemList(String typeName, String articleNum, int itemID, int typeID, double weight, String typeVersion) {
        TypeName = typeName;
        ArticleNum = articleNum;
        ItemID = itemID;
        TypeID = typeID;
        Weight = weight;
        TypeVersion = typeVersion;
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

    public double getWeight() {
        return Weight;
    }

    public void setWeight(double weight) {
        Weight = weight;
    }

    public String getTypeVersion() {
        return TypeVersion;
    }

    public void setTypeVersion(String typeVersion) {
        TypeVersion = typeVersion;
    }
}
