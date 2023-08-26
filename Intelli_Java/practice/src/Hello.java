public class Hello {
    public static void main(String[] args) {

        long start = System.nanoTime();

 
        long end = System.nanoTime();
        System.out.println("수행시간: " + (end - start) + " ns");

    }
}