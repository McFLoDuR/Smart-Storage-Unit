package tables;

public class storagePosition {

    private int ID;
    private int StorageID;
    private int ItemID;
    private int InsidePosition;
    private int Quantity;
    private int QuantityMax;

    public storagePosition(int ID, int storageID, int itemID, int insidePosition, int quantity, int quantityMax) {
        this.ID = ID;
        StorageID = storageID;
        ItemID = itemID;
        InsidePosition = insidePosition;
        Quantity = quantity;
        QuantityMax = quantityMax;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public int getStorageID() {
        return StorageID;
    }

    public void setStorageID(int storageID) {
        StorageID = storageID;
    }

    public int getItemID() {
        return ItemID;
    }

    public void setItemID(int itemID) {
        ItemID = itemID;
    }

    public int getInsidePosition() {
        return InsidePosition;
    }

    public void setInsidePosition(int insidePosition) {
        InsidePosition = insidePosition;
    }

    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int quantity) {
        Quantity = quantity;
    }

    public int getQuantityMax() {
        return QuantityMax;
    }

    public void setQuantityMax(int quantityMax) {
        QuantityMax = quantityMax;
    }
}
