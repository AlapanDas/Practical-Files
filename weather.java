import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.ProtocolException;
import java.net.URL;

class weather {
    public static void show(String s) throws IOException, IOException {
        String site = "https://api.openweathermap.org/data/2.5/weather?q=" + s + "&appid=3e296e84c837be3621f0c16f176ec3a0";
        URL url;
        url = new URL(site);
        String res = null;
        HttpURLConnection conection = (HttpURLConnection) url.openConnection();
        try {
            conection.setRequestMethod("GET");
        } catch (ProtocolException e) {
            ;
        }
        int responseCode = conection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(conection.getInputStream()));
            StringBuffer response = new StringBuffer();
            while ((res = in .readLine()) != null) {
                response.append(res);
            } in .close();
            // print result
            System.out.println("JSON String Result " + response.toString());
            //GetAndPost.POSTRequest(response.toString());
        } else {
            System.out.println("GET NOT WORKED");
        }
    }
}
