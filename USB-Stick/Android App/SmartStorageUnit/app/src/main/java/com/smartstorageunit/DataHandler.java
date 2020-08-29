package com.smartstorageunit;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;

import tables.componentTypes;
import tables.itemData;
import tables.itemList;
import tables.overview;
import tables.permissions;
import tables.references;
import tables.storageBox;
import tables.storagePosTable;
import tables.storagePosition;
import tables.users;

public class DataHandler {

    public static volatile boolean IsHTTPInUse=false;

    public static List<users> getUsersData(){
        List<users> usersList =new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("users",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row= rs.split(";");

        for (String r:row)
        {
            String[] col = r.split("\\|");
            usersList.add(new users(
                    Integer.parseInt(col[0]),
                    col[1],
                    col[2],
                    col[3],
                    col[4],
                    "1".equals(col[5]),
                    "1".equals(col[6]),
                    Integer.parseInt(col[7])
            ));
        }
        return usersList;
    }

    public static List<overview> getOverviewData(){
        List<overview> overviewList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("overview",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            overviewList.add(new overview(
                    col[0],
                    col[1],
                    Integer.parseInt(col[2]),
                    (Integer.parseInt(col[3])>0),
                    Integer.parseInt(col[4]),
                    Integer.parseInt(col[5]),
                    Integer.parseInt(col[6]),
                    Double.parseDouble(col[7])
            ));
        }
        return overviewList;
    }

    public static List<componentTypes> getComponentType(int typeId){
        List<componentTypes> typesList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("component",makeParams("id",typeId+""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            typesList.add(new componentTypes(
                    Integer.parseInt(col[0]),
                    col[1],
                    col[2]
            ));
        }
        return typesList;
    }

    public static List<componentTypes> getComponentTypeList(){
        List<componentTypes> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("componentTypeList",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            list.add(new componentTypes(
                    Integer.parseInt(col[0]),
                    col[1],
                    col[2]
            ));
        }
        return list;
    }

    public static List<componentTypes> getComponentVersionList(String type){
        List<componentTypes> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("componentVersionList",makeParams("type",type));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            list.add(new componentTypes(
                    Integer.parseInt(col[0]),
                    col[1],
                    col[2]
            ));
        }
        return list;
    }

    public static List<componentTypes> getComponentList(){
        List<componentTypes> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("componentList",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            list.add(new componentTypes(
                    Integer.parseInt(col[0]),
                    col[1],
                    col[2]
            ));
        }
        return list;
    }

    public static List<references> getReferenceList(){
        List<references> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("reference",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            list.add(new references(
                    Integer.parseInt(col[0]),
                    col[1]
            ));
        }
        return list;
    }

    public static List<itemData> getItemData(int itemId){
        List<itemData> itemList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("itemdata",makeParams("id",itemId+""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            itemList.add(new itemData(
                    col[0],
                    col[1],
                    col[2]
            ));
        }
        return itemList;
    }

    public static List<storagePosition> getStoragePositionData(int itemId){
        List<storagePosition> storageList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("storagep",makeParams("id",itemId+""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r:row) {
            String[] col = r.split("\\|");
            storageList.add(new storagePosition(
                    Integer.parseInt(col[0]),
                    Integer.parseInt(col[1]),
                    Integer.parseInt(col[2]),
                    Integer.parseInt(col[3]),
                    Integer.parseInt(col[4]),
                    Integer.parseInt(col[5])
            ));
        }
        return storageList;
    }

    public static List<permissions> getPermission(int permissionId){
        List<permissions> permList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("permission",makeParams("id",permissionId+""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            permList.add(new permissions(
                    Integer.parseInt(col[0]),
                    col[1],
                    "1".equals(col[2]),
                    "1".equals(col[3]),
                    "1".equals(col[4]),
                    "1".equals(col[5]),
                    "1".equals(col[6]),
                    "1".equals(col[7]),
                    "1".equals(col[8]),
                    "1".equals(col[9])
            ));
        }
        return permList;
    }

    public static List<storageBox> getStorageBoxData(int storagehId){
        List<storageBox> storageList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("storageh",makeParams("id",storagehId+""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            storageList.add(new storageBox(
                    Integer.parseInt(col[0]),
                    Integer.parseInt(col[1]),
                    "1".equals(col[2]),
                    "1".equals(col[3]),
                    "1".equals(col[4])
            ));
        }
        return storageList;
    }

    public static List<storageBox> getStorageBoxList(){
        List<storageBox> storageList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("storagehList",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            storageList.add(new storageBox(
                    Integer.parseInt(col[0]),
                    Integer.parseInt(col[1]),
                    "1".equals(col[2]),
                    "1".equals(col[3]),
                    "1".equals(col[4])
            ));
        }
        return storageList;
    }

    public static List<storagePosition> getStoragePositionList(int storagehId){
        List<storagePosition> storageList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("storagepList",makeParams("id",storagehId+""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r:row) {
            String[] col = r.split("\\|");
            storageList.add(new storagePosition(
                    Integer.parseInt(col[0]),
                    Integer.parseInt(col[1]),
                    Integer.parseInt(col[2]),
                    Integer.parseInt(col[3]),
                    Integer.parseInt(col[4]),
                    Integer.parseInt(col[5])
            ));
        }
        return storageList;
    }

    public static List<String> getUnitList(){
        List<String> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("unitList",makeParams(""));
        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r:row) {
            String[] col = r.split("\\|");
            list.add(col[0]);
        }
        return list;
    }

    public static List<String> getItemList(){
        List<String> list= new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("itemList",makeParams(""));
        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r:row) {
            String[] col = r.split("\\|");
            list.add(col[0]);
        }
        return list;
    }

    public static List<itemList> getItemListData(){
        List<itemList> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("itemListData",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r:row) {
            String[] col = r.split("\\|");
            list.add(new itemList(
                    col[0],
                    col[1],
                    Integer.parseInt(col[2]),
                    Integer.parseInt(col[3]),
                    Double.parseDouble(col[4]),
                    col[5]
            ));
        }
        return list;
    }

    public static List<storagePosTable> getAllStoragep(){
        List<storagePosTable> list = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("allStoragep",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            list.add(new storagePosTable(
                    col[0],
                    col[1],
                    Integer.parseInt(col[2]),
                    Integer.parseInt(col[3]),
                    Integer.parseInt(col[4]),
                    Integer.parseInt(col[5]),
                    Integer.parseInt(col[6])
            ));
        }
        return list;
    }

    public static List<storageBox> getAllStorageBoxes(){
        List<storageBox> storageList = new ArrayList<>();

        checkHTTPAvailable();
        String rs = executeQuery("allStorageBoxes",makeParams(""));

        if(rs == null||rs.contains("Error")||rs.isEmpty()){
            return null;
        }
        String[] row=rs.split(";");
        for (String r: row) {
            String[] col = r.split("\\|");
            storageList.add(new storageBox(
                    Integer.parseInt(col[0]),
                    Integer.parseInt(col[1]),
                    "1".equals(col[2]),
                    "1".equals(col[3]),
                    "1".equals(col[4])
            ));
        }
        return storageList;
    }

    public static void createInventoryReport(int userId, int mode){
        checkHTTPAvailable();
        //DBConnector.con.setDoInput(false);
        executeQuery("report",makeParams("id",userId+"","mode",mode+""));
        //DBConnector.con.setDoInput(true);
    }

    public static void updateInsidePos(int id, int insidePos){
        checkHTTPAvailable();
        executeQuery("updateInsidePos",makeParams("id",id+"","insidePos",insidePos+""));
    }

    public static void setAlarm(int itemId, boolean state){
        checkHTTPAvailable();
        executeQuery("setAlarm",makeParams("id",itemId+"","state",state+""));
    }

    public static int getRefId(String name){
        checkHTTPAvailable();
        return Integer.parseInt(executeQuery("getRefId",makeParams("name",name)));
    }

    public static void insertReference(String name){
        checkHTTPAvailable();
        executeQuery("insertRef",makeParams("name",name));
    }

    public static void insertItemData(int itemId, int refId, String value, String unit){
        checkHTTPAvailable();
        executeQuery("newItemData",makeParams("itemId",itemId+"","refId",refId+"","value",value,"unit",unit));
    }

    public static int getItemId(String articleNum){
        checkHTTPAvailable();
        return Integer.parseInt(executeQuery("getItemId",makeParams("article",articleNum)));
    }

    public static void insertItem(int typeId, String articleNum, double weight, String web){
        checkHTTPAvailable();
        executeQuery("newItem",makeParams("type",typeId+"","article",articleNum,"weight",weight+"","web",web));
    }

    public static void insertComponent(String type, String version){
        checkHTTPAvailable();
        executeQuery("newComponent",makeParams("type",type,"version",version));
    }

    public static void setWeight(int itemId, double weight){
        checkHTTPAvailable();
        executeQuery("setWeight",makeParams("id",itemId+"","weight",weight+""));
    }

    public static boolean isScaleInUse(){
        checkHTTPAvailable();
        return Boolean.parseBoolean(executeQuery("scaleInUse",makeParams("")));
    }

    public static String getScaleValue(){
        checkHTTPAvailable();
        return executeQuery("getScaleValue",makeParams(""));
    }

    public static void setStateMicroScale(int userId, boolean state){
        checkHTTPAvailable();
        executeQuery("setStateScale",makeParams("state",state+"","userID",userId+""));
    }

    public static void updateStorageP(int id, int insidePos, int quantity, int maxQuantity){
        checkHTTPAvailable();
        executeQuery("updateStorageP",makeParams("id",id+"","insidePos",insidePos+"","quantity",quantity+"","maxQuantity",maxQuantity+""));
    }

    public static void insertStorageP(int storagehId, int itemId, int insidePos, int quantity, int minQuantity, int maxQuantity, boolean alarmAct){
        checkHTTPAvailable();
        executeQuery("insertStorageP",makeParams("storagehId",storagehId+"","itemId",itemId+"","insidePos",insidePos+"","quantity",quantity+"","minQuantity",minQuantity+"","maxQuantity",maxQuantity+"","alarmAct",alarmAct+""));
    }

    public static void updateDividers(int storagehId, boolean firstPar, boolean secondPar, boolean thirdPar){
        checkHTTPAvailable();
        executeQuery("updateDividers",makeParams("id",storagehId+"","first",firstPar+"","second",secondPar+"","third",thirdPar+""));
    }

    public static void updateQuantity(int id,int quantity){
        checkHTTPAvailable();
        executeQuery("updateQuantity",makeParams("id",id+"","quantity",quantity+""));
    }

    public static void deactivateLED(int storagePosition){
        checkHTTPAvailable();
        executeQuery("deactivateLED",makeParams("id",storagePosition+""));
    }

    public static boolean activateLED(int storagePosition, String color, int speed, boolean activ, boolean change){
        checkHTTPAvailable();
        String rs = executeQuery("activateLED",makeParams("id",storagePosition+"","color",color,"speed",speed+"","activ",activ+"","change",change+""));
        return Boolean.parseBoolean(rs);
    }

    public static boolean checkPassword(int id, String password){
        checkHTTPAvailable();
        return Boolean.parseBoolean(executeQuery("checkpass",makeParams("id",id+"","password",password)));
    }

    public static void setSignedIn(int id,boolean state){
        checkHTTPAvailable();
        executeQuery("setSignedIn",makeParams("id",id+"","state",state+""));
    }

    public static void deleteStoragePos(int posId){
        checkHTTPAvailable();
        executeQuery("deleteStoragep",makeParams("posId",posId+""));
    }

    private static String executeQuery(String method, StringBuilder params){
        if(!IsHTTPInUse) {
            IsHTTPInUse = true;
            try {
                OutputStreamWriter sw = DBConnector.connect();
                sw.write(getUrlParams(method, params));
                sw.flush();
                String result = DBConnector.readResult();
                IsHTTPInUse=false;
                return result;
            } catch (IOException e) {
                IsHTTPInUse=false;
            }
        }
        return null;
    }

    private static String getUrlParams(String method, StringBuilder params) throws IOException{
        StringBuffer urlBuffer = new StringBuffer();
        urlBuffer.append(URLEncoder.encode("method","utf-8"));
        urlBuffer.append('=');
        urlBuffer.append(URLEncoder.encode(method,"utf-8"));
        if(params!=null){
            urlBuffer.append(params);
        }
        return urlBuffer.toString();
    }

    private static StringBuilder makeParams(String ...s){
        StringBuilder createParams = new StringBuilder();
        int countParams = s.length;

        if(countParams==1){
            return null;
        }

        try {
            for (int i = 0; i < countParams; i += 2) {
                createParams.append("&");
                createParams.append(URLEncoder.encode(s[i], "UTF-8"));
                createParams.append("=");
                createParams.append(URLEncoder.encode(s[i + 1], "UTF-8"));
            }
            return createParams;
        }catch (UnsupportedEncodingException e){
        }
        return null;
    }

    private static void checkHTTPAvailable(){
        while(IsHTTPInUse){
        }
    }
}
