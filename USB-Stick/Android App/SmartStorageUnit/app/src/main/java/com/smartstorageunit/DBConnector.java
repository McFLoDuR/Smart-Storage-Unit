package com.smartstorageunit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;

public class DBConnector {

    public static HttpsURLConnection con;
    public static String Website="https://smartstorageunit.ddns.net/MysqlConnector/DBConnector.php";

    public static OutputStreamWriter connect() throws IOException {
        HostnameVerifier hostnameVerifier = org.apache.http.conn.ssl.SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER;
        HttpsURLConnection.setDefaultHostnameVerifier(hostnameVerifier);

        URL url =new URL(Website);

        con= (HttpsURLConnection) url.openConnection();
        con.setConnectTimeout(5000);
        con.setDoOutput(true);
        OutputStreamWriter sw = new OutputStreamWriter(con.getOutputStream());
        return sw;
    }

    public static String readResult() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(con.getInputStream()));
        StringBuilder sb = new StringBuilder();
        String line = null;

        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        con.disconnect();
        return sb.toString();
    }
}

