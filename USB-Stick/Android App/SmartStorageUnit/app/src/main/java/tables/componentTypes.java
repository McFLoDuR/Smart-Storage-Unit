package tables;

public class componentTypes {

    private int Id;
    private String TypeName;
    private String TypeVersion;

    public componentTypes(int id, String typeName, String typeVersion) {
        Id = id;
        TypeName = typeName;
        TypeVersion = typeVersion;
    }

    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }

    public String getTypeName() {
        return TypeName;
    }

    public void setTypeName(String typeName) {
        TypeName = typeName;
    }

    public String getTypeVersion() {
        return TypeVersion;
    }

    public void setTypeVersion(String typeVersion) {
        TypeVersion = typeVersion;
    }
}
