package tables;

public class permissions {

    private int Id;
    private String Name;
    private boolean ManageUsers;
    private boolean StoreItems;
    private boolean WithdrawItems;
    private boolean DeleteStorageSlot;
    private boolean MoveStorageSlot;
    private boolean ManagePartitions;
    private boolean CorrectQuantity;
    private boolean CreateInventoryReport;

    public permissions(int id, String name, boolean manageUsers, boolean storeItems, boolean withdrawItems, boolean deleteStorageSlot, boolean moveStorageSlot, boolean managePartitions, boolean correctQuantity, boolean createInventoryReport) {
        Id = id;
        Name = name;
        ManageUsers = manageUsers;
        StoreItems = storeItems;
        WithdrawItems = withdrawItems;
        DeleteStorageSlot = deleteStorageSlot;
        MoveStorageSlot = moveStorageSlot;
        ManagePartitions = managePartitions;
        CorrectQuantity = correctQuantity;
        CreateInventoryReport = createInventoryReport;
    }

    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    public boolean isManageUsers() {
        return ManageUsers;
    }

    public void setManageUsers(boolean manageUsers) {
        ManageUsers = manageUsers;
    }

    public boolean isStoreItems() {
        return StoreItems;
    }

    public void setStoreItems(boolean storeItems) {
        StoreItems = storeItems;
    }

    public boolean isWithdrawItems() {
        return WithdrawItems;
    }

    public void setWithdrawItems(boolean withdrawItems) {
        WithdrawItems = withdrawItems;
    }

    public boolean isDeleteStorageSlot() {
        return DeleteStorageSlot;
    }

    public void setDeleteStorageSlot(boolean deleteStorageSlot) {
        DeleteStorageSlot = deleteStorageSlot;
    }

    public boolean isMoveStorageSlot() {
        return MoveStorageSlot;
    }

    public void setMoveStorageSlot(boolean moveStorageSlot) {
        MoveStorageSlot = moveStorageSlot;
    }

    public boolean isManagePartitions() {
        return ManagePartitions;
    }

    public void setManagePartitions(boolean managePartitions) {
        ManagePartitions = managePartitions;
    }

    public boolean isCorrectQuantity() {
        return CorrectQuantity;
    }

    public void setCorrectQuantity(boolean correctQuantity) {
        CorrectQuantity = correctQuantity;
    }

    public boolean isCreateInventoryReport() {
        return CreateInventoryReport;
    }

    public void setCreateInventoryReport(boolean createInventoryReport) {
        CreateInventoryReport = createInventoryReport;
    }
}
