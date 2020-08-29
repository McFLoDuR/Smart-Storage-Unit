package tables;

import java.util.List;

public class allStorageBoxPos {

    private int Id;
    private int StoragePosition;
    private boolean FirstPartition;
    private boolean SecondPartition;
    private boolean ThirdPartition;
    private List<storagePosTable> List;

    public allStorageBoxPos(int id, int storagePosition, boolean firstPartition, boolean secondPartition, boolean thirdPartition, java.util.List<storagePosTable> list) {
        Id = id;
        StoragePosition = storagePosition;
        FirstPartition = firstPartition;
        SecondPartition = secondPartition;
        ThirdPartition = thirdPartition;
        List = list;
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

    public java.util.List<storagePosTable> getList() {
        return List;
    }

    public void setList(java.util.List<storagePosTable> list) {
        List = list;
    }
}
