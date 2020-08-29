package tables;


import java.io.Serializable;

public class users implements Serializable{

    private int Id;
    private String Username;
    private String Password;
    private String Color;
    private String Email;
    private boolean MonthlyNotification;
    private boolean UserSignedIn;
    private int PermissionID;

    public users(int id, String username, String password, String color, String email, boolean monthlyNotification, boolean userSignedIn, int permissionID) {
        Id = id;
        Username = username;
        Password = password;
        Color = color;
        Email = email;
        MonthlyNotification = monthlyNotification;
        UserSignedIn = userSignedIn;
        PermissionID = permissionID;
    }



    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }

    public String getUsername() {
        return Username;
    }

    public void setUsername(String username) {
        Username = username;
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String password) {
        Password = password;
    }

    public String getColor() {
        return Color;
    }

    public void setColor(String color) {
        Color = color;
    }

    public String getEmail() {
        return Email;
    }

    public void setEmail(String email) {
        Email = email;
    }

    public boolean isMonthlyNotification() {
        return MonthlyNotification;
    }

    public void setMonthlyNotification(boolean monthlyNotification) {
        MonthlyNotification = monthlyNotification;
    }

    public boolean isUserSignedIn() {
        return UserSignedIn;
    }

    public void setUserSignedIn(boolean userSignedIn) {
        UserSignedIn = userSignedIn;
    }

    public int getPermissionID() {
        return PermissionID;
    }

    public void setPermissionID(int permissionID) {
        PermissionID = permissionID;
    }


}
