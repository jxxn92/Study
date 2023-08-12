import java.util.*;

public class basic_collection{
    public static void main(String[] args) {
        Set<String> foods = new HashSet<>();

        // foods.add("치킨");
        // foods.add("피자");
        // foods.add("고구마말랭이");

        for(String food : foods){
            System.out.println(food);
        }

        if(foods.isEmpty()){
            System.out.println("목록이 비어있습니다.");
        
        } else {
            System.out.println("총 " + foods.size() + "개의 음식 목록이 존재합니다.");
        }
    }
}