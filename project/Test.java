import java.io.*;

public class Test{
    public static void main(String[] args) {
        try{
        FileOutputStream fos = new FileOutputStream("chicken.txt");
    }
        catch (FileNotFoundException e){
            System.out.println("error faced.");
        }

    }
}