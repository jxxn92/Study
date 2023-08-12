import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class basic_map{
    public static void main(String[] args) {
        Map<String, String> dictionary = new HashMap<>();
        dictionary.put("chicken","닭");
        dictionary.put("hippo","하마");


        if (dictionary.isEmpty()){
            System.out.println("단어가 하나도 존재하지 않습니다.");
            System.exit(0);
        } else{
            System.out.println(dictionary.size() +"개의 단어가 존재합니다.");
        }

        Set<Map.Entry<String, String>> entries = dictionary.entrySet();

        for(Map.Entry<String, String> entry : entries){
            String english = entry.getKey();
            String korean = entry.getValue();
            
            System.out.println(english + " : " + korean);
        }
    }
}