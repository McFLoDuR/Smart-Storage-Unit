package tables;

public class itemData {

    private String RefName;
    private String Value;
    private String Unit;

    public itemData(String refName, String value, String unit) {
        RefName = refName;
        Value = value;
        Unit = unit;
    }

    public String getRefName() {
        return RefName;
    }

    public void setRefName(String refName) {
        RefName = refName;
    }

    public String getValue() {
        return Value;
    }

    public void setValue(String value) {
        Value = value;
    }

    public String getUnit() {
        return Unit;
    }

    public void setUnit(String unit) {
        Unit = unit;
    }
}
