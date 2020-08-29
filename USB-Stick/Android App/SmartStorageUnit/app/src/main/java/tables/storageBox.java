package tables;

public class storageBox {

    private int Id;
    private int StoragePosition;
    private boolean FirstPartition;
    private boolean SecondPartition;
    private boolean ThirdPartition;

    public storageBox(int id, int storagePosition, boolean firstPartition, boolean secondPartition, boolean thirdPartition) {
        Id = id;
        StoragePosition = storagePosition;
        FirstPartition = firstPartition;
        SecondPartition = secondPartition;
        ThirdPartition = thirdPartition;
    }

    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }

    public int getStoragePosition() {
        return StoragePosition;
    }

    public void setStoragePosition(int storagePosition) {
        StoragePosition = storagePosition;
    }

    public boolean isFirstPartition() {
        return FirstPartition;
    }

    public void setFirstPartition(boolean firstPartition) {
        FirstPartition = firstPartition;
    }

    public boolean isSecondPartition() {
        return SecondPartition;
    }

    public void setSecondPartition(boolean secondPartition) {
        SecondPartition = secondPartition;
    }

    public boolean isThirdPartition() {
        return ThirdPartition;
    }

    public void setThirdPartition(boolean thirdPartition) {
        ThirdPartition = thirdPartition;
    }
}
