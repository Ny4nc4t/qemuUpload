import java.io.File;
import java.io.IOException;

class Main {
   public static void main(String[] args) {
      try {
         File file = new File("~/qemuUpload/myfile.txt");
         
         if(file.createNewFile())System.out.println("Success!");
         else System.out.println ("Error, file already exists.");
      }
      catch(IOException ioe) {
         ioe.printStackTrace();
      }
   }
}
