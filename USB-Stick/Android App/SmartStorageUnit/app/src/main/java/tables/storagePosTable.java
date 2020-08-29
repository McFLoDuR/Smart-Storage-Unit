package tables;

public class storagePosTable {

    private String ComponentName;
    private String ArticleNumber;
    private int Quantity;
    private int Id;
    private int StoragehId;
    private int InsidePos;
    private int MaxQuantity;

    public storagePosTable(String componentName, String articleNumber, int quantity, int id, int storagehId, int insidePos, int maxQuantity) {
        ComponentName = componentName;
        ArticleNumber = articleNumber;
        Quantity = quantity;
        Id = id;
        StoragehId = storagehId;
        InsidePos = insidePos;
        MaxQuantity = maxQuantity;
    }

    public String getComponentName() {
        return ComponentName;
    }

    public void setComponentName(String componentName) {
        ComponentName = componentName;
    }

    public String getArticleNumber() {
        return ArticleNumber;
    }

    public void setArticleNumber(String articleNumber) {
        ArticleNumber = articleNumber;
    }

    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int quantity) {
        Quantity = quantity;
    }

    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }

    public int getStoragehId() {
        return StoragehId;
    }

    public void setStoragehId(int storagehId) {
        StoragehId = storagehId;
    }

    public int getInsidePos() {
        return InsidePos;
    }

    public void setInsidePos(int insidePos) {
        InsidePos = insidePos;
    }

    public int getMaxQuantity() {
        return MaxQuantity;
    }

    public void setMaxQuantity(int maxQuantity) {
        MaxQuantity = maxQuantity;
    }
}
